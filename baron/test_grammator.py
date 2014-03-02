#!/usr/bin/python
# -*- coding:Utf-8 -*-
from test_utils import parse_simple, inteu, endl, name, parse_multi

def test_empty():
    ""
    parse_simple([

    ], [])

def test_int():
    "1"
    parse_simple([
           ('INT', '1')],
          [inteu("1")])

def test_name():
    "a"
    parse_simple([
           ('NAME', 'a')],
          [name("a")])

def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    parse_simple([
           ('STRING', '"pouet pouet"')],
          [{ "type": "string", "value": '"pouet pouet"', }])
    parse_simple([
           ('STRING', '"""pouet pouet"""')],
          [{ "type": "string", "value": '"""pouet pouet"""', }])

def test_file_input_empty():
    ""
    parse_multi([
        ],[
        ])

def test_file_input_one_item():
    "a"
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'),
           endl("\n"),
          ])

def test_file_input_two_items():
    """
    a
    a
    """
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), endl("\n"),
           name('a'), endl("\n"),
          ])

def test_file_input_two_items_endl():
    """
    a

    a
    """
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), endl("\n"),
           endl("\n"),
           name('a'), endl("\n"),
          ])

def test_file_input_simple_stmt_one_item_semicolon():
    """
    a;
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('ENDL', '\n'),
        ],[
           name('a'), { "type": "semicolon", "value": ";", "before_space": "", "after_space": "", }, endl("\n"),
          ])

def test_file_input_simple_stmt_two_items_semicolon():
    """
    a;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), { "type": "semicolon", "value": ";", "before_space": "", "after_space": "", }, name('a'), endl("\n"),
          ])

def test_file_input_simple_stmt_three_items_semicolon():
    """
    a;b;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), {"type": "semicolon", "value": ";", "before_space": "", "after_space": ""}, name('b'), { "type": "semicolon", "value": ";", "before_space": "", "after_space": "", }, name('a'), endl("\n"),
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), {"type": "semicolon", "value": ";", "before_space": "", "after_space": ""}, name('b'), { "type": "semicolon", "value": ";", "before_space": "", "after_space": "", }, name('a'), endl("\n"),
          ])

def test_file_input_simple_stmt_one_item_semicolon_space():
    """
    a ;
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';', ' ', ' '), ('ENDL', '\n'),
        ],[
           name('a'), { "type": "semicolon", "value": ";", "before_space": ' ', "after_space": ' ', }, endl("\n"),
          ])

def test_funcdef_stmt_indent():
    """
    def a () :
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '(', ' '),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_space": " ",
            "second_space": " ",
            "third_space": "",
            "forth_space": "",
            "fith_space": " ",
            "arguments": [],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "space": "",
               "indent": "",
               "value": "\n"
            }],
          }])

def test_funcdef_stmt_one_parameter_indent():
    """
    def a ( x ) :
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '(', ' ', ' '),
             ('NAME', 'x'),
             ('RIGHT_PARENTHESIS', ')', ' '),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": " ",
            "fith_space": " ",
            "arguments": [{
                "type": "argument",
                "first_space": "",
                "second_space": "",
                "value": {
                    "type": "name",
                    "value": "x",
                },
                "default": {},
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "space": "",
               "indent": "",
               "value": "\n"
            }],
          }])

def test_funcdef_stmt_one_parameter_comma_indent():
    """
    def a ( x , ) :
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '(', ' ', ' '),
             ('NAME', 'x'),
             ('COMMA', ',', ' ', ' '),
             ('RIGHT_PARENTHESIS', ')', ' '),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "decorators": [],
            "name": "a",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": " ",
            "fith_space": " ",
            "arguments": [{
                "type": "argument",
                "first_space": "",
                "second_space": "",
                "value": {
                    "type": "name",
                    "value": "x",
                },
                "default": {},
            },{
                "type": "comma",
                "first_space": " ",
                "second_space": " ",
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "space": "",
               "indent": "",
               "value": "\n"
            }],
          }])

def test_funcdef_stmt_one_parameter_comma_default_indent():
    """
    def a ( x=1 , ) :
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '(', ' ', ' '),
             ('NAME', 'x'),
             ('EQUAL', '='),
             ('INT', '1'),
             ('COMMA', ',', ' ', ' '),
             ('RIGHT_PARENTHESIS', ')', ' '),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "decorators": [],
            "name": "a",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": " ",
            "fith_space": " ",
            "arguments": [{
                "type": "argument",
                "first_space": "",
                "second_space": "",
                "value": {
                    "type": "name",
                    "value": "x",
                },
                "default": {
                    "type": "int",
                    "value": "1",
                    "section": "number",
                },
            },{
                "type": "comma",
                "first_space": " ",
                "second_space": " ",
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_class_empty():
    """
    class A:
        pass
    """
    parse_multi([
             ('CLASS', 'class', '', ' '),
             ('NAME', 'A'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n', '', ''),
             ('DEDENT', ''),
          ],
          [{
            "type": "class",
            "name": "A",
            "parenthesis": False,
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": "",
            "inherit_from": [],
            "value": [{
               "type": "endl",
               "space": "",
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_class_empty_parenthesis():
    """
    class A ( ) :
        pass
    """
    parse_multi([
             ('CLASS', 'class', '', ' '),
             ('NAME', 'A'),
             ('LEFT_PARENTHESIS', '(', ' ', ' '),
             ('RIGHT_PARENTHESIS', ')', '', ' '),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n', '', ''),
             ('DEDENT', ''),
          ],
          [{
            "type": "class",
            "name": "A",
            "parenthesis": True,
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " ",
            "inherit_from": [],
            "value": [{
               "type": "endl",
               "space": "",
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_class_inherit():
    """
    class A ( B ) :
        pass
    """
    parse_multi([
             ('CLASS', 'class', '', ' '),
             ('NAME', 'A'),
             ('LEFT_PARENTHESIS', '(', ' ', ' '),
             ('NAME', 'B'),
             ('RIGHT_PARENTHESIS', ')', ' ', ' '),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n', '', ''),
             ('DEDENT', ''),
          ],
          [{
            "type": "class",
            "name": "A",
            "parenthesis": True,
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": " ",
            "fith_space": " ",
            "inherit_from": [{
                "type": "name",
                "value": "B"
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_funcdef_stmt_one_start_parameter_indent():
    """
    def a (*b):
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '('),
             ('STAR', '*'),
             ('NAME', 'b'),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": "",
            "arguments": [{
                "type": "list_argument",
                "first_space": "",
                "name": "b",
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "space": "",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_funcdef_stmt_one_star_star_parameter_indent():
    """
    def a (**b):
        pass
    """
    parse_multi([
             ('DEF', 'def', '', ' '),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '('),
             ('DOUBLE_STAR', '**'),
             ('NAME', 'b'),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": "",
            "arguments": [{
                "type": "dict_argument",
                "first_space": "",
                "second_space": "",
                "name": "b",
            }],
            "value": [{
               "type": "endl",
               "space": "",
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n"
            }],
          }])

def test_comment():
    """
      # comment
    """
    parse_multi([
             ('COMMENT', '# comment', '  ', ''),
             ('ENDL', '\n'),
          ],
          [{
            "space": "  ",
            "type": "comment",
            "value": "# comment",
          },{
            "space": "",
            "indent": "",
            "type": "endl",
            "value": "\n",
          }])

def test_with_a():
    """
    with a: pass
    """
    parse_multi([
             ('WITH', 'with', '', ' '),
             ('NAME', 'a'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "type": "with",
            "contexts": [{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "a",
                },
                "first_space": "",
                "second_space": "",
                "as": {},
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_with_a_as_b():
    """
    with a as b: pass
    """
    parse_multi([
             ('WITH', 'with', '', ' '),
             ('NAME', 'a'),
             ('AS', 'as', ' ', ' '),
             ('NAME', 'b'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "type": "with",
            "contexts": [{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "a",
                },
                "first_space": " ",
                "second_space": " ",
                "as": {
                    "type": "name",
                    "value": "b",
                },
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_with_a_as_b_c():
    """
    with a as b, c: pass
    """
    parse_multi([
             ('WITH', 'with', '', ' '),
             ('NAME', 'a'),
             ('AS', 'as', ' ', ' '),
             ('NAME', 'b'),
             ('COMMA', ',', '', ' '),
             ('NAME', 'c'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "type": "with",
            "contexts": [{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "a",
                },
                "first_space": " ",
                "second_space": " ",
                "as": {
                    "type": "name",
                    "value": "b",
                },
            },{
               "type": "comma",
                "first_space": "",
                "second_space": " ",
            },{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "c",
                },
                "first_space": "",
                "second_space": "",
                "as": {},
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_decorator():
    """
    @a
    def b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('ENDL', '\n'),
             ('DEF', 'def', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "space": "",
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_decorator_parenthesis():
    """
    @a()
    def b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('ENDL', '\n'),
             ('DEF', 'def', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "space": "",
                "call": {
                    "third_space": "",
                    "type": "call",
                    "first_space": "",
                    "value": [],
                    "second_space": "",
                },
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_decorator_parenthesis_arg():
    """
    @a(c)
    def b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('LEFT_PARENTHESIS', '('),
             ('NAME', 'c'),
             ('RIGHT_PARENTHESIS', ')'),
             ('ENDL', '\n'),
             ('DEF', 'def', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "space": "",
                "call": {
                    "third_space": "",
                    "type": "call",
                    "first_space": "",
                    "value": [{
                        "default": {},
                        "first_space": "",
                        "second_space": "",
                        "type": "argument",
                        "value": {
                            "type": "name",
                            "value": "c",
                        },
                    }],
                    "second_space": "",
                },
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_decorator_two():
    """
    @a
    @ c
    def b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('ENDL', '\n'),
             ('AT', '@', '', ' '),
             ('NAME', 'c'),
             ('ENDL', '\n'),
             ('DEF', 'def', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "space": "",
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            },{
                "type": "decorator",
                "space": " ",
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "c",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_class_decorator():
    """
    @a
    class b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('ENDL', '\n'),
             ('CLASS', 'class', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "call": {},
                "space": "",
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_class_decorator_two():
    """
    @a
    @ c
    class b(): pass
    """
    parse_multi([
             ('AT', '@', '', ''),
             ('NAME', 'a'),
             ('ENDL', '\n'),
             ('AT', '@', '', ' '),
             ('NAME', 'c'),
             ('ENDL', '\n'),
             ('CLASS', 'class', '', ' '),
             ('NAME', 'b'),
             ('LEFT_PARENTHESIS', '('),
             ('RIGHT_PARENTHESIS', ')'),
             ('COLON', ':', '', ' '),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "call": {},
                "space": "",
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            },{
                "type": "decorator",
                "call": {},
                "space": " ",
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "c",
                    }],
                }
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_fplist():
    """
    def a((b,)): pass
    """
    parse_multi([
            ('DEF', 'def', '', ' '),
            ('NAME', 'a'),
            ('LEFT_PARENTHESIS', '('),
            ('LEFT_PARENTHESIS', '('),
            ('NAME', 'b'),
            ('COMMA', ','),
            ('RIGHT_PARENTHESIS', ')'),
            ('RIGHT_PARENTHESIS', ')'),
            ('COLON', ':', '', ' '),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [{
                "type": "argument",
                "default": {},
                "first_space": "",
                "second_space": "",
                "value": {
                    "type": "tuple",
                    "first_space": "",
                    "second_space": "",
                    "value": [{
                        "type": "argument",
                        "default": {},
                        "first_space": "",
                        "second_space": "",
                        "value": {
                            "type": "name",
                            "value": "b",
                        },
                    },{
                        "type": "comma",
                        "first_space": "",
                        "second_space": "",
                    }],
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_fplist_two():
    """
    def a((b,c)): pass
    """
    parse_multi([
            ('DEF', 'def', '', ' '),
            ('NAME', 'a'),
            ('LEFT_PARENTHESIS', '('),
            ('LEFT_PARENTHESIS', '('),
            ('NAME', 'b'),
            ('COMMA', ','),
            ('NAME', 'c'),
            ('RIGHT_PARENTHESIS', ')'),
            ('RIGHT_PARENTHESIS', ')'),
            ('COLON', ':', '', ' '),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [{
                "type": "argument",
                "default": {},
                "first_space": "",
                "second_space": "",
                "value": {
                    "type": "tuple",
                    "first_space": "",
                    "second_space": "",
                    "value": [{
                        "type": "argument",
                        "default": {},
                        "first_space": "",
                        "second_space": "",
                        "value": {
                            "type": "name",
                            "value": "b",
                        },
                    },{
                        "type": "comma",
                        "first_space": "",
                        "second_space": "",
                    },{
                        "type": "argument",
                        "default": {},
                        "first_space": "",
                        "second_space": "",
                        "value": {
                            "type": "name",
                            "value": "c",
                        },
                    }],
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])

def test_fplist_alone():
    """
    def a((b)): pass
    """
    parse_multi([
            ('DEF', 'def', '', ' '),
            ('NAME', 'a'),
            ('LEFT_PARENTHESIS', '('),
            ('LEFT_PARENTHESIS', '('),
            ('NAME', 'b'),
            ('RIGHT_PARENTHESIS', ')'),
            ('RIGHT_PARENTHESIS', ')'),
            ('COLON', ':', '', ' '),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
          ],
          [{
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "fith_space": "",
            "forth_space": "",
            "type": "funcdef",
            "arguments": [{
                "type": "associative_parenthesis",
                "first_space": "",
                "second_space": "",
                "value": {
                    "default": {},
                    "type": "argument",
                    "first_space": "",
                    "second_space": "",
                    "value": {
                        "type": "name",
                        "value": "b",
                    },
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "space": "",
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])
