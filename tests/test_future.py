from baron.future import has_print_function, replace_print_by_name
from baron.baron import parse, tokenize
import json


def print_token_is_a_function(code):
    return has_print_function(tokenize(code))


def print_is_parsed_as_a_function(parsed_code):
    code_json = json.dumps(parsed_code)
    return '"type": "name", "value": "print"' in code_json \
           or '"value": "print", "type": "name"' in code_json


def test_no_future():
    code = "a = 1"
    assert not print_token_is_a_function(code)


def test_other_future():
    code = "from __future__ import other"
    assert not print_token_is_a_function(code)


def test_print_future():
    code = "from __future__ import print_function"
    assert print_token_is_a_function(code)


def test_print_future_as():
    code = "from __future__ import print_function as p_f"
    assert print_token_is_a_function(code)


def test_print_future_comma():
    code = "from __future__ import a, b, print_function"
    assert print_token_is_a_function(code)


def test_print_future_comma_as():
    code = "from __future__ import a as c, b as d, print_function as e"
    assert print_token_is_a_function(code)


def test_print_no_future_comma_as():
    code = "from __future__ import a as c, b as d"
    assert not print_token_is_a_function(code)


def test_print_future_in_parenthesis():
    code = "from __future__ import (a, b, print_function)"
    assert print_token_is_a_function(code)


def test_print_future_in_parenthesis_as():
    code = "from __future__ import (a as c, b as d, print_function as e)"
    assert print_token_is_a_function(code)


def test_print_no_future_in_parenthesis_as():
    code = "from __future__ import (a as c, b as d)"
    assert not print_token_is_a_function(code)


def test_print_future_second():
    code = """from __future__ import a, b as e
from __future__ import c, print_function"""
    assert print_token_is_a_function(code)


def test_auto_print_as_name():
    code = "from __future__ import print_function\nprint(a)"
    assert print_is_parsed_as_a_function(parse(code))


def test_auto_print_as_print():
    code = "print(a)"
    assert not print_is_parsed_as_a_function(parse(code))


def test_print_as_name():
    code = "print(a)"
    assert print_is_parsed_as_a_function(parse(code, True))


def test_print_as_print():
    code = "print(a)"
    assert not print_is_parsed_as_a_function(parse(code, False))


def test_replace_print_token():
    tokens = [('PRINT', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    after = [('NAME', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    assert after == replace_print_by_name(tokens)
