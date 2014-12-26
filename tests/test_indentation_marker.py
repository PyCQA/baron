#!/usr/bin/python
# -*- coding:Utf-8 -*-

from baron.indentation_marker import mark_indentation
from .test_utils import zip_longest


def check(input, output):
    for i, j in zip_longest(mark_indentation(input + [('ENDMARKER', ''), None]), output + [('ENDMARKER', ''), None]):
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
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
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
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '        ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '        ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
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
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])


def test_dummy_if_followed_blank_line():
    """
    if a:

        pass
    """
    check([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('INDENT', ''),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ])


def test_dumy_if_dendent_quite_a_lot():
    """
    if a:
        if b:
            if c:
                pass

    pouet
    """
    check([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])


def test_dumy_if_dendent_a_lot():
    """
    if a:
        if b:
            if c:
                pass
        if d:
            pass
            if e:
                pass

    pouet
    """
    check([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'pouet'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 1)]),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 3)]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('DEDENT', ''),
        ('NAME', 'pouet'),
    ])


def test_trailing_spaces():
    """
    if a:
        if b:
 
 
            pass
    """
    check([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('DEDENT', ''),
    ])


def test_tab_and_spaces_because_some_people_are_horrible():
    """
    if a:
            pass
    	pass
    """
    check([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '	')]),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ' * 2)]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], [('SPACE', '	')]),
        ('PASS', 'pass'),
        ('DEDENT', ''),
    ])


def test_try_pass_on_same_line():
    """
    try: pass

    except:
        pass
    """
    check([
        ('TRY', 'try'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('EXCEPT', 'except'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        ('TRY', 'try'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('EXCEPT', 'except'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ])

