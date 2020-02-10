#!/usr/bin/python
# -*- coding:Utf-8 -*-

import pytest
from baron.parser import ParsingError
from .test_utils import parse_multi


def test_if_stmt():
    "if a: pass"
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": [
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
            ],
        }
    ])


def test_if_stmt_indent():
    """
    if a:
        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": [
                        {
                            "formatting": [],
                            "type": "endl",
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
            ]
        }
    ])


def test_if_stmt_indent_two_endls():
    """
    if a:

        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": [
                        {
                            "type": "endl",
                            "value": "\n",
                            "formatting": [],
                            "indent": ""
                        },
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
            ]
        }
    ])


def test_if_stmt_indent_multiple_endls():
    """
    if a:


        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('ENDL', '\n', [], [('SPACE', '  ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": [
                        {
                            "type": "endl",
                            "formatting": [],
                            "value": "\n",
                            "indent": ""
                        },
                        {
                            "type": "endl",
                            "formatting": [],
                            "value": "\n",
                            "indent": "  "
                        },
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
            ]
        }
    ])


def test_if_else_stmt_indent():
    """
    if a:
        pass
    else:
        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else', [], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
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
                },
                {
                    "type": "else",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
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
                            "value": "\n",
                        }
                    ]
                }
            ]
        }
    ])


def test_if_elif_elif_stmt_indent():
    """
    if a:
        pass
    elif b:
        pass
    elif c :
        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELIF', 'elif', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELIF', 'elif', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
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
                },
                {
                    "type": "elif",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "b",
                    },
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
                },
                {
                    "type": "elif",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "c",
                    },
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
            ]
        }
    ])


def test_if_elif_elif_else_stmt_indent():
    """
    if a:
        pass
    elif b:
        pass
    elif c :
        pass
    else:
        pass
    """
    parse_multi([
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELIF', 'elif', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELIF', 'elif', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else', [], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "ifelseblock",
            "value": [
                {
                    "type": "if",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "a",
                    },
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
                },
                {
                    "type": "elif",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "b",
                    },
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
                            "value": "\n",
                            "formatting": [],
                            "indent": "",
                        }
                    ],
                },
                {
                    "type": "elif",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [],
                    "test": {
                        "type": "name",
                        "value": "c",
                    },
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
                },
                {
                    "type": "else",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "value": [
                        {
                            "formatting": [],
                            "type": "endl",
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
                            "value": "\n",
                        }
                    ]
                }
            ]
        }
    ])


def test_while_stmt_indent():
    """
    while a:
        pass
    """
    parse_multi([
        ('WHILE', 'while', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "while",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "else": {},
            "test": {
                "type": "name",
                "value": "a",
            },
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


def test_while_stmt_indent_third_formatting():
    """
    while a :
        pass
    """
    parse_multi([
        ('WHILE', 'while', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "while",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "else": {},
            "test": {
                "type": "name",
                "value": "a",
            },
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


def test_while_else_stmt_indent():
    """
    while a:
        pass
    else:
        pass
    """
    parse_multi([
        ('WHILE', 'while', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else', [], [('SPACE', " ")]),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "while",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "test": {
                "type": "name",
                "value": "a",
            },
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
            "else": {
                "type": "else",
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
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
                        "indent": "",
                        "formatting": [],
                        "type": "endl",
                        "value": "\n",
                    }
                ]
            }
        }
    ])


def test_for_stmt_indent():
    """
    for i in a:
        pass
    """
    parse_multi([
        ('FOR', 'for', [], [('SPACE', ' ')]),
        ('NAME', 'i'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "for",
            "async": False,
            "async_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "else": {},
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "a",
            },
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_async_for_stmt_indent():
    """
    async for i in a:
        pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('FOR', 'for', [], [('SPACE', ' ')]),
        ('NAME', 'i'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "for",
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "fifth_formatting": [{"type": "space", "value": " "}],
            "else": {},
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "a",
            },
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_async_for_stmt_indent_bad_keyword():
    """
    not_async for i in a:
        pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('FOR', 'for', [], [('SPACE', ' ')]),
            ('NAME', 'i'),
            ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'a'),
            ('COLON', ':', [], [('SPACE', ' ')]),
            ('ENDL', '\n', [], [('SPACE', '    ')]),
            ('INDENT', ''),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
            ('DEDENT', ''),
        ], [])


def test_for_else_stmt_indent():
    """
    for i in b:
        pass
    else:
        pass
    """
    parse_multi([
        ('FOR', 'for', [], [('SPACE', ' ')]),
        ('NAME', 'i'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "for",
            "async": False,
            "async_formatting": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "else": {
                "type": "else",
                "first_formatting": [],
                "second_formatting": [],
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
                        "indent": "",
                        "formatting": [],
                        "type": "endl",
                        "value": "\n",
                    }
                ]
            },
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "b",
            },
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_async_for_else_stmt_indent():
    """
    async for i in b:
        pass
    else:
        pass
    """
    parse_multi([
        ('NAME', 'async', [], []),
        ('SPACE', ' '),
        ('FOR', 'for', [], [('SPACE', ' ')]),
        ('NAME', 'i'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "for",
            "async": True,
            "async_formatting": [{"type": "space", "value": " "}],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "else": {
                "type": "else",
                "first_formatting": [],
                "second_formatting": [],
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
                        "indent": "",
                        "formatting": [],
                        "type": "endl",
                        "value": "\n",
                    }
                ]
            },
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "b",
            },
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_async_for_else_stmt_indent_bad_keyword():
    """
    async for i in b:
        pass
    else:
        pass
    """
    with pytest.raises(ParsingError):
        parse_multi([
            ('NAME', 'not_async', [], []),
            ('SPACE', ' '),
            ('FOR', 'for', [], [('SPACE', ' ')]),
            ('NAME', 'i'),
            ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
            ('COLON', ':'),
            ('ENDL', '\n', [], [('SPACE', '    ')]),
            ('INDENT', ''),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
            ('DEDENT', ''),
            ('ELSE', 'else'),
            ('COLON', ':'),
            ('ENDL', '\n', [], [('SPACE', '    ')]),
            ('INDENT', ''),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
            ('DEDENT', ''),
        ], [])


def test_try_finally_stmt_indent():
    """
    try :
        pass
    finally :
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('FINALLY', 'finally'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {
                "type": "finally",
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
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
                        "indent": "",
                        "formatting": [],
                        "type": "endl",
                        "value": "\n"
                    }
                ],
            },
            "excepts": [],
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_try_excepts_stmt_empty():
    """
    try :
        pass
    except:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], []),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {},
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": "",
                    "target": {},
                    "exception": {},
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
                            "indent": "",
                            "formatting": [],
                            "type": "endl",
                            "value": "\n"
                        }
                    ]
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_try_excepts_stmt_indent():
    """
    try :
        pass
    except IOError:
        pass
    except Exception:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'Exception'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {},
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": "",
                    "target": {},
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                            "indent": "",
                            "formatting": [],
                            "type": "endl",
                            "value": "\n"
                        }
                    ]
                },
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": "",
                    "target": {},
                    "exception": {
                        "type": "name",
                        "value": "Exception",
                    },
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
                            "indent": "",
                            "formatting": [],
                            "type": "endl",
                            "value": "\n"
                        }
                    ]
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
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n"
                }
            ],
        }
    ])


def test_try_except_comma_stmt_indent():
    """
    try :
        pass
    except IOError, e:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {},
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": ",",
                    "target": {
                        "type": "name",
                        "value": "a"
                    },
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                            "indent": "",
                            "formatting": [],
                            "type": "endl",
                            "value": "\n"
                        }
                    ]
                }
            ],
            "value": [
                {
                    "formatting": [],
                    "type": "endl",
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


def test_try_except_comma_stmt_else_indent():
    """
    try :
        pass
    except IOError, e:
        pass
    else:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {
                "type": "else",
                "first_formatting": [],
                "second_formatting": [],
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
                        "value": "\n",
                        "formatting": [],
                        "indent": ""
                    }
                ]
            },
            "finally": {},
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": ",",
                    "target": {
                        "type": "name",
                        "value": "a"
                    },
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                    ]
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


def test_try_except_comma_stmt_else_finally_indent():
    """
    try :
        pass
    except IOError, e:
        pass
    else:
        pass
    finally:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('ELSE', 'else'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('FINALLY', 'finally'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {
                "type": "else",
                "first_formatting": [],
                "second_formatting": [],
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
                        "value": "\n",
                        "formatting": [],
                        "indent": ""
                    }
                ]
            },
            "finally": {
                "type": "finally",
                "first_formatting": [],
                "second_formatting": [],
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
                        "value": "\n",
                        "formatting": [],
                        "indent": "",
                    }
                ],
            },
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": ",",
                    "target": {
                        "type": "name",
                        "value": "a"
                    },
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                    ]
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


def test_try_except_comma_stmt_finally_indent():
    """
    try :
        pass
    except IOError, e:
        pass
    finally:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('FINALLY', 'finally'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {
                "type": "finally",
                "first_formatting": [],
                "second_formatting": [],
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
            },
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": ",",
                    "target": {
                        "type": "name",
                        "value": "a"
                    },
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                    ]
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


def test_try_except_as_stmt_indent():
    """
    try :
        pass
    except IOError as e:
        pass
    """
    parse_multi([
        ('TRY', 'try'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
        ('EXCEPT', 'except', [], [('SPACE', ' ')]),
        ('NAME', 'IOError'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':'),
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('INDENT', ''),
        ('PASS', 'pass'),
        ('ENDL', '\n'),
        ('DEDENT', ''),
    ], [
        {
            "type": "try",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "else": {},
            "finally": {},
            "excepts": [
                {
                    "type": "except",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "fifth_formatting": [],
                    "delimiter": "as",
                    "target": {
                        "type": "name",
                        "value": "a"
                    },
                    "exception": {
                        "type": "name",
                        "value": "IOError",
                    },
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
                    ]
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
