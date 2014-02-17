# encoding: utf-8

from test_utils import parse_simple


def test_empty_tuple():
    "()"
    parse_simple([
           ('LEFT_PARENTHESIS', '('),
           ('RIGHT_PARENTHESIS', ')'),
          ],
          [{
            "type": "tuple",
            "first_space": "",
            "second_space": "",
            "value": [],
          }])

def test_empty_tuple_space():
    "(  )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', '  '),
           ('RIGHT_PARENTHESIS', ')'),
          ],
          [{
            "type": "tuple",
            "first_space": "  ",
            "second_space": "",
            "value": [],
          }])

def test_tuple_one():
    "( a, )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('RIGHT_PARENTHESIS', ')', '', ''),
          ],
          [{
            "type": "tuple",
            "first_space": " ",
            "second_space": "",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            }],
          }])

def test_tuple_many():
    "(a, b, c)"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ''),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('RIGHT_PARENTHESIS', ')', '', ''),
          ],
          [{
            "type": "tuple",
            "first_space": "",
            "second_space": "",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
               "type": "name",
               "value": "b",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
               "type": "name",
               "value": "c",
            }],
          }])

def test_empty_list():
    "[ ]"
    parse_simple([
           ('LEFT_SQUARE_BRACKET', '[', '', ' '),
           ('RIGHT_SQUARE_BRACKET', ']', '', ''),
          ],
          [{
            "type": "list",
            "first_space": " ",
            "second_space": "",
            "value": [],
          }])

def test_list_one():
    "[ a ]"
    parse_simple([
           ('LEFT_SQUARE_BRACKET', '[', '', ' '),
           ('NAME', 'a'),
           ('RIGHT_SQUARE_BRACKET', ']', ' ', ''),
          ],
          [{
            "type": "list",
            "first_space": " ",
            "second_space": " ",
            "value": [{
               "type": "name",
               "value": "a",
            }],
          }])

def test_list_more():
    "[a, b, c]"
    parse_simple([
           ('LEFT_SQUARE_BRACKET', '[', '', ''),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('RIGHT_SQUARE_BRACKET', ']', '', ''),
          ],
          [{
            "type": "list",
            "first_space": "",
            "second_space": "",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
               "type": "name",
               "value": "b",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
               "type": "name",
               "value": "c",
            }],
          }])

def test_dict_empty():
    "{ }"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ' '),
           ('RIGHT_BRACKET', '}', '', ''),
          ],
          [{
            "type": "dict",
            "first_space": " ",
            "second_space": "",
            "value": [],
          }])

def test_dict_one():
    "{a: b}"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ''),
           ('NAME', 'a'),
           ('COLON', ':', '', ' '),
           ('NAME', 'b'),
           ('RIGHT_BRACKET', '}', '', ''),
          ],
          [{
            "type": "dict",
            "first_space": "",
            "second_space": "",
            "value": [{
                "type": "dictitem",
                "first_space": "",
                "second_space": " ",
                "key": {
                    "type": "name",
                    "value": "a",
                },
                "value": {
                    "type": "name",
                    "value": "b",
                }
            }],
          }])

def test_dict_more():
    "{a: b, b: c, c: d}"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ''),
           ('NAME', 'a'),
           ('COLON', ':', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COLON', ':', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COLON', ':', '', ' '),
           ('NAME', 'd'),
           ('RIGHT_BRACKET', '}', '', ''),
          ],
          [{
            "type": "dict",
            "first_space": "",
            "second_space": "",
            "value": [{
                "type": "dictitem",
                "first_space": "",
                "second_space": " ",
                "key": {
                    "type": "name",
                    "value": "a",
                },
                "value": {
                    "type": "name",
                    "value": "b",
                }
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
                "type": "dictitem",
                "first_space": "",
                "second_space": " ",
                "key": {
                    "type": "name",
                    "value": "b",
                },
                "value": {
                    "type": "name",
                    "value": "c",
                }
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
                "type": "dictitem",
                "first_space": "",
                "second_space": " ",
                "key": {
                    "type": "name",
                    "value": "c",
                },
                "value": {
                    "type": "name",
                    "value": "d",
                }
            }],
          }])

def test_set_one():
    "{a}"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ''),
           ('NAME', 'a'),
           ('RIGHT_BRACKET', '}', '', ''),
          ],
          [{
            "type": "set",
            "first_space": "",
            "second_space": "",
            "value": [{
                "type": "name",
                "value": "a",
            }],
          }])

def test_set_more():
    "{a, b, c}"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ''),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('RIGHT_BRACKET', '}', '', ''),
          ],
          [{
            "type": "set",
            "first_space": "",
            "second_space": "",
            "value": [{
                "type": "name",
                "value": "a",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
                "type": "name",
                "value": "b",
            },{
               "type": "comma",
               "first_space": "",
               "second_space": " ",
            },{
                "type": "name",
                "value": "c",
            }],
          }])

def test_generator_comprehension():
    "( a for b in c )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "generator_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [],
            }]
          }])

def test_generator_comprehension_if():
    "( a for b in c if d )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'd'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "generator_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "d"
                    },
                }],
            }]
          }])

def test_generator_comprehension_if_if():
    "( a for b in c if d if e )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'd'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'e'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "generator_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "d"
                    },
                },{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "e"
                    },
                }],
            }]
          }])

def test_generator_comprehension_double():
    "( a for b in c for d in e )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'd'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'e'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "generator_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [],
            },{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "d",
                },
                "target": {
                   "type": "name",
                   "value": "e",
                },
                "ifs": [],
            }]
          }])

def test_generator_comprehension_double_if_if():
    "( a for b in c if x for d in e if y )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'x'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'd'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'e'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'y'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "generator_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "x"
                    },
                }],
            },{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "d",
                },
                "target": {
                   "type": "name",
                   "value": "e",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "y"
                    },
                }],
            }]
          }])

def test_list_comprehension():
    "[ a for b in c ]"
    parse_simple([
           ('LEFT_SQUARE_BRACKET', '[', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('RIGHT_SQUARE_BRACKET', ']', ' ', ''),
          ],
          [{
            "type": "list_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [],
            }]
          }])

def test_list_comprehension_if():
    "[ a for b in c if d ]"
    parse_simple([
           ('LEFT_SQUARE_BRACKET', '[', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'd'),
           ('RIGHT_SQUARE_BRACKET', ']', ' ', ''),
          ],
          [{
            "type": "list_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "d"
                    },
                }],
            }]
          }])

def test_set_comprehension():
    "{ a for b in c }"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('RIGHT_BRACKET', '}', ' ', ''),
          ],
          [{
            "type": "set_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [],
            }]
          }])

def test_set_comprehension_if():
    "{ a for b in c if d }"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'd'),
           ('RIGHT_BRACKET', '}', ' ', ''),
          ],
          [{
            "type": "set_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "d"
                    },
                }],
            }]
          }])

def test_set_comprehension_double_if_if():
    "{ a for b in c if x for d in e if y }"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ' '),
           ('NAME', 'a'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'x'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'd'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'e'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'y'),
           ('RIGHT_BRACKET', '}', ' ', ''),
          ],
          [{
            "type": "set_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
               "type": "name",
               "value": "a",
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "x"
                    },
                }],
            },{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "d",
                },
                "target": {
                   "type": "name",
                   "value": "e",
                },
                "ifs": [{
                    "type": "comprehension_if",
                    "first_space": " ",
                    "second_space": " ",
                    "value": {
                        "type": "name",
                        "value": "y"
                    },
                }],
            }]
          }])

def test_dict_comprehension():
    "{ a: x for b in c }"
    parse_simple([
           ('LEFT_BRACKET', '{', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':', '', ' '),
           ('NAME', 'x'),
           ('FOR', 'for', ' ', ' '),
           ('NAME', 'b'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'c'),
           ('RIGHT_BRACKET', '}', ' ', ''),
          ],
          [{
            "type": "dict_comprehension",
            "first_space": " ",
            "second_space": " ",
            "result": {
                "key": {
                    "type": "name",
                    "value": "a",
                },
                "first_space": "",
                "second_space": " ",
                "value": {
                    "type": "name",
                    "value": "x",
                },
            },
            "generators": [{
                "type": "comprehension_loop",
                "first_space": " ",
                "second_space": " ",
                "third_space": " ",
                "forth_space": " ",
                "iterator": {
                   "type": "name",
                   "value": "b",
                },
                "target": {
                   "type": "name",
                   "value": "c",
                },
                "ifs": [],
            }]
          }])

def test_prioritizing_parenthesis():
    "( a )"
    parse_simple([
           ('LEFT_PARENTHESIS', '(', '', ' '),
           ('YIELD', 'yield', '', ' '),
           ('NAME', 'a'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "yield_atom",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "value": {
                "type": "name",
                "value": "a",
            },
          }])

### atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
### atom: '[' [SPACE] [listmaker] [SPACE] ']'
### atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# atom: '`' [SPACE] testlist1 [SPACE] '`'

# -

### testlist_safe: old_test
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+]
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+ [SPACE] [',']]

# -

# yield_expr: déjà fait

# -

# lambdef: 'lambda' [SPACE] ':' [SPACE] test
# lambdef: 'lambda' [SPACE] [varargslist] [SPACE] ':' [SPACE] test

# -

### trailer: '.' [SPACE] NAME
### trailer: '[' [SPACE] ']'
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
### trailer: '(' [SPACE] ')'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# -

# subscriptlist: subscript
# subscriptlist: subscript [SPACE] [',']
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)*
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)* [SPACE] [',']

# -

# subscript: test
# subscript: '.' [SPACE] '.' [SPACE] '.'
# subscript: [test] [SPACE] ':' [SPACE] [test] [SPACE] [sliceop]

# -

# sliceop: ':' [SPACE] [test]

# -

# exprlist: expr
# exprlist: expr [SPACE] [',']
# exprlist: expr ([SPACE] ',' [SPACE] expr)*
# exprlist: expr ([SPACE] ',' [SPACE] expr)* [SPACE] [',']

# -

# testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# for reference
# arglist: (argument [SPACE] ',' [SPACE])* (argument [SPACE] [','] |'*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test] |'**' [SPACE] test)


# arglist: (argument [SPACE] ',' [SPACE])*
# arglist: argument [SPACE] [',']
# arglist: (argument [SPACE] ',' [SPACE])* argument [SPACE] [',']
# arglist: '**' [SPACE] test
# arglist: (argument [SPACE] ',' [SPACE])* '**' [SPACE] test

# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]
# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]

# -

# argument: test
# argument: test [SPACE] comp_for
# argument: test [SPACE] '=' [SPACE] test

# -

# testlist1: test
# testlist1: test ([SPACE] ',' [SPACE] test)*

# -

### old_test: or_test
# old_test: old_lambdef

# -

# old_lambdef: 'lambda' [space] ':' [space] old_test
# old_lambdef: 'lambda' space [varargslist] [space] ':' [space] old_test
