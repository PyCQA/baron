# encoding: utf-8

from .test_utils import parse_simple


def test_empty_tuple():
    "()"
    parse_simple([
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "with_parenthesis": True,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "type": "tuple",
            "value": [],
        }
    ])


def test_empty_tuple_space():
    "(  )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', '  ')]),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "with_parenthesis": True,
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "type": "tuple",
            "value": [],
        }
    ])


def test_associative_parenthesis():
    "( a )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "associative_parenthesis",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "value": {
                "type": "name",
                "value": "a",
            },
        }
    ])


def test_tuple_one():
    "( a, )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', [], []),
    ], [
        {
            "with_parenthesis": True,
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "type": "tuple",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                }
            ],
        }
    ])


def test_tuple_many():
    "(a, b, c)"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], []),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')', [], []),
    ], [
        {
            "with_parenthesis": True,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "type": "tuple",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "c",
                }
            ],
        }
    ])


def test_empty_list():
    "[ ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('RIGHT_SQUARE_BRACKET', ']', [], []),
    ], [
        {
            "type": "list",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [],
        }
    ])


def test_list_one():
    "[ a ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                }
            ],
        }
    ])


def test_list_more():
    "[a, b, c]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], []),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']', [], []),
    ], [
        {
            "type": "list",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "c",
                }
            ],
        }
    ])


def test_dict_empty():
    "{ }"
    parse_simple([
        ('LEFT_BRACKET', '{', [], [('SPACE', ' ')]),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "dict",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [],
        }
    ])


def test_dict_one_colon():
    "{a: b}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "dict",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "dictitem",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "key": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": {
                        "type": "name",
                        "value": "b",
                    }
                }
            ],
        }
    ])


def test_dict_one_double_star():
    "{**a}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'a'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            'type': 'dict',
            'first_formatting': [],
            'second_formatting': [],
            'third_formatting': [],
            'fourth_formatting': [],
            'value': [
                {
                    'type': 'dict_argument',
                    'annotation': {},
                    'annotation_first_formatting': [],
                    'annotation_second_formatting': [],
                    'formatting': [],
                    'value': {'type': 'name', 'value': 'a'}
                }
            ]
        }
    ]
)


def test_dict_more_colon():
    "{a: b, b: c, c: d}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "dict",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "dictitem",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "key": {
                        "type": "name",
                        "value": "a",
                    },
                    "value": {
                        "type": "name",
                        "value": "b",
                    }
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "dictitem",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "key": {
                        "type": "name",
                        "value": "b",
                    },
                    "value": {
                        "type": "name",
                        "value": "c",
                    }
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "dictitem",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "key": {
                        "type": "name",
                        "value": "c",
                    },
                    "value": {
                        "type": "name",
                        "value": "d",
                    }
                }
            ],
        }
    ])


def test_dict_more_double_star():
    "{**a, b: c}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "first_formatting": [],
            "fourth_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "type": "dict",
            "value": [
                {
                    "annotation": {},
                    "annotation_first_formatting": [],
                    "annotation_second_formatting": [],
                    "formatting": [],
                    "type": "dict_argument",
                    "value": {
                        "type": "name",
                        "value": "a"
                    }
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
                    "first_formatting": [],
                    "key": {
                        "type": "name",
                        "value": "b"
                    },
                    "second_formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "dictitem",
                    "value": {
                        "type": "name",
                        "value": "c"
                    }
                }
            ]
        }
    ])


def test_set_one():
    "{a}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('NAME', 'a'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "set",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                }
            ],
        }
    ])


def test_set_one_comma():
    "{a,}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "set",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [],
                }
            ],
        }
    ])


def test_set_more():
    "{a, b, c}"
    parse_simple([
        ('LEFT_BRACKET', '{', [], []),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_BRACKET', '}', [], []),
    ], [
        {
            "type": "set",
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "c",
                }
            ],
        }
    ])


def test_generator_comprehension():
    "( a for b in c )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "generator_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_generator_comprehension_if():
    "( a for b in c if d )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "generator_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_generator_comprehension_if_if():
    "( a for b in c if d if e )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "generator_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        },
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "e"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_generator_comprehension_double():
    "( a for b in c for d in e )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "generator_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [],
                },
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "d",
                    },
                    "target": {
                        "type": "name",
                        "value": "e",
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_generator_comprehension_double_if_if():
    "( a for b in c if x for d in e if y )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'y'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "generator_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "x"
                            },
                        }
                    ],
                },
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "d",
                    },
                    "target": {
                        "type": "name",
                        "value": "e",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "y"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_list_comprehension():
    "[ a for b in c ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_list_comprehension_if():
    "[ a for b in c if d ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_list_comprehension_if_if():
    "[ a for b in c if d if d ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        },
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_list_comprehension_tuple():
    "[ a for b in c, d ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "tuple",
                        "with_parenthesis": False,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "value": [
                            {
                                "type": "name",
                                "value": "c",
                            },
                            {
                                "type": "comma",
                                "first_formatting": [],
                                "second_formatting": [{"type": "space", "value": " "}],
                            },
                            {
                                "type": "name",
                                "value": "d",
                            }
                        ],
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_list_comprehension_tuple_more():
    "[ a for b in c, d, e ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "tuple",
                        "with_parenthesis": False,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "value": [
                            {
                                "type": "name",
                                "value": "c",
                            },
                            {
                                "type": "comma",
                                "first_formatting": [],
                                "second_formatting": [{"type": "space", "value": " "}],
                            },
                            {
                                "type": "name",
                                "value": "d",
                            },
                            {
                                "type": "comma",
                                "first_formatting": [],
                                "second_formatting": [{"type": "space", "value": " "}],
                            },
                            {
                                "type": "name",
                                "value": "e",
                            }
                        ],
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_list_comprehension_lambda():
    "[ a for b in lambda: c ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('LAMBDA', 'lambda', [], []),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "lambda",
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [{"type": "space", "value": " "}],
                        "arguments": [],
                        "value": {
                            "type": "name",
                            "value": "c",
                        }
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_list_comprehension_lambda_with_arguments():
    "[ a for b in lambda argument: c ]"
    parse_simple([
        ('LEFT_SQUARE_BRACKET', '[', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('LAMBDA', 'lambda', [], [('SPACE', ' ')]),
        ('NAME', 'argument'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "list_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "lambda",
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [],
                        "third_formatting": [{"type": "space", "value": " "}],
                        "arguments": [
                            {
                                "value": {},
                                "first_formatting": [],
                                "second_formatting": [],
                                "annotation": {},
                                "annotation_first_formatting": [],
                                "annotation_second_formatting": [],
                                "type": "def_argument",
                                "target": {
                                    "type": "name",
                                    "value": "argument",
                                }
                            }
                        ],
                        "value": {
                            "type": "name",
                            "value": "c",
                        }
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_set_comprehension():
    "{ a for b in c }"
    parse_simple([
        ('LEFT_BRACKET', '{', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_BRACKET', '}', [('SPACE', ' ')]),
    ], [
        {
            "type": "set_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_set_comprehension_if():
    "{ a for b in c if d }"
    parse_simple([
        ('LEFT_BRACKET', '{', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_BRACKET', '}', [('SPACE', ' ')]),
    ], [
        {
            "type": "set_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "d"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_set_comprehension_double_if_if():
    "{ a for b in c if x for d in e if y }"
    parse_simple([
        ('LEFT_BRACKET', '{', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'e'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'y'),
        ('RIGHT_BRACKET', '}', [('SPACE', ' ')]),
    ], [
        {
            "type": "set_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "type": "name",
                "value": "a",
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "x"
                            },
                        }
                    ],
                },
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "d",
                    },
                    "target": {
                        "type": "name",
                        "value": "e",
                    },
                    "ifs": [
                        {
                            "type": "comprehension_if",
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "value": {
                                "type": "name",
                                "value": "y"
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_dict_comprehension():
    "{ a: x for b in c }"
    parse_simple([
        ('LEFT_BRACKET', '{', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'x'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_BRACKET', '}', [('SPACE', ' ')]),
    ], [
        {
            "type": "dict_comprehension",
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [],
            "result": {
                "key": {
                    "type": "name",
                    "value": "a",
                },
                "first_formatting": [],
                "type": "dictitem",
                "second_formatting": [{"type": "space", "value": " "}],
                "value": {
                    "type": "name",
                    "value": "x",
                },
            },
            "generators": [
                {
                    "type": "comprehension_loop",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "iterator": {
                        "type": "name",
                        "value": "b",
                    },
                    "target": {
                        "type": "name",
                        "value": "c",
                    },
                    "ifs": [],
                }
            ]
        }
    ])


def test_yield_atom_empty():
    "( yield )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('YIELD', 'yield', [], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', []),
    ], [
        {
            "type": "yield_atom",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "value": None,
        }
    ])


def test_yield_atom():
    "( yield a )"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('YIELD', 'yield', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ], [
        {
            "type": "yield_atom",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "value": {
                "type": "name",
                "value": "a",
            },
        }
    ])


def test_repr_quote():
    "` a `"
    parse_simple([
        ('BACKQUOTE', '`', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('BACKQUOTE', '`', [('SPACE', ' ')]),
    ], [
        {
            "type": "repr",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                }
            ],
        }
    ])


def test_repr_quote_double():
    "` a, b `"
    parse_simple([
        ('BACKQUOTE', '`', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('BACKQUOTE', '`', [('SPACE', ' ')]),
    ], [
        {
            "type": "repr",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "type": "comma",
                },
                {
                    "type": "name",
                    "value": "b",
                }
            ],
        }
    ])


def test_empty_tuple_endl():
    "(\n)"
    parse_simple([
        ('LEFT_PARENTHESIS', '(', [], [('ENDL', '\n')]),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "with_parenthesis": True,
            "first_formatting": [],
            "second_formatting": [
                {
                    "indent": "",
                    "formatting": [],
                    "type": "endl",
                    "value": "\n",
                }
            ],
            "third_formatting": [],
            "fourth_formatting": [],
            "type": "tuple",
            "value": [],
        }
    ])


def test_subscript_special_case():
    "z[a, b, c,]"
    parse_simple([
        ('NAME', 'z'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ','),
        ('RIGHT_SQUARE_BRACKET', ']')
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "z"
                },
                {
                    "first_formatting": [],
                    "type": "getitem",
                    "value": {
                        "first_formatting": [],
                        "with_parenthesis": False,
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "type": "tuple",
                        "value": [
                            {
                                "type": "name",
                                "value": "a"
                            },
                            {
                                "first_formatting": [],
                                "type": "comma",
                                "second_formatting": [
                                    {
                                        "type": "space",
                                        "value": " "
                                    }
                                ]
                            },
                            {
                                "type": "name",
                                "value": "b"
                            },
                            {
                                "first_formatting": [],
                                "type": "comma",
                                "second_formatting": [
                                    {
                                        "type": "space",
                                        "value": " "
                                    }
                                ]
                            },
                            {
                                "type": "name",
                                "value": "c"
                            },
                            {
                                "first_formatting": [],
                                "type": "comma",
                                "second_formatting": []
                            }
                        ],
                        "second_formatting": []
                    },
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": []
                }
            ]
        }
    ])
