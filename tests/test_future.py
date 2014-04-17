from baron.future import has_print_function, replace_print_by_name
from baron.baron import parse,tokenize
import json


def assert_print_function(code, is_print_function):
    assert has_print_function(tokenize(code)) == is_print_function


def assert_print_is_function(code, is_function):
    count = json.dumps(code).find('{"type": "name", "value": "print"}')
    if is_function:
        assert count > 0
    else:
        assert count == -1


def test_no_future():
    code = "a = 1"
    assert_print_function(code, False)


def test_other_future():
    code = "from future import other"
    assert_print_function(code, False)


def test_print_future():
    code = "from future import print_function"
    assert_print_function(code, True)


def test_auto_print_as_name():
    code = "from future import print_function\nprint(a)"
    assert_print_is_function(parse(code), True)


def test_auto_print_as_print():
    code = "print(a)"
    assert_print_is_function(parse(code), False)


def test_print_as_name():
    code = "print(a)"
    assert_print_is_function(parse(code, True), True)


def test_print_as_print():
    code = "print(a)"
    assert_print_is_function(parse(code, False), False)


def test_replace_print_token():
    tokens = [('PRINT', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    after = [('NAME', 'print'), ('LEFT_PARENTHESIS', '('), ('NAME', 'A'), ('RIGHT_PARENTHESIS', ')'), ('ENDMARKER', '')]
    assert after == replace_print_by_name(tokens)
