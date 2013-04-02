#!/usr/bin/python
# -*- coding:Utf-8 -*-

from grammator import parser, Token

def parse(tokens, result):
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [('ENDMARKER', ''), None]))) == result

def test_empty():
    parse([], [])

def test_space():
    parse([('SPACE', '   ')], [{"type": "space", "section": "space", "value": "   "}])

def test_int():
    parse([('INT', '1')], [{"type": "int", "section": "number", "value": "1"}])

def test_endl():
    parse([('ENDL', '\n')], [{"type": "endl", "section": "separator", "value": "\n", "before_space": ""}])

def test_space_endl():
    parse([('SPACE', '   '), ('ENDL', '\n')], [{"type": "endl", "section": "separator", "value": "\n", "before_space": "   "}])

def test_some_stuff():
    parse([('INT', '3'), ('SPACE', '   '), ('ENDL', '\n'), ('INT', '42')], [{"type": "int", "section": "number", "value": "3"}, {"type": "endl", "section": "separator", "value": "\n", "before_space": "   "}, {"type": "int", "section": "number", "value": "42"}])
