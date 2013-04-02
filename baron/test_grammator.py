#!/usr/bin/python
# -*- coding:Utf-8 -*-

from grammator import parser, Token

def parse(tokens, result):
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [None]))) == result

def test_int():
    parse([('INT', '1')], ["1"])
