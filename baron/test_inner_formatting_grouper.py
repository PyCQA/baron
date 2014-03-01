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


def test_parenthesis():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', '', '', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_parenthesis_one_space():
    assert group([
        ('LEFT_PARENTHESIS', '(', ' '),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', ' ', '', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_parenthesis_two_space():
    assert group([
        ('LEFT_PARENTHESIS', '(', ' ', ' '),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', ' ', ' ', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_two_parenthesis():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', '', '', [], [('ENDL', '\n'), ('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_two_parenthesis_comma():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('COMMA', ','),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', '', '', [], [('ENDL', '\n'), ]),
        ('COMMA', ',', '', '', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]
