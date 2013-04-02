#!/usr/bin/python
# -*- coding:Utf-8 -*-

from grouper import group

def test_empty():
    assert group([]) == []

def test_one():
    assert group(['a']) == ['a']

def test_random():
    assert group(list("abcdef")) == list("abcdef")

def test_add_egual():
    assert group(["+", "="]) == ["+="]

def test_add_add():
    assert group(["+", "+"]) == ["+", "+"]

def test_add_egual_double():
    assert group(["+", "=", "+", "="]) == ["+=", "+="]

def test_add_egual_random():
    assert group(list(" qsd += qsd")) == [" ", "q", "s", "d", " ", "+=", " ", "q", "s", "d"]

def test_minus_egual():
    assert group(["-", "="]) == ["-="]

def test_mult_egual():
    assert group(["*", "="]) == ["*="]

def test_div_egual():
    assert group(["/", "="]) == ["/="]

def test_modulo_egual():
    assert group(["%", "="]) == ["%="]

def test_amper_egual():
    assert group(["&", "="]) == ["&="]

def test_bar_egual():
    assert group(["|", "="]) == ["|="]

def test_power_egual():
    assert group(["^", "="]) == ["^="]

def test_less_less():
    assert group(["<", "<"]) == ["<<"]

def test_more_more():
    assert group([">", ">"]) == [">>"]

def test_egual_egual():
    assert group(["=", "="]) == ["=="]

def test_different():
    assert group(["!", "="]) == ["!="]

def test_different_old_style():
    assert group(["<", ">"]) == ["<>"]

def test_power_power_egual():
    assert group(["*", "*", "="]) == ["**="]

def test_div_div_egual():
    assert group(["/", "/", "="]) == ["//="]

def test_less_less_egual():
    assert group(["<", "<", "="]) == ["<<="]

def test_more_more_egual():
    assert group([">", ">", "="]) == [">>="]

def test_decorator():
    assert group(["@", "pouet"]) == ["@pouet"]

def test_endl():
    assert group(["\r", "\n"]) == ["\r\n"]

def test_raw_string():
    assert group(["r", "'pouet'"]) == ["r'pouet'"]
    assert group(["R", "'pouet'"]) == ["R'pouet'"]

def test_unicode_string():
    assert group(["u", "'pouet'"]) == ["u'pouet'"]
    assert group(["U", "'pouet'"]) == ["U'pouet'"]

def test_binary_string():
    assert group(["b", "'pouet'"]) == ["b'pouet'"]
    assert group(["B", "'pouet'"]) == ["B'pouet'"]

def test_binary_raw_string():
    assert group(["br", "'pouet'"]) == ["br'pouet'"]
    assert group(["Br", "'pouet'"]) == ["Br'pouet'"]
    assert group(["bR", "'pouet'"]) == ["bR'pouet'"]
    assert group(["BR", "'pouet'"]) == ["BR'pouet'"]

def test_unicode_raw_string():
    assert group(["ur", "'pouet'"]) == ["ur'pouet'"]
    assert group(["Ur", "'pouet'"]) == ["Ur'pouet'"]
    assert group(["uR", "'pouet'"]) == ["uR'pouet'"]
    assert group(["UR", "'pouet'"]) == ["UR'pouet'"]
