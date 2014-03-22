# encoding: utf-8

import re
from utils import FlexibleIterator

to_group = (
    ("+", "="),
    ("-", "="),
    ("*", "="),
    ("/", "="),
    ("%", "="),
    ("&", "="),
    ("|", "="),
    ("^", "="),
    ("/", "/"),
    ("*", "*"),
    ("<", "<"),
    (">", ">"),
    ("=", "="),
    ("!", "="),
    ("<", ">"),
    ("<", "="),
    (">", "="),
    ("**", "="),
    ("//", "="),
    ("<<", "="),
    (">>", "="),
    ("\r", "\n"),
)

to_group_keys, _ = zip(*to_group)


def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None
    while True:
        if iterator.end():
            return

        current = iterator.next()
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += iterator.next()
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += iterator.next()
        if current in list('uUrRbB') and str(iterator.show_next()).startswith(('"', "'")):
            current += iterator.next()
        if str(current).lower() in ["ur", "br"] and str(iterator.show_next()).startswith(('"', "'")):
            current += iterator.next()
        if any(map(lambda x: re.match(x, current), (r'^\d+e$', r'^\d+\.\d*e$', r'^\.\d+e$'))):
            current += iterator.next()
            current += iterator.next()

            # I'm obligatory in a case where I have something like that:
            # ['123.123e', '[+-]', '123']
            assert re.match(r'^\d+[eE][-+]?\d+$', current) or re.match(r'^\d*.\d*[eE][-+]?\d+$', current)

        if current == "\\" and iterator.show_next() in ('\n', '\r\n'):
            current += iterator.next()
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += iterator.next()

        if current == "\\" and iterator.show_next() == "\r" and iterator.show_next(2) == "\n":
            current += iterator.next()
            current += iterator.next()
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += iterator.next()

        if re.match(r'^\s+$', current) and iterator.show_next() == "\\":
            current += iterator.next()
            current += iterator.next()
            if iterator.show_next() == "\n":
                current += iterator.next()
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += iterator.next()

        if (re.match(r'^\d+$', current) and iterator.show_next() and iterator.show_next() == ".") or\
           (current == "." and iterator.show_next() and re.match(r'^\d+[jJ]?$', iterator.show_next())):
            current += iterator.next()

            if iterator.show_next() and re.match(r'^\d*[jJ]?$', iterator.show_next()) and re.match(r'^\d*[jJ]?$', iterator.show_next()).group():
                current += iterator.next()

        if re.match(r'^\d+\.$', current) and iterator.show_next() and re.match(r'^\d*[eE]\d*$', iterator.show_next()):
            current += iterator.next()

        if re.match(r'^\d+\.?[eE]$', current) and iterator.show_next() and re.match(r'^\d+$', iterator.show_next()):
            current += iterator.next()

        if re.match(r'^\d+\.?\d*[eE]$', current) and iterator.show_next() and iterator.show_next() in "-+" and re.match(r'^\d+$', iterator.show_next(2) if iterator.show_next(2) else ""):
            current += iterator.next()
            current += iterator.next()

        yield current


def matching_found(to_group, current, target):
    return target in zip(*filter(lambda x: x[0] == current, to_group))[1]
