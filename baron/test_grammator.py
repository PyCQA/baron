#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import (parse_simple, inteu, endl, name,
                        string, parse_multi, semicolon)

def test_empty():
    ""
    parse_simple([

    ], [])

def test_int():
    "1"
    parse_simple([
           ('INT', '1')],
          [inteu("1")])

# TODO: will be done in file_input
#def test_endl():
    #"\n"
    #parse_simple([
           #('ENDL', '\n')],
          #[endl("\n", before_space="")])

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
          [string('"pouet pouet"')])
    parse_simple([
           ('STRING', '"""pouet pouet"""')],
          [string('"""pouet pouet"""')])

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
           name('a'), endl("\n"),
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
           name('a'), semicolon(), endl("\n"),
          ])

def test_file_input_simple_stmt_two_items_semicolon():
    """
    a;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), semicolon(), name('a'), endl("\n"),
          ])

def test_file_input_simple_stmt_three_items_semicolon():
    """
    a;b;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           name('a'), semicolon(), name('b'), semicolon(), name('a'), endl("\n"),
          ])

def test_file_input_simple_stmt_one_item_semicolon_space():
    """
    a ;
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';', ' ', ' '), ('ENDL', '\n'),
        ],[
           name('a'), semicolon(' ', ' '), endl("\n"),
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
            "first_space": " ",
            "second_space": " ",
            "third_space": "",
            "forth_space": "",
            "fith_space": " ",
            "arguments": [],
            "value": [{
               "type": "endl",
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
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
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
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
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
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
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
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
               "type": "endl",
               "value": "\n",
            }],
          }])


### fpdef: NAME
# fpdef: '(' [SPACE] fplist [SPACE] ')'

# -

# fplist: fpdef
# fplist: fpdef [SPACE] ',' [SPACE] fpdef
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)*
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)* [SPACE] [',']

# -

# decorator: '@' [SPACE] dotted_name [SPACE] NEWLINE
# decorator: '@' dotted_name [ [SPACE] '(' [SPACE] [arglist] [SPACE] ')' ] [SPACE] NEWLINE

# -

# decorators: (decorator [BLANKLINE])+

# -

# decorated: decorators classdef
# decorated: decorators funcdef

# -

### expr_stmt: testlist
### expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# expr_stmt: testlist augassign yield_expr
### expr_stmt: testlist augassign testlist

# -

### compound_stmt: if_stmt
### compound_stmt: while_stmt
### compound_stmt: for_stmt
### compound_stmt: try_stmt
### compound_stmt: with_stmt
### compound_stmt: funcdef
### compound_stmt: classdef
# compound_stmt: decorated
