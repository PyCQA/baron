#!/usr/bin/python
# -*- coding:Utf-8 -*-

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
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n'),]),
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
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n'),]),
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
        ('LEFT_BRACKET', '{', [], [('ENDL', '\n'),]),
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
        ('LEFT_SQUARE_BRACKET', '[', [], [('ENDL', '\n'),]),
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
