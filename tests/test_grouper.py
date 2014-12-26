#!/usr/bin/python
# -*- coding:Utf-8 -*-

from baron.grouper import group


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
    assert group(["@", "pouet"]) == ["@", "pouet"]


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


def test_exponant():
    assert group(['1e', '+', '123']) == ['1e+123']
    assert group(['1e', '-', '123']) == ['1e-123']
    assert group(['1.1e', '+', '123']) == ['1.1e+123']
    assert group(['1.1e', '-', '123']) == ['1.1e-123']
    assert group(['.1e', '+', '123']) == ['.1e+123']
    assert group(['.1e', '-', '123']) == ['.1e-123']


def test_endl_with_backslash():
    assert group(['\\', '\n']) == ['\\\n']


def test_space_endl_with_backslash():
    assert group([' 	 ', '\\', '\n', '   ']) == [' 	 \\\n   ']
    assert group([' 	 ', '\\', '\n', 'pouet']) == [' 	 \\\n', 'pouet']


def test_regression():
    assert group(['0x045e', ':', ' ']) == ['0x045e', ':', ' ']
    assert group(['180', '.', '\n']) == ['180.', '\n']


def test_backslash_window_endl():
    assert group(['\\', '\r', '\n']) == ['\\\r\n']


def test_regression_float():
    assert group(['1', '.']) == ['1.']
    assert group(['.', '1']) == ['.1']
    assert group(['1', '.', '1']) == ['1.1']
    assert group(['7', '.', '629e', '-', '6']) == ['7.629e-6']


def test_complex():
    assert group(['.', '1j']) == ['.1j']
    assert group(['.', '1J']) == ['.1J']
    assert group(['1', '.', 'j']) == ['1.j']
    assert group(['1', '.', 'J']) == ['1.J']
    assert group(['1', '.', '1j']) == ['1.1j']
    assert group(['1', '.', '1J']) == ['1.1J']
    assert group(['1J']) == ['1J']
    assert group(['1e', '-', '1j']) == ['1e-1j']


def test_float_exponant():
    assert group(['1E1']) == ['1E1']
    assert group(['1E', '-', '2']) == ['1E-2']
    assert group(['1E', '+', '2']) == ['1E+2']
    assert group(['1', '.', 'E', '+', '2']) == ['1.E+2']
    assert group(['1', '.', 'E', '-', '2']) == ['1.E-2']
    assert group(['1', '.', 'E', '2']) == ['1.E2']
    assert group(['1', '.', 'E2']) == ['1.E2']
    assert group(['1e1']) == ['1e1']
    assert group(['1e', '-', '2']) == ['1e-2']
    assert group(['1e', '+', '2']) == ['1e+2']
    assert group(['1', '.', 'e', '+', '2']) == ['1.e+2']
    assert group(['1', '.', 'e', '-', '2']) == ['1.e-2']
    assert group(['1', '.', 'e', '2']) == ['1.e2']
    assert group(['1', '.', 'e2']) == ['1.e2']
    assert group(['.', '3e55']) == ['.3e55']

