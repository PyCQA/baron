#!/usr/bin/python
# -*- coding:Utf-8 -*-


from baron.tokenizer import tokenize, KEYWORDS


def match(string, token):
    assert tokenize([string]) == [(token, string), ('ENDMARKER', ''), None]


def test_empty():
    assert tokenize([]) == [('ENDMARKER', ''), None]


def test_name():
    match('a', 'NAME')
    match('pouet', 'NAME')


def test_name__():
    match('_a', 'NAME')


def test_name_number():
    match('a123', 'NAME')


def test_await_as_name():
    # not a real keyword in python
    match('await', 'NAME')


def test_asyc_as_name():
    # not a real keyword in python
    match('async', 'NAME')


def test_number():
    match('1234', 'INT')
    match('1234L', 'LONG')
    match('1234l', 'LONG')


def test_float():
    match('1234.', 'FLOAT')
    match('.1234', 'FLOAT')
    match('1234.1234', 'FLOAT')
    match('1234.L', 'FLOAT')
    match('.1234L', 'FLOAT')
    match('1234.1234L', 'FLOAT')
    match('1234.l', 'FLOAT')
    match('.1234l', 'FLOAT')
    match('1234.1234l', 'FLOAT')


def test_hexa():
    match('0x123ABCD', 'HEXA')
    match('0X123ABCD', 'HEXA')
    match('0x123ABCDl', 'HEXA')
    match('0x123ABCDL', 'HEXA')


def test_grouped():
    match('100_000', 'INT')
    match('10_000_000.', 'FLOAT')
    match('10_000_000.0', 'FLOAT')
    match('0xCAFE_F00D', 'HEXA')
    match('0o123_45', 'OCTA')
    match('0b_0011_1111_0100_1110', 'BINARY')


def test_octa():
    match('012345', 'OCTA')
    match('0o12345', 'OCTA')
    match('0O1235', 'OCTA')
    match('0O1235l', 'OCTA')
    match('0O1235L', 'OCTA')


def test_float_exponant():
    match('1234e10', 'FLOAT_EXPONANT')
    match('1234E10', 'FLOAT_EXPONANT')
    match('1234e+10', 'FLOAT_EXPONANT')
    match('1234e-10', 'FLOAT_EXPONANT')
    match('1234E+10', 'FLOAT_EXPONANT')
    match('1234E-10', 'FLOAT_EXPONANT')
    match('1234.5678e10', 'FLOAT_EXPONANT')
    match('1234.5678E10', 'FLOAT_EXPONANT')
    match('1234.5678e+10', 'FLOAT_EXPONANT')
    match('1234.5678e-10', 'FLOAT_EXPONANT')
    match('1234.5678E+10', 'FLOAT_EXPONANT')
    match('1234.5678E-10', 'FLOAT_EXPONANT')
    match('.5678e10', 'FLOAT_EXPONANT')
    match('.5678E10', 'FLOAT_EXPONANT')
    match('.5678e+10', 'FLOAT_EXPONANT')
    match('.5678e-10', 'FLOAT_EXPONANT')
    match('.5678E+10', 'FLOAT_EXPONANT')
    match('.5678E-10', 'FLOAT_EXPONANT')


def test_floating_point_parser_bug_85():
    from baron import parse
    assert parse('d*e-1') == [
        {'first': {'first': {'type': 'name', 'value': 'd'},
                   'first_formatting': [],
                   'second': {'type': 'name', 'value': 'e'},
                   'second_formatting': [],
                   'type': 'binary_operator',
                   'value': '*'},
         'first_formatting': [],
         'second': {'section': 'number', 'type': 'int', 'value': '1'},
         'second_formatting': [],
         'type': 'binary_operator',
         'value': '-'}]


def test_left_parenthesis():
    match('(', 'LEFT_PARENTHESIS')


def test_right_parenthesis():
    match(')', 'RIGHT_PARENTHESIS')


def test_colon():
    match(':', 'COLON')
    assert tokenize([':']) == [('COLON', ':'), ('ENDMARKER', ''), None]


def test_comma():
    match(',', 'COMMA')


def test_semicolon():
    match(';', 'SEMICOLON')


def test_sequence():
    assert tokenize(['a', '123']) == [('NAME', 'a'), ('INT', '123'), ('ENDMARKER', ''), None]


def test_plus():
    match('+', 'PLUS')


def test_minus():
    match('-', 'MINUS')


def test_start():
    match('*', 'STAR')


def test_slash():
    match('/', 'SLASH')


def test_vbar():
    match('|', 'VBAR')


def test_amper():
    match('&', 'AMPER')


def test_less():
    match('<', 'LESS')


def test_greater():
    match('>', 'GREATER')


def test_equal():
    match('=', 'EQUAL')


def test_dot():
    match('.', 'DOT')


def test_percent():
    match('%', 'PERCENT')


def test_left_square_bracket():
    match('[', 'LEFT_SQUARE_BRACKET')


def test_right_square_bracket():
    match(']', 'RIGHT_SQUARE_BRACKET')


def test_left_bracket():
    match('{', 'LEFT_BRACKET')


def test_right_bracket():
    match('}', 'RIGHT_BRACKET')


def test_back_quote():
    match('`', 'BACKQUOTE')


def test_equal_equal():
    match('==', 'EQUAL_EQUAL')


def test_not_equal():
    match('!=', 'NOT_EQUAL')
    match('<>', 'NOT_EQUAL')


def test_less_equal():
    match('<=', 'LESS_EQUAL')


def test_greater_equal():
    match('>=', 'GREATER_EQUAL')


def test_tilde():
    match('~', 'TILDE')


def test_circumflex():
    match('^', 'CIRCUMFLEX')


def test_left_shift():
    match('<<', 'LEFT_SHIFT')


def test_right_shift():
    match('>>', 'RIGHT_SHIFT')


def test_double_star():
    match('**', 'DOUBLE_STAR')


def test_plus_equal():
    match('+=', 'PLUS_EQUAL')


def test_minus_equal():
    match('-=', 'MINUS_EQUAL')


def test_star_equal():
    match('*=', 'STAR_EQUAL')


def test_slash_equal():
    match('/=', 'SLASH_EQUAL')


def test_percent_equal():
    match('%=', 'PERCENT_EQUAL')


def test_amper_equal():
    match('&=', 'AMPER_EQUAL')


def test_at_equal():
    match('@=', 'AT_EQUAL')


def test_vbar_equal():
    match('|=', 'VBAR_EQUAL')


def test_circumflex_equal():
    match('^=', 'CIRCUMFLEX_EQUAL')


def test_left_shift_equal():
    match('<<=', 'LEFT_SHIFT_EQUAL')


def test_right_shift_equal():
    match('>>=', 'RIGHT_SHIFT_EQUAL')


def test_double_star_equal():
    match('**=', 'DOUBLE_STAR_EQUAL')


def test_double_slash():
    match('//', 'DOUBLE_SLASH')


def test_double_slash_equal():
    match('//=', 'DOUBLE_SLASH_EQUAL')


def test_keywords():
    for keyword in KEYWORDS:
        assert tokenize([keyword]) == [(keyword.upper(), keyword), ('ENDMARKER', ''), None]


def test_endl():
    match('\n', 'ENDL')
    match('\r\n', 'ENDL')


def test_simple_string():
    match('"pouet pouet"', 'STRING')
    match("'pouet pouet'", "STRING")


def test_multi_string():
    match('"""pouet pouet"""', 'STRING')
    match("'''pouet pouet'''", "STRING")


def test_unicode_string():
    match('u"pouet pouet"', 'UNICODE_STRING')
    match("u'pouet pouet'", "UNICODE_STRING")
    match('u"""pouet pouet"""', 'UNICODE_STRING')
    match("u'''pouet pouet'''", "UNICODE_STRING")
    match('U"pouet pouet"', 'UNICODE_STRING')
    match("U'pouet pouet'", "UNICODE_STRING")
    match('U"""pouet pouet"""', 'UNICODE_STRING')
    match("U'''pouet pouet'''", "UNICODE_STRING")


def test_interpolated_string():
    match("f'He said his name is {name!r}.'", 'INTERPOLATED_STRING')
    match("f'The value is {value}.'", 'INTERPOLATED_STRING')
    match('F"He said his name is {name!r}."', 'INTERPOLATED_STRING')
    match('f"The value is {value}."', 'INTERPOLATED_STRING')
    match("F'{date} was on a {date:%A}'", 'INTERPOLATED_STRING')
    match("f'a={d[\"a\"]}'", 'INTERPOLATED_STRING')
    match("F'{(lambda x: x*2)(3)}'", 'INTERPOLATED_STRING')


def test_interpolated_raw_string():
    match("fr'He said his name is {name!r}.'", 'INTERPOLATED_RAW_STRING')
    match("fr'The value is {value}.'", 'INTERPOLATED_RAW_STRING')
    match('Fr"He said his name is {name!r}."', 'INTERPOLATED_RAW_STRING')
    match('fR"The value is {value}."', 'INTERPOLATED_RAW_STRING')
    match("FR'{date} was on a {date:%A}'", 'INTERPOLATED_RAW_STRING')
    match("fr'a={d[\"a\"]}'", 'INTERPOLATED_RAW_STRING')
    match("FR'{(lambda x: x*2)(3)}'", 'INTERPOLATED_RAW_STRING')
    match("FR'{(lambda x: x*2)(3)}'", 'INTERPOLATED_RAW_STRING')

    match("rf'He said his name is {name!r}.'", 'INTERPOLATED_RAW_STRING')
    match("rf'The value is {value}.'", 'INTERPOLATED_RAW_STRING')
    match('rF"He said his name is {name!r}."', 'INTERPOLATED_RAW_STRING')
    match('Rf"The value is {value}."', 'INTERPOLATED_RAW_STRING')
    match("RF'{date} was on a {date:%A}'", 'INTERPOLATED_RAW_STRING')
    match("rf'a={d[\"a\"]}'", 'INTERPOLATED_RAW_STRING')
    match("RF'{(lambda x: x*2)(3)}'", 'INTERPOLATED_RAW_STRING')
    match("RF'{(lambda x: x*2)(3)}'", 'INTERPOLATED_RAW_STRING')


def test_raw_string():
    match('r"pouet pouet"', 'RAW_STRING')
    match("r'pouet pouet'", "RAW_STRING")
    match('r"""pouet pouet"""', 'RAW_STRING')
    match("r'''pouet pouet'''", "RAW_STRING")
    match('R"pouet pouet"', 'RAW_STRING')
    match("R'pouet pouet'", "RAW_STRING")
    match('R"""pouet pouet"""', 'RAW_STRING')
    match("R'''pouet pouet'''", "RAW_STRING")


def test_binary_string():
    match('b"pouet pouet"', 'BINARY_STRING')
    match("b'pouet pouet'", "BINARY_STRING")
    match('b"""pouet pouet"""', 'BINARY_STRING')
    match("b'''pouet pouet'''", "BINARY_STRING")
    match('B"pouet pouet"', 'BINARY_STRING')
    match("B'pouet pouet'", "BINARY_STRING")
    match('B"""pouet pouet"""', 'BINARY_STRING')
    match("B'''pouet pouet'''", "BINARY_STRING")


def test_raw_unicode_string():
    match('ur"pouet pouet"', 'UNICODE_RAW_STRING')
    match("uR'pouet pouet'", "UNICODE_RAW_STRING")
    match('uR"""pouet pouet"""', 'UNICODE_RAW_STRING')
    match("ur'''pouet pouet'''", "UNICODE_RAW_STRING")
    match('Ur"pouet pouet"', 'UNICODE_RAW_STRING')
    match("UR'pouet pouet'", "UNICODE_RAW_STRING")
    match('UR"""pouet pouet"""', 'UNICODE_RAW_STRING')
    match("Ur'''pouet pouet'''", "UNICODE_RAW_STRING")


def test_raw_binary_string():
    match('br"pouet pouet"', 'BINARY_RAW_STRING')
    match("bR'pouet pouet'", "BINARY_RAW_STRING")
    match('bR"""pouet pouet"""', 'BINARY_RAW_STRING')
    match("br'''pouet pouet'''", "BINARY_RAW_STRING")
    match('Br"pouet pouet"', 'BINARY_RAW_STRING')
    match("BR'pouet pouet'", "BINARY_RAW_STRING")
    match('BR"""pouet pouet"""', 'BINARY_RAW_STRING')
    match("Br'''pouet pouet'''", "BINARY_RAW_STRING")


def test_big_string_with_endl():
    match('"""pouet\n \r\npouet"""', 'STRING')
    match('u"""pouet\n \r\npouet"""', 'UNICODE_STRING')
    match('r"""pouet\n \r\npouet"""', 'RAW_STRING')
    match('b"""pouet\n \r\npouet"""', 'BINARY_STRING')
    match('ur"""pouet\n \r\npouet"""', 'UNICODE_RAW_STRING')
    match('br"""pouet\n \r\npouet"""', 'BINARY_RAW_STRING')


def test_comment():
    match('# pouet pouet', 'COMMENT')


def test_space():
    match(' ', 'SPACE')
    match('	', 'SPACE')
    match('	 ', 'SPACE')
    match('	 \\\n ', 'SPACE')
    match('	 \\\r\n ', 'SPACE')


def test_arobase():
    match('@', 'AT')


def test_binary():
    match("0b01010101", "BINARY")


def test_zero():
    match("0", "INT")


def test_float_exponant_advanced():
    match("1E1", "FLOAT_EXPONANT")
    match("1E-2", "FLOAT_EXPONANT")
    match("1E+2", "FLOAT_EXPONANT")
    match("1.E1", "FLOAT_EXPONANT")
    match(".1E1", "FLOAT_EXPONANT")
    match("1e1", "FLOAT_EXPONANT")
    match("1e-2", "FLOAT_EXPONANT")
    match("1e+2", "FLOAT_EXPONANT")
    match("1.e1", "FLOAT_EXPONANT")
    match(".1e1", "FLOAT_EXPONANT")


def test_complex():
    match(".1j", "COMPLEX")
    match("1.j", "COMPLEX")
    match("1.1j", "COMPLEX")
    match("11j", "COMPLEX")
    match(".1J", "COMPLEX")
    match("1.J", "COMPLEX")
    match("1.1J", "COMPLEX")
    match("11J", "COMPLEX")


def test_float_advanced():
    match("1.", "FLOAT")
    match(".1", "FLOAT")
    match("1.1", "FLOAT")


def test_exponant_complex():
    match("1e1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.e1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e1j", "FLOAT_EXPONANT_COMPLEX")
    match(".1e1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e1j", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e1j", "FLOAT_EXPONANT_COMPLEX")
    match("1e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e-1j", "FLOAT_EXPONANT_COMPLEX")
    match(".1e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e-1j", "FLOAT_EXPONANT_COMPLEX")
    match("1e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e+1j", "FLOAT_EXPONANT_COMPLEX")
    match(".1e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e+1j", "FLOAT_EXPONANT_COMPLEX")
    match("1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e1J", "FLOAT_EXPONANT_COMPLEX")
    match("1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1e+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1E1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.E1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1E1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1E1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.E1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1E1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1E1J", "FLOAT_EXPONANT_COMPLEX")
    match("1E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1E-1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1E-1J", "FLOAT_EXPONANT_COMPLEX")
    match("1E+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.E+1J", "FLOAT_EXPONANT_COMPLEX")
    match("1.1E+1J", "FLOAT_EXPONANT_COMPLEX")
    match(".1E+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.E+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-1.1E+1J", "FLOAT_EXPONANT_COMPLEX")
    match("-.1E+1J", "FLOAT_EXPONANT_COMPLEX")

# TODO 1.1e1j


def test_backslash():
    match("\\\n", "SPACE")


def test_ellipsis():
    match("...", "ELLIPSIS")


def test_right_arrow():
    match("->", "RIGHT_ARROW")
