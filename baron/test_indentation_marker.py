#!/usr/bin/python
# -*- coding:Utf-8 -*-

from indentation_marker import mark_indentation
from itertools import izip_longest


def check(input, output):
    for i, j in izip_longest(mark_indentation(input + [('ENDMARKER', ''), None]), output + [('ENDMARKER', ''), None]):
        assert i == j


def test_empty():
    check([], [])


def test_dummy():
    check([
        ('NAME', 'a'),
    ], [
        ('NAME', 'a'),
    ])


def test_dumy_if():
    check([
        ('IF', 'if'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('SPACE', '    '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('INDENT', ''),
        ('SPACE', '    '),
        ('PASS', 'pass'),
        ('DEDENT', ''),
    ])
