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

        # classical grouping using to_group
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += next(iterator)
        if current in to_group_keys and matching_found(to_group, current, iterator.show_next()):
            current += next(iterator)

        # unicode/raw/binary string notation
        if current in list('uUrRbB') and str(iterator.show_next()).startswith(('"', "'")):
            current += next(iterator)

        # in case of unicode_raw or binary_raw string notation
        if str(current).lower() in ["ur", "br"] and str(iterator.show_next()).startswith(('"', "'")):
            current += next(iterator)

        # float exponant notation
        if any([re.match(x, current) for x in (r'^\d+[eE]$', r'^\d+\.\d*[eE]$', r'^\.\d+[eE]$')]):
            current += next(iterator)
            current += next(iterator)

            # It's required in a case where I have something like that:
            # ['123.123e', '[+-]', '123']
            assert re.match(r'^\d+[eE][-+]?\d+[jJ]?$', current) or re.match(r'^\d*.\d*[eE][-+]?\d+[jJ]?$', current)

        # escaped endl
        if current == "\\" and iterator.show_next() in ('\n', '\r\n'):
            current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        # escaped endl in window notation
        if current == "\\" and iterator.show_next() == "\r" and iterator.show_next(2) == "\n":
            current += next(iterator)
            current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        # space before escaped endl
        if re.match(r'^\s+$', current) and iterator.show_next() == "\\":
            current += next(iterator)
            current += next(iterator)
            if iterator.show_next() == "\n":
                current += next(iterator)
            if re.match(r'^\s+$', str(iterator.show_next())):
                current += next(iterator)

        # complex number notation
        if (re.match(r'^\d+$', current) and match_on_next(r'^\.$', iterator)) or\
           (current == "." and match_on_next(r'^\d+([jJ]|[eE]\d*)?$', iterator)):
            current += next(iterator)

            if match_on_next(r'^\d*[jJ]?$', iterator) and match_on_next(r'^\d*[jJ]?$', iterator).group():
                current += next(iterator)

        if re.match(r'^\d+\.$', current) and match_on_next(r'^\d*[eE]\d*$', iterator):
            current += next(iterator)

        if re.match(r'^\d+\.?[eE]$', current) and match_on_next(r'^\d+$', iterator):
            current += next(iterator)

        if re.match(r'^\d*\.?\d*[eE]$', current) and match_on_next(r'^[-+]$', iterator) and iterator.show_next(2) and re.match(r'^\d+$', iterator.show_next(2)):
            current += next(iterator)
            current += next(iterator)

        yield current


def matching_found(to_group, current, target):
    return target in [x[1] for x in to_group if x[0] == current]
