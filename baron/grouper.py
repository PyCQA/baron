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
        if current == "@" and re.match("[a-zA-Z_]+", iterator.show_next()):
            current += iterator.next()
        yield current


def matching_found(to_group, current, target):
    return target in zip(*filter(lambda x: x[0] == current, to_group))[1]
