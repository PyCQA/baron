#!/usr/bin/python
# -*- coding:Utf-8 -*-


from baron.spliter import split, UntreatedError
from baron.utils import python_version
import pytest


def test_empty():
    assert split("") == []


def test_print():
    assert split("print") == ["print"]


def test_print_space():
    assert split("print ") == ['print', ' ']


def test_import():
    assert split("import  pouet") == ["import", "  ", "pouet"]


def test_from_import():
    assert split(" from zob   import  pouet ") == [" ", "from", " ", "zob", "   ", "import", "  ", "pouet", " "]


def test_from_import_as():
    assert split("from a import b as c") == ["from", " ", "a", " ", "import", " ", "b", " ", "as", " ", "c"]


def test_underscore_variable():
    assert split("some_variable") == ["some_variable"]


def test_different_case():
    assert split("AbCd cDeF") == ["AbCd", " ", "cDeF"]


def test_decorator():
    assert split("@pouet") == ["@", "pouet"]


def test_tab_n_space():
    assert split("	 ") == ["	 "]


def test_several_spaces():
    assert split("     ") == ["     "]


def test_numbers():
    assert split("1234") == ["1234"]


def test_several_numbers():
    assert split("12 34") == ["12", " ", "34"]


def test_comma():
    assert split(",") == [","]


def test_comma_with_words():
    assert split("a, b") == ["a", ",", " ", "b"]


def test_dot():
    assert split(".") == ["."]


def test_dot_with_word():
    assert split("a.b") == ["a", ".", "b"]


def test_dot_with_words():
    assert split("a.b.c") == ["a", ".", "b", ".", "c"]


def test_colon():
    assert split(";") == [";"]


def test_colon_word():
    assert split("pouet;") == ["pouet", ";"]


def test_assign():
    assert split("a = b") == ["a", " ", "=", " ", "b"]


def test_call():
    assert split("function()") == ["function", "(", ")"]


def test_call_with_arg():
    assert split("function(a)") == ["function", "(", "a", ")"]


def test_call_with_args():
    assert split("function(a, b, c)") == ["function", "(", "a", ",", " ", "b", ",", " ", "c", ")"]


def test_call_with_kwarg():
    assert split("function(a=b)") == ["function", "(", "a", "=", "b", ")"]


def test_call_with_kwargs():
    assert split("function(a=b, c= d)") == ["function", "(", "a", "=", "b", ",", " ", "c", "=", " ", "d", ")"]


def test_call_with_start_args():
    assert split("function(*args)") == ["function", "(", "*", "args", ")"]


def test_call_with_start_kwargs():
    assert split("function(**kwargs)") == ["function", "(", "*", "*", "kwargs", ")"]


def test_function_def():
    assert split("def pouet(): pass") == ["def", " ", "pouet", "(", ")", ":", " ", "pass"]


def test_addition():
    assert split("a + 2") == ["a", " ", "+", " ", "2"]


def test_substraction():
    assert split("a - 2") == ["a", " ", "-", " ", "2"]


def test_multiplication():
    assert split("a * 2") == ["a", " ", "*", " ", "2"]


def test_division():
    assert split("a/2") == ["a", "/", "2"]


def test_power():
    assert split("a**2") == ["a", "*", "*", "2"]


def test_modulo():
    assert split("a % 2") == ["a", " ", "%", " ", "2"]


def test_binary_stuff():
    assert split("a^2") == ["a", "^", "2"]
    assert split("a&2") == ["a", "&", "2"]
    assert split("a|2") == ["a", "|", "2"]
    assert split("a << 2") == ["a", " ", "<", "<", " ", "2"]
    assert split("a >> 2") == ["a", " ", ">", ">", " ", "2"]


def test_operator_assign():
    assert split("a += 2") == ["a", " ", "+", "=", " ", "2"]
    assert split("a -= 2") == ["a", " ", "-", "=", " ", "2"]
    assert split("a *= 2") == ["a", " ", "*", "=", " ", "2"]
    assert split("a /= 2") == ["a", " ", "/", "=", " ", "2"]
    assert split("a %= 2") == ["a", " ", "%", "=", " ", "2"]
    assert split("a &= 2") == ["a", " ", "&", "=", " ", "2"]
    assert split("a |= 2") == ["a", " ", "|", "=", " ", "2"]
    assert split("a ^= 2") == ["a", " ", "^", "=", " ", "2"]
    assert split("a //= 2") == ["a", " ", "/", "/", "=", " ", "2"]
    assert split("a **= 2") == ["a", " ", "*", "*", "=", " ", "2"]
    assert split("a <<= 2") == ["a", " ", "<", "<", "=", " ", "2"]
    assert split("a >>= 2") == ["a", " ", ">", ">", "=", " ", "2"]


def test_factor():
    assert split("~a") == ["~", "a"]


def test_del_pouet():
    assert split("del pouet") == ["del", " ", "pouet"]


def test_pass():
    assert split("pass") == ["pass"]


def test_break():
    assert split("break") == ["break"]


def test_continue():
    assert split("continue") == ["continue"]


def test_return():
    assert split("return") == ["return"]


def test_return_stuff():
    assert split("return stuff") == ["return", " ", "stuff"]


def test_yield():
    assert split("yield") == ["yield"]


def test_yield_stuff():
    assert split("yield stuff") == ["yield", " ", "stuff"]


def test_raise():
    assert split("raise") == ["raise"]


def test_raise_stuff():
    assert split("raise Exception()") == ["raise", " ", "Exception", "(", ")"]


def test_global_stuff():
    assert split("global stuff") == ["global", " ", "stuff"]


def test_exec():
    assert split("exec") == ["exec"]


def test_exec_stuff():
    assert split("exec stuff") == ["exec", " ", "stuff"]


def test_assert():
    assert split("assert") == ["assert"]


def test_assert_stuff():
    assert split("assert stuff") == ["assert", " ", "stuff"]


def test_line_end():
    assert split("\n") == ["\n"]


def test_line_end_windows():
    assert split("\r\n") == ["\r", "\n"]


def test_if():
    assert split("if ab: pass") == ["if", " ", "ab", ":", " ", "pass"]


def test_if_elif_else():
    assert split("if a:\n pass\nelif b:\n pass\nelse: \n pass") == ["if", " ", "a", ":", "\n", " ", "pass", "\n", "elif", " ", "b", ":", "\n", " ", "pass", "\n", "else", ":", " ", "\n", " ", "pass"]


def test_while():
    assert split("while a: pass") == ["while", " ", "a", ":", " ", "pass"]


def test_lambda():
    assert split("lambda x: x + 1") == ["lambda", " ", "x", ":", " ", "x", " ", "+", " ", "1"]


def test_for():
    assert split("for a in b: pass") == ["for", " ", "a", " ", "in", " ", "b", ":", " ", "pass"]


def test_empty_list():
    assert split("[]") == ["[", "]"]


def test_list():
    assert split("[a, b, c]") == ["[", "a", ",", " ", "b", ",", " ", "c", "]"]


def test_empty_dict():
    assert split("{}") == ["{", "}"]


def test_dict():
    assert split("{a: b, c: d}") == ["{", "a", ":", " ", "b", ",", " ", "c", ":", " ", "d", "}"]


def test_not():
    assert split("!a") == ["!", "a"]


def test_not_equal():
    assert split("a != b") == ["a", " ", "!", "=", " ", "b"]


def test_backquote():
    assert split("`a`") == ["`", "a", "`"]


def test_number_in_var():
    assert split("a1") == ["a1"]


def test_comment():
    assert split("# a b c d") == ["# a b c d"]


def test_comments():
    assert split("# a b c d\n# pouet") == ["# a b c d", "\n", "# pouet"]


def test_empty_string():
    assert split("''") == ["''"]


def test_string():
    assert split("'pouet pouet'") == ["'pouet pouet'"]


def test_empty_string_other_quotes():
    assert split('"pouet pouet"') == ['"pouet pouet"']


def test_multi_string():
    assert split("'''pouet pouet'''") == ["'''pouet pouet'''"]


def test_multi_string_other_quotes():
    assert split('"""pouet pouet"""') == ['"""pouet pouet"""']


def test_missing_quote_yields_error():
    with pytest.raises(UntreatedError):
        split("'")

    with pytest.raises(UntreatedError):
        split("'''")

    with pytest.raises(UntreatedError):
        split('"')

    with pytest.raises(UntreatedError):
        split('"""')


def test_escape():
    assert split("\\\\") == ["\\", "\\"]


def test_escape_in_string():
    assert split("'\\\\'") == ["'\\\\'"]


def test_other_escape_string():
    assert split("'\\\\'") == ["'\\\\'"]


def test_hexa():
    assert split("0x7F") == ["0x7F"]


def test_multi_string_with_same_quotes_in():
    assert split('"""pouet " "" pouet"""') == ['"""pouet " "" pouet"""']


def test_comment_backslash():
    assert split('# pouet \\\npouet') == ["# pouet \\", "\n", "pouet"]


def test_backslash_in_comment():
    assert split("# pouet \\t pouet\npouet") == ["# pouet \\t pouet", "\n", "pouet"]


def test_regression():
    assert split("(r'[\"\\'](.|\n|\r)*[\"\\']', 'STRING'),") == ["(", "r", "'[\"\\'](.|\n|\r)*[\"\\']'", ",", " ", "'STRING'", ")", ","]


# TODO: make this test pass in python3 also
# requires to remove dependency on ast.py
if python_version == 2:
    def test_remove_crap():
        assert split("\x0c\xef\xbb\xbf") == []
