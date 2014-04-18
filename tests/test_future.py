from baron.future import has_print_function, replace_print_by_name
from baron.baron import parse,tokenize
import json


def print_token_is_a_function(code):
    return has_print_function(tokenize(code))


def print_is_parsed_as_a_function(parsed_code):
    code_json = json.dumps(parsed_code)
    return '"type": "name", "value": "print"' in code_json \
           or '"value": "print", "type": "name"' in code_json


def test_no_future():
    code = "a = 1"
    assert print_token_is_a_function(code) == False


def test_other_future():
    code = "from future import other"
    assert print_token_is_a_function(code) == False


def test_print_future():
    code = "from future import print_function"
    assert print_token_is_a_function(code) == True


def test_auto_print_as_name():
    code = "from future import print_function\nprint(a)"
    assert print_is_parsed_as_a_function(parse(code)) == True


def test_auto_print_as_print():
    code = "print(a)"
    assert print_is_parsed_as_a_function(parse(code)) == False


def test_print_as_name():
    code = "print(a)"
    assert print_is_parsed_as_a_function(parse(code, True)) == True


def test_print_as_print():
    code = "print(a)"
    assert print_is_parsed_as_a_function(parse(code, False)) == False


def test_replace_print_token():
    tokens = [('PRINT', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    after = [('NAME', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    assert after == replace_print_by_name(tokens)
