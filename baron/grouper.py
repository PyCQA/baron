# encoding: utf-8

import re
from .utils import FlexibleIterator

to_group = (
    ("+", "="),
    ("-", "="),
    ("*", "="),
    ("/", "="),
    ("%", "="),
    ("&", "="),
    ("|", "="),
    ("^", "="),
    ("@", "="),
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
    (".", "."),
    ("..", "."),
    ("-", ">"),
)

to_group_keys, _ = list(zip(*to_group))


def group(sequence):
    return list(group_generator(sequence))


def match_on_next(regex, iterator):
    return iterator.show_next() and re.match(regex, iterator.show_next())


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None
    while True:
        if iterator.end():
            return

        current = next(iterator)
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += next(iterator)
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += next(iterator)
        if current in list('uUfFrRbB') and str(iterator.show_next()).startswith(('"', "'")):
            current += next(iterator)
        if str(current).lower() in ["ur", "br", "fr", "rf"] and str(iterator.show_next()).startswith(('"', "'")):
            current += next(iterator)
        if any([re.match(x, current) for x in (r'^\d+[eE]$', r'^\d+\.\d*[eE]$', r'^\.\d+[eE]$')]):
            current += next(iterator)
            current += next(iterator)

            # It's required in a case where I have something like that:
            # ['123.123e', '[+-]', '123']
            assert re.match(r'^\d+[eE][-+]?\d+[jJ]?$', current) or re.match(r'^\d*.\d*[eE][-+]?\d+[jJ]?$', current)

        if current == "\\" and iterator.show_next() in ('\n', '\r\n'):
            current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        if current == "\\" and iterator.show_next() == "\r" and iterator.show_next(2) == "\n":
            current += next(iterator)
            current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        if re.match(r'^\s+$', current) and iterator.show_next() == "\\":
            current += next(iterator)
            current += next(iterator)
            if iterator.show_next() == "\n":
                current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        if (re.match(r'^[_\d]+$', current) and match_on_next(r'^\.$', iterator)) or\
           (current == "." and match_on_next(r'^\d+[_\d]*([jJ]|[eE]\d*)?$', iterator)):
            current += next(iterator)

            if match_on_next(r'^[_\d]*[jJ]?$', iterator) and match_on_next(r'^[_\d]*[jJ]?$', iterator).group():
                current += next(iterator)

        if re.match(r'^\d+\.$', current) and match_on_next(r'^\d*[eE]\d*$', iterator):
            current += next(iterator)

        if re.match(r'^\d+\.?[eE]$', current) and match_on_next(r'^\d+$', iterator):
            current += next(iterator)

        if re.match(r'^\d*\.?\d*[eE]$', current) and not re.match('[eE]', current) and match_on_next(r'^[-+]$', iterator) and iterator.show_next(2) and re.match(r'^\d+$', iterator.show_next(2)):
            current += next(iterator)
            current += next(iterator)

        # edge case where 2 dots follow themselves but not 3 (an ellipsis)
        if current == "..":
            yield "."
            yield "."
            continue

        yield current


def matching_found(to_group, current, target):
    return target in [x[1] for x in to_group if x[0] == current]
