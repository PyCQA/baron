#!/usr/bin/python
# -*- coding:Utf-8 -*-

from indentation_marker import mark_indentation
from itertools import izip_longest


def check(input, output):
    for i, j in izip_longest(mark_indentation(input + [('ENDMARKER', ''), None]), output + [('ENDMARKER', ''), None]):
        assert i == j


def test_empty():
    ""
    check([], [])


def test_dummy():
    "a"
    check([
        ('NAME', 'a'),
    ], [
        ('NAME', 'a'),
    ])


def test_dumy_if():
    """
    if a:
        pass
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('DEDENT', ''),
    ])


def test_dumy_if_if():
    """
    if a:
        if b:
            pass
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '        '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('IF', 'if', '', ' '),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', '',  '        '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('DEDENT', ''),
        ('DEDENT', ''),
    ])

def test_dummy_if_followed():
    """
    if a:
        pass
    pouet
    """
    check([
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', ''),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', '', ' '),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', '', '    '),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', '', ''),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])
