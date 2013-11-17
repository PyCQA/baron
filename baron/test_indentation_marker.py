#!/usr/bin/python
# -*- coding:Utf-8 -*-

from indentation_marker import mark_indentation


def check(input, output):
    assert mark_indentation(input) == output


def test_empty():
    check([], [])


def test_dummy():
    check([
        ('NAME', 'a'),
    ], [
        ('NAME', 'a'),
    ])
