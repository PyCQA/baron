#!/usr/bin/python
# -*- coding:Utf-8 -*-

from inner_formatting_grouper import group

def test_empty():
    assert group([]) == []


def test_some_stuff():
    assert group([
        ('INT', '1'),
        ('PLUS', '+', ' ', ' '),
        ('INT', '2')
    ]) == [
        ('INT', '1'),
        ('PLUS', '+', ' ', ' '),
        ('INT', '2')
    ]
