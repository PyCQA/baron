#!/usr/bin/python
# -*- coding:Utf-8 -*-

from baron.grouper import group
from baron.spliter import split


def grouper_test(input_, split_output, group_output):
    assert split(input_) == split_output
    assert group(split_output) == group_output


def test_empty():
    grouper_test("", [], [])


def test_one():
    grouper_test('a', ['a'], ['a'])


def test_random():
    assert group(list("abcdef")) == list("abcdef")


def test_add_egual():
    grouper_test("+=", ["+", "="], ["+="])


def test_add_add():
    grouper_test("++", ["+", "+"], ["+", "+"])


def test_add_egual_double():
    grouper_test("+=+=", ["+", "=", "+", "="], ["+=", "+="])


def test_add_egual_random():
    grouper_test(" qsd+=qsd", [' ', 'qsd', '+', '=', 'qsd'], [' ', 'qsd', '+=', 'qsd'])


def test_minus_egual():
    grouper_test("-=", ["-", "="], ["-="])


def test_mult_egual():
    grouper_test("*=", ["*", "="], ["*="])


def test_div_egual():
    grouper_test("/=", ["/", "="], ["/="])


def test_modulo_egual():
    grouper_test("%=", ["%", "="], ["%="])


def test_amper_egual():
    grouper_test("&=", ["&", "="], ["&="])


def test_bar_egual():
    grouper_test("|=", ["|", "="], ["|="])


def test_power_egual():
    grouper_test("^=", ["^", "="], ["^="])


def test_less_less():
    grouper_test("<<", ["<", "<"], ["<<"])


def test_more_more():
    grouper_test(">>", [">", ">"], [">>"])


def test_egual_egual():
    grouper_test("==", ["=", "="], ["=="])


def test_different():
    grouper_test("!=", ["!", "="], ["!="])


def test_inferior_egual():
    grouper_test(">=", [">", "="], [">="])


def test_superior_egual():
    grouper_test("<=", ["<", "="], ["<="])


def test_different_old_style():
    grouper_test("<>", ["<", ">"], ["<>"])


def test_power_power_egual():
    grouper_test("**=", ["*", "*", "="], ["**="])


def test_div_div_egual():
    grouper_test("//=", ["/", "/", "="], ["//="])


def test_less_less_egual():
    grouper_test("<<=", ["<", "<", "="], ["<<="])


def test_more_more_egual():
    grouper_test(">>=", [">", ">", "="], [">>="])


def test_decorator():
    grouper_test("@pouet", ["@", "pouet"], ["@", "pouet"])


def test_endl():
    grouper_test("\r\n", ["\r", "\n"], ["\r\n"])


def test_raw_string():
    grouper_test("r'pouet'", ["r", "'pouet'"], ["r'pouet'"])
    grouper_test("R'pouet'", ["R", "'pouet'"], ["R'pouet'"])


def test_unicode_string():
    grouper_test("u'pouet'", ["u", "'pouet'"], ["u'pouet'"])
    grouper_test("U'pouet'", ["U", "'pouet'"], ["U'pouet'"])


def test_binary_string():
    grouper_test("b'pouet'", ["b", "'pouet'"], ["b'pouet'"])
    grouper_test("B'pouet'", ["B", "'pouet'"], ["B'pouet'"])


def test_binary_raw_string():
    grouper_test("br'pouet'", ["br", "'pouet'"], ["br'pouet'"])
    grouper_test("Br'pouet'", ["Br", "'pouet'"], ["Br'pouet'"])
    grouper_test("bR'pouet'", ["bR", "'pouet'"], ["bR'pouet'"])
    grouper_test("BR'pouet'", ["BR", "'pouet'"], ["BR'pouet'"])


def test_unicode_raw_string():
    grouper_test("ur'pouet'", ["ur", "'pouet'"], ["ur'pouet'"])
    grouper_test("Ur'pouet'", ["Ur", "'pouet'"], ["Ur'pouet'"])
    grouper_test("uR'pouet'", ["uR", "'pouet'"], ["uR'pouet'"])
    grouper_test("UR'pouet'", ["UR", "'pouet'"], ["UR'pouet'"])


def test_exponant():
    grouper_test("1e+123", ['1e', '+', '123'], ['1e+123'])
    grouper_test("1e-123", ['1e', '-', '123'], ['1e-123'])
    grouper_test("1.1e+123", ['1', '.', '1e', '+', '123'], ['1.1e+123'])
    grouper_test("1.1e-123", ['1', '.', '1e', '-', '123'], ['1.1e-123'])
    grouper_test(".1e+123", ['.', '1e', '+', '123'], ['.1e+123'])
    grouper_test(".1e-123", ['.', '1e', '-', '123'], ['.1e-123'])


def test_endl_with_backslash():
    grouper_test("\\\n", ['\\', '\n'], ['\\\n'])


def test_space_endl_with_backslash():
    grouper_test(" 	 \\\n   ", [' 	 ', '\\', '\n', '   '], [' 	 \\\n   '])
    grouper_test(" 	 \\\npouet", [' 	 ', '\\', '\n', 'pouet'], [' 	 \\\n', 'pouet'])


def test_number_with_backslash():
    grouper_test("3\\\n", ['3', '\\', '\n'], ['3', '\\\n'])


def test_regression():
    grouper_test("0x045e: ", ['0x045e', ':', ' '], ['0x045e', ':', ' '])
    grouper_test("180.\n", ['180', '.', '\n'], ['180.', '\n'])


def test_backslash_window_endl():
    grouper_test("\\\r\n", ['\\', '\r', '\n'], ['\\\r\n'])


def test_regression_float():
    grouper_test('1.', ['1', '.'], ['1.'])
    grouper_test('.1', ['.', '1'], ['.1'])
    grouper_test('1.1', ['1', '.', '1'], ['1.1'])
    grouper_test('7.629e-6', ['7', '.', '629e', '-', '6'], ['7.629e-6'])


def test_complex():
    grouper_test(".1j", ['.', '1j'], ['.1j'])
    grouper_test(".1J", ['.', '1J'], ['.1J'])
    grouper_test("1.j", ['1', '.', 'j'], ['1.j'])
    grouper_test("1.J", ['1', '.', 'J'], ['1.J'])
    grouper_test("1.1j", ['1', '.', '1j'], ['1.1j'])
    grouper_test("1.1J", ['1', '.', '1J'], ['1.1J'])
    grouper_test("1J", ['1J'], ['1J'])
    grouper_test("1e-1j", ['1e', '-', '1j'], ['1e-1j'])
    grouper_test("1e1j", ['1e1j'], ['1e1j'])


def test_float_exponant():
    grouper_test("1E1", ['1E1'], ['1E1'])
    grouper_test("1E-2", ['1E', '-', '2'], ['1E-2'])
    grouper_test("1E+2", ['1E', '+', '2'], ['1E+2'])
    grouper_test("1.E+2", ['1', '.', 'E', '+', '2'], ['1.E+2'])
    grouper_test("1.E-2", ['1', '.', 'E', '-', '2'], ['1.E-2'])
    grouper_test("1.E2", ['1', '.', 'E2'], ['1.E2'])
    grouper_test("1e1", ['1e1'], ['1e1'])
    grouper_test("1e-2", ['1e', '-', '2'], ['1e-2'])
    grouper_test("1e+2", ['1e', '+', '2'], ['1e+2'])
    grouper_test("1.e+2", ['1', '.', 'e', '+', '2'], ['1.e+2'])
    grouper_test("1.e-2", ['1', '.', 'e', '-', '2'], ['1.e-2'])
    grouper_test("1.e2", ['1', '.', 'e2'], ['1.e2'])
    grouper_test(".3e55", ['.', '3e55'], ['.3e55'])


def test_float_with_underscores():
    grouper_test(".098_765", ['.', '098_765'], ['.098_765'])
    grouper_test("123.098_765", ['123', '.', '098_765'], ['123.098_765'])
    grouper_test("123_456.098", ['123_456', '.', '098'], ['123_456.098'])
    grouper_test("123_456.098_765", ['123_456', '.', '098_765'], ['123_456.098_765'])


def test_arrow():
    grouper_test("->", ['-', '>'], ['->'])


def test_dot_dot():
    grouper_test("..", ['.', '.'], ['.', '.'])


def test_dot_dot_dot():
    grouper_test("...", ['.', '.', '.'], ['...'])
