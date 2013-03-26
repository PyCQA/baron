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

def test_inferior_egual():
    assert group([">", "="]) == [">="]

def test_superior_egual():
    assert group(["<", "="]) == ["<="]

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
