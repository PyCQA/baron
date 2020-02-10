#!/usr/bin/python
# -*- coding:utf-8 -*-

from baron.inner_formatting_grouper import group


def test_empty():
    assert group([]) == []


def test_some_stuff():
    assert group([
        ('INT', '1'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('INT', '2')
    ]) == [
        ('INT', '1'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('INT', '2')
    ]


def test_parenthesis():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_parenthesis_one_space():
    assert group([
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')]),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_parenthesis_two_space():
    assert group([
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' '), ('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_two_parenthesis():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n'), ('ENDL', '\n')]),
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
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n'), ]),
        ('COMMA', ',', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_tuple_one():
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('COMMA', ','),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n'), ]),
        ('NAME', 'a'),
        ('COMMA', ',', [('ENDL', '\n')], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('RIGHT_PARENTHESIS', ')', [('ENDL', '\n')], []),
    ]


def test_set_one():
    assert group([
        ('LEFT_BRACKET', '{'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('COMMA', ','),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('RIGHT_BRACKET', '}'),
    ]) == [
        ('LEFT_BRACKET', '{', [], [('ENDL', '\n'), ]),
        ('NAME', 'a'),
        ('COMMA', ',', [('ENDL', '\n')], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('RIGHT_BRACKET', '}', [('ENDL', '\n')], []),
    ]


def test_list_one():
    assert group([
        ('LEFT_SQUARE_BRACKET', '['),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('COMMA', ','),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ]) == [
        ('LEFT_SQUARE_BRACKET', '[', [], [('ENDL', '\n'), ]),
        ('NAME', 'a'),
        ('COMMA', ',', [('ENDL', '\n')], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('RIGHT_SQUARE_BRACKET', ']', [('ENDL', '\n')], []),
    ]


def test_dict_one():
    assert group([
        ('LEFT_BRACKET', '{'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('COMMA', ','),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('RIGHT_BRACKET', '}'),
    ]) == [
        ('LEFT_BRACKET', '{', [], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('COLON', ':', [('ENDL', '\n')], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('COMMA', ',', [('ENDL', '\n')], [('ENDL', '\n')]),
        ('NAME', 'a'),
        ('RIGHT_BRACKET', '}', [('ENDL', '\n')], []),
    ]


def test_number_backslash():
    assert group([
        ('INT', '3'),
        ('SPACE', '\\'),
    ]) == [
        ('INT', '3'),
        ('SPACE', '\\'),
    ]


def test_number_backslash_newline():
    assert group([
        ('INT', '3'),
        ('SPACE', '\\\n'),
    ]) == [
        ('INT', '3'),
        ('SPACE', '\\\n'),
    ]


def test_nested_grouping_after_endl():
    """
    (b
     [0])
    """
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('ENDL', '\n'),
        ('SPACE', ' '),
        ('LEFT_SQUARE_BRACKET', '['),
        ('INT', '0'),
        ('RIGHT_SQUARE_BRACKET', ']'),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('LEFT_SQUARE_BRACKET', '[', [('ENDL', '\n'), ('SPACE', ' ')], []),
        ('INT', '0'),
        ('RIGHT_SQUARE_BRACKET', ']'),
        ('RIGHT_PARENTHESIS', ')'),
    ]


def test_equal():
    """
    (a = b)
    """
    assert group([
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('EQUAL', '='),
        ('SPACE', ' '),
        ('RIGHT_PARENTHESIS', ')'),
    ]) == [
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
    ]
