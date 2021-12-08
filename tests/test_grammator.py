#!/usr/bin/python
# -*- coding:Utf-8 -*-
import pytest
from baron.parser import ParsingError
from .test_utils import parse_simple, parse_multi


def test_empty():
    ""
    parse_simple([], [])


def test_int():
    "1"
    parse_simple([('INT', '1')], [
        {
            "type": "int",
            "section": "number",
            "value": "1",
        }
    ])


def test_long():
    "123234L"
    parse_simple([('LONG', '123234L')], [
        {
            "type": "long",
            "section": "number",
            "value": "123234L",
        }
    ])


def test_name():
    "a"
    parse_simple([('NAME', 'a')], [{"type": "name", "value": "a", }])


def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    parse_simple([('STRING', '"pouet pouet"')], [
        {
            "type": "string",
            "value": '"pouet pouet"',
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([('STRING', '"""pouet pouet"""')], [
        {
            "type": "string",
            "value": '"""pouet pouet"""',
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_file_input_empty():
    ""
    parse_multi([], [])


def test_file_input_one_item():
    "a"
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_two_items():
    """
    a
    a
    """
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_two_items_endl():
    """
    a

    a
    """
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
    ])
    parse_multi([
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('ENDL', '\n'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_simple_stmt_one_item_semicolon():
    """
    a;
    """
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {
            "type": "semicolon",
            "value": ";",
            "first_formatting": [],
            "second_formatting": [],
        },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_simple_stmt_two_items_semicolon():
    """
    a;a
    """
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {
            "type": "semicolon",
            "value": ";",
            "first_formatting": [],
            "second_formatting": [],
        },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {
            "type": "semicolon",
            "value": ";",
            "first_formatting": [],
            "second_formatting": [],
        },
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_simple_stmt_three_items_semicolon():
    """
    a;b;a
    """
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b', },
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b', },
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a'},
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';'),
        ('NAME', 'b'),
        ('SEMICOLON', ';'),
        ('NAME', 'a'),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": []},
        {"type": "name", "value": 'b'},
        {"type": "semicolon", "value": ";", "first_formatting": [], "second_formatting": [], },
        {"type": "name", "value": 'a', },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_file_input_simple_stmt_one_item_semicolon_space():
    """
    a ;
    """
    parse_multi([
        ('NAME', 'a'),
        ('SEMICOLON', ';', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('ENDL', '\n'),
    ], [
        {"type": "name", "value": 'a', },
        {"type": "semicolon", "value": ";", "first_formatting": [{"type": "space", "value": ' '}], "second_formatting": [{"type": "space", "value": ' '}], },
        {"type": "endl", "value": "\n", "formatting": [], "indent": "", },
    ])


def test_ellipsis():
    "..."
    parse_simple([('ELLIPSIS', '...')], [
        {
            "type": "ellipsis",
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_funcdef_stmt_indent():
    """
    def a () :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_indent_return_annotation():
    """
    def a () -> b :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
        ('RIGHT_ARROW', '->', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "return_annotation": {"type": "name", "value": "b"},
            "return_annotation_first_formatting": [{"type": "space", "value": " "}],
            "return_annotation_second_formatting": [{"type": "space", "value": " "}],
            "async_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_async():
    """
    async def a():
        pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_async_bad_keyword():
    """
    async def a():
        pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('DEF', 'def', [], [('SPACE', ' ')]),
            ('NAME', 'a'),
            ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')]),
            ('RIGHT_PARENTHESIS', ')'),
            ('COLON', ':', [], [('SPACE', ' ')]),
            ('ENDL', '\n', [], [('SPACE', '    ')]),
            ('INDENT', ''),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
            ('DEDENT', ''),
        ], [])


def test_funcdef_stmt_one_parameter_indent():
    """
    def a ( x ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {},
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_parameter_typed_indent():
    """
    def a ( x : int ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'int'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "first_formatting": [],
                    "second_formatting": [],
                    "annotation": {"type": "name", "value": "int"},
                    "annotation_first_formatting": [{"type": "space", "value": " "}],
                    "annotation_second_formatting": [{"type": "space", "value": " "}],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {},
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_parameter_typed_indent_no_format():
    """
    def a ( x:int ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('COLON', ':', [], []),
        ('NAME', 'int'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {"type": "name", "value": "int"},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {},
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_star_parameter_typed_indent_no_format():
    """
    def a ( *x:int ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('STAR', 'x'),
        ('NAME', 'x'),
        ('COLON', ':', [], []),
        ('NAME', 'int'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "list_argument",
                    "annotation": {"type": "name", "value": "int"},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "formatting": [],
                    "value": {
                        "type": "name",
                        "value": "x",
                    },
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_double_star_parameter_typed_indent_no_format():
    """
    def a ( **x:int ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'x'),
        ('COLON', ':', [], []),
        ('NAME', 'int'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "dict_argument",
                    "annotation": {"type": "name", "value": "int"},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "formatting": [],
                    "value": {
                        "type": "name",
                        "value": "x",
                    },
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_parameter_comma_indent():
    """
    def a ( x , ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "name": "a",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {},
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_parameter_comma_default_indent():
    """
    def a ( x=1 , ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('EQUAL', '='),
        ('INT', '1'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "name": "a",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {
                        "type": "int",
                        "value": "1",
                        "section": "number",
                    },
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_two_parameters_typed_with_default_indent():
    """
    def a ( x : int = 1 , y : List[str] ) :
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'int'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('INT', '1'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'y'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'List'),
        ('LEFT_SQUARE_BRACKET', '[', [], []),
        ('NAME', 'str'),
        ('RIGHT_SQUARE_BRACKET', '[', [], []),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {"type": "name", "value": "int"},
                    "annotation_first_formatting": [{"type": "space", "value": " "}],
                    "annotation_second_formatting": [{"type": "space", "value": " "}],
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "target": {
                        "type": "name",
                        "value": "x",
                    },
                    "value": {"section": "number", "type": "int", "value": "1"},
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "def_argument",
                    "annotation": {
                        "type": "atomtrailers",
                        "value": [
                            {
                                "type": "name",
                                "value": "List",
                            },
                            {
                                "type": "getitem",
                                "first_formatting": [],
                                "second_formatting": [],
                                "third_formatting": [],
                                "fourth_formatting": [],
                                "value": {"type": "name", "value": "str"},
                            }
                        ]
                    },
                    "annotation_first_formatting": [{"type": "space", "value": " "}],
                    "annotation_second_formatting": [{"type": "space", "value": " "}],
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "name",
                        "value": "y",
                    },
                    "value": {},
                },
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "type": "endl",
                    "formatting": [],
                    "indent": "",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_empty():
    """
    class A:
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": False,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "sixth_formatting": [],
            "inherit_from": [],
            "value": [
                {
                    "type": "endl",
                    "formatting": [],
                    "value": "\n",
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_empty_parenthesis():
    """
    class A ( ) :
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', [], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [],
            "value": [
                {
                    "type": "endl",
                    "formatting": [],
                    "value": "\n",
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_inherit():
    """
    class A ( B ) :
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'B'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [
                {
                    "type": "name",
                    "value": "B"
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_inherit_metaclass():
    """
    class A ( B = C ) :
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'B'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'C'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [
                {
                    "first_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "target": {
                        "type": "name",
                        "value": "B"
                    },
                    "type": "call_argument",
                    "value": {
                        "type": "name",
                        "value": "C"
                    }
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_inherit_metaclass_arglist():
    """
    class A ( B, C = D ) :
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'B'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'C'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'D'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [
                {
                    "type": "name",
                    "value": "B"
                },
                {
                    "first_formatting": [],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "comma"
                },
                {
                    "first_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "target": {
                        "type": "name",
                        "value": "C"
                    },
                    "type": "call_argument",
                    "value": {
                        "type": "name",
                        "value": "D"
                    }
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_class_inherit_metaclass_arglist_more():
    """
    class A ( B, E, F, C = D ) :
        pass
    """
    parse_multi([
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'A'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'B'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'E'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'F'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'C'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'D'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
    ], [
        {
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [
                {
                    "type": "name",
                    "value": "B"
                },
                {
                    "first_formatting": [],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "comma"
                },
                {
                    "type": "name",
                    "value": "E"
                },
                {
                    "first_formatting": [],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "comma"
                },
                {
                    "type": "name",
                    "value": "F"
                },
                {
                    "first_formatting": [],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "comma"
                },
                {
                    "first_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "target": {
                        "type": "name",
                        "value": "C"
                    },
                    "type": "call_argument",
                    "value": {
                        "type": "name",
                        "value": "D"
                    }
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_start_parameter_indent():
    """
    def a (*b):
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('STAR', '*'),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [
                {
                    "type": "list_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "formatting": [],
                    "value": {
                        "value": "b",
                        "type": "name",
                    }
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "value": "\n",
                    "formatting": [],
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_funcdef_stmt_one_star_star_parameter_indent():
    """
    def a (**b):
        pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "def",
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [
                {
                    "type": "dict_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "formatting": [],
                    "value": {
                        "value": "b",
                        "type": "name",
                    }
                }
            ],
            "value": [
                {
                    "type": "endl",
                    "formatting": [],
                    "value": "\n",
                    "indent": "    "
                },
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_comment():
    """
      # comment
    """
    parse_multi([
        ('COMMENT', '# comment', [('SPACE', '  ')]),
        ('ENDL', '\n'),
    ], [
        {
            "formatting": [{"type": "space", "value": "  "}],
            "type": "comment",
            "value": "# comment",
        },
        {
            "formatting": [],
            "indent": "",
            "type": "endl",
            "value": "\n",
        }
    ])


def test_comment_consistant():
    """
      # comment
    """
    parse_multi([
        ('COMMENT', '# comment'),
        ('ENDL', '\n'),
    ], [
        {
            "formatting": [],
            "type": "comment",
            "value": "# comment",
        },
        {
            "formatting": [],
            "indent": "",
            "type": "endl",
            "value": "\n",
        }
    ])


def test_with_a():
    """
    with a: pass
    """
    parse_multi([
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": False,
            "async_formatting": [],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                    "as": {},
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_with_a_as_b():
    """
    with a as b: pass
    """
    parse_multi([
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": False,
            "async_formatting": [],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "as": {
                        "type": "name",
                        "value": "b",
                    },
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_with_a_as_b_c():
    """
    with a as b, c: pass
    """
    parse_multi([
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": False,
            "async_formatting": [],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "as": {
                        "type": "name",
                        "value": "b",
                    },
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "c",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                    "as": {},
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_async_with_a():
    """
    async with a: pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                    "as": {},
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_async_with_a_as_b():
    """
    async with a as b: pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "as": {
                        "type": "name",
                        "value": "b",
                    },
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_async_with_a_as_b_c():
    """
    async with a as b, c: pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('WITH', 'with', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "contexts": [
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "a",
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "as": {
                        "type": "name",
                        "value": "b",
                    },
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "with_context_item",
                    "value": {
                        "type": "name",
                        "value": "c",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                    "as": {},
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_async_with_a_bad_keyword():
    """
    async with a: pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('WITH', 'with', [], [('SPACE', ' ')]),
            ('NAME', 'a'),
            ('COLON', ':', [], [('SPACE', ' ')]),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
        ], [])


def test_async_with_a_as_b_bad_keyword():
    """
    async with a as b: pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('WITH', 'with', [], [('SPACE', ' ')]),
            ('NAME', 'a'),
            ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
            ('COLON', ':', [], [('SPACE', ' ')]),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
        ], [])


def test_async_with_a_as_b_c_bad_keyword():
    """
    async with a as b, c: pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('WITH', 'with', [], [('SPACE', ' ')]),
            ('NAME', 'a'),
            ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
            ('COMMA', ',', [], [('SPACE', ' ')]),
            ('NAME', 'c'),
            ('COLON', ':', [], [('SPACE', ' ')]),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
        ], [])


def test_decorator():
    """
    @a
    def b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [],
            "name": "b",
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "decorators": [
                {
                    "type": "decorator",
                    "formatting": [],
                    "call": {},
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_decorator_parenthesis():
    """
    @a()
    def b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('ENDL', '\n'),
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [],
            "name": "b",
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "decorators": [
                {
                    "type": "decorator",
                    "formatting": [],
                    "call": {
                        "third_formatting": [],
                        "type": "call",
                        "first_formatting": [],
                        "value": [],
                        "second_formatting": [],
                        "fourth_formatting": [],
                    },
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_decorator_parenthesis_arg():
    """
    @a(c)
    def b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
        ('ENDL', '\n'),
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [],
            "name": "b",
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "decorators": [
                {
                    "type": "decorator",
                    "formatting": [],
                    "call": {
                        "third_formatting": [],
                        "type": "call",
                        "fourth_formatting": [],
                        "first_formatting": [],
                        "value": [
                            {
                                "target": {},
                                "first_formatting": [],
                                "second_formatting": [],
                                "type": "call_argument",
                                "value": {
                                    "type": "name",
                                    "value": "c",
                                },
                            }
                        ],
                        "second_formatting": [],
                    },
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_decorator_two():
    """
    @a
    @ c
    def b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('AT', '@', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('ENDL', '\n'),
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [],
            "name": "b",
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "decorators": [
                {
                    "type": "decorator",
                    "formatting": [],
                    "call": {},
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                },
                {
                    "type": "decorator",
                    "formatting": [{"type": "space", "value": " "}],
                    "call": {},
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "c",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_class_decorator():
    """
    @a
    class b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [
                {
                    "type": "decorator",
                    "call": {},
                    "formatting": [],
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_class_decorator_two():
    """
    @a
    @ c
    class b(): pass
    """
    parse_multi([
        ('AT', '@', [], []),
        ('NAME', 'a'),
        ('ENDL', '\n'),
        ('AT', '@', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('ENDL', '\n'),
        ('CLASS', 'class', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [
                {
                    "type": "decorator",
                    "call": {},
                    "formatting": [],
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "a",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                },
                {
                    "type": "decorator",
                    "call": {},
                    "formatting": [{"type": "space", "value": " "}],
                    "value": {
                        "type": "dotted_name",
                        "value": [
                            {
                                "type": "name",
                                "value": "c",
                            }
                        ],
                    }
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_fplist():
    """
    def a((b,)): pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('RIGHT_PARENTHESIS', ')'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "value": {},
                    "target": {
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "type": "tuple",
                        "with_parenthesis": True,
                        "value": [
                            {
                                "value": "b",
                                "type": "name",
                            },
                            {
                                "first_formatting": [],
                                "second_formatting": [],
                                "type": "comma",
                            }
                        ],
                    },
                }
            ],
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_fplist_two():
    """
    def a((b,c)): pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "first_formatting": [],
                    "second_formatting": [],
                    "value": {},
                    "target": {
                        "type": "tuple",
                        "with_parenthesis": True,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "value": [
                            {
                                "type": "name",
                                "value": "b",
                            },
                            {
                                "type": "comma",
                                "first_formatting": [],
                                "second_formatting": [],
                            },
                            {
                                "type": "name",
                                "value": "c",
                            }
                        ],
                    }
                }
            ],
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_fplist_alone():
    """
    def a((b)): pass
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fifth_formatting": [],
            "fourth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "def",
            "arguments": [
                {
                    "type": "def_argument",
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "value": {},
                    "first_formatting": [],
                    "second_formatting": [],
                    "target": {
                        "type": "associative_parenthesis",
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "value": {
                            "type": "name",
                            "value": "b",
                        }
                    }
                }
            ],
            "name": "a",
            "decorators": [],
            "async": False,
            "async_formatting": [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            "value": [
                {
                    "type": "pass",
                },
                {
                    "formatting": [],
                    "indent": "",
                    "type": "endl",
                    "value": "\n",
                }
            ],
        }
    ])


def test_endl_dont_grab_comment_as_indent():
    """
    \n# pouet
    """
    parse_multi([
        ('ENDL', '\n', [], [('COMMENT', '# pouet')])
    ], [
        {"type": "endl", "value": "\n", "indent": "", "formatting": []},
        {"type": "comment", "value": "# pouet", "formatting": []},
    ])


def test_regression_def_argument_tuple():
    """
    def function_name((a,b)=c):\n    pass\n
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'function_name'),
        ('LEFT_PARENTHESIS', '('),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')'),
        ('EQUAL', '='),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n', [], []),
        ('DEDENT', ''),
        ('ENDMARKER', '')
    ], [
        {
            'arguments': [
                {
                    'first_formatting': [],
                    'second_formatting': [],
                    'type': 'def_argument',
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    'target': {
                        'type': 'tuple',
                        'first_formatting': [],
                        'with_parenthesis': True,
                        'fourth_formatting': [],
                        'second_formatting': [],
                        'third_formatting': [],
                        'value': [
                            {
                                'value': 'a',
                                'type': 'name',
                            },
                            {
                                'first_formatting': [],
                                'second_formatting': [],
                                'type': 'comma'
                            },
                            {
                                'value': 'b',
                                'type': 'name',
                            }
                        ]
                    },
                    'value': {
                        'type': 'name',
                        'value': 'c',
                    }
                }
            ],
            'decorators': [],
            'async': False,
            'async_formatting': [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            'fifth_formatting': [],
            'first_formatting': [
                {
                    'type': 'space',
                    'value': ' '
                }
            ],
            'fourth_formatting': [],
            'name': 'function_name',
            'second_formatting': [],
            'sixth_formatting': [],
            'third_formatting': [],
            'type': 'def',
            'value': [
                {
                    'formatting': [],
                    'indent': '    ',
                    'type': 'endl',
                    'value': '\n'
                },
                {
                    'type': 'pass'
                },
                {
                    'formatting': [],
                    'indent': '',
                    'type': 'endl',
                    'value': '\n'
                }
            ]
        }
    ])


def test_regression_def_argument_tuple_nested():
    """
    def function_name((a,(x,y))=c):\n    pass\n
    """
    parse_multi([
        ('DEF', 'def', [], [('SPACE', ' ')]),
        ('NAME', 'function_name'),
        ('LEFT_PARENTHESIS', '('),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'x'),
        ('COMMA', ','),
        ('NAME', 'y'),
        ('RIGHT_PARENTHESIS', ')'),
        ('RIGHT_PARENTHESIS', ')'),
        ('EQUAL', '='),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ENDMARKER', ''),
    ], [
        {
            'arguments': [
                {
                    'first_formatting': [],
                    'second_formatting': [],
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    'type': 'def_argument',
                    'target': {
                        'type': 'tuple',
                        'first_formatting': [],
                        'with_parenthesis': True,
                        'fourth_formatting': [],
                        'second_formatting': [],
                        'third_formatting': [],
                        'value': [
                            {
                                'value': 'a',
                                'type': 'name',
                            },
                            {
                                'first_formatting': [],
                                'second_formatting': [],
                                'type': 'comma'
                            },
                            {
                                'type': 'tuple',
                                'first_formatting': [],
                                'with_parenthesis': True,
                                'fourth_formatting': [],
                                'second_formatting': [],
                                'third_formatting': [],
                                'value': [
                                    {
                                        'value': 'x',
                                        'type': 'name',
                                    },
                                    {
                                        'first_formatting': [],
                                        'second_formatting': [],
                                        'type': 'comma'
                                    },
                                    {
                                        'value': 'y',
                                        'type': 'name',
                                    },
                                ]
                            },
                        ]
                    },
                    'value': {
                        'type': 'name',
                        'value': 'c',
                    }
                }
            ],
            'decorators': [],
            'async': False,
            'async_formatting': [],
            "return_annotation": {},
            "return_annotation_first_formatting": [],
            "return_annotation_second_formatting": [],
            'fifth_formatting': [],
            'first_formatting': [
                {
                    'type': 'space',
                    'value': ' '
                }
            ],
            'fourth_formatting': [],
            'name': 'function_name',
            'second_formatting': [],
            'sixth_formatting': [],
            'third_formatting': [],
            'type': 'def',
            'value': [
                {
                    'formatting': [],
                    'indent': '    ',
                    'type': 'endl',
                    'value': '\n'
                },
                {
                    'type': 'pass'
                },
                {
                    'formatting': [],
                    'indent': '',
                    'type': 'endl',
                    'value': '\n'
                }
            ]
        }
    ])


def test_standalone_annotation():
    """
    x :  int
    """
    parse_simple([
        ('NAME', 'x'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'int'),
    ], [
        {
            "type": "standalone_annotation",
            "annotation": {"type": "name", "value": "int"},
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}],
            "target": {"type": "name", "value": "x"},
        }
    ])


def test_typed_variable_with_assignment():
    """
    x : int = 1
    """
    parse_simple([
        ('NAME', 'x'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'int'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('INT', '1'),
    ], [
        {
            "type": "assignment",
            "annotation": {"type": "name", "value": "int"},
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "annotation_first_formatting": [{"type": "space", "value": " "}],
            "annotation_second_formatting": [{"type": "space", "value": " "}],
            "target": {"type": "name", "value": "x"},
            "operator": "",
            "value": {"section": "number", "type": "int", "value": "1"}
        }
    ])
