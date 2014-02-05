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
             ('STAR', '*'),
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
           ('COMMA', ','),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [{
            "type": "tuple",
            "first_space": " ",
            "second_space": " ",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "comma",
               "value": ",",
            }],
          }])

# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
# atom: '[' [SPACE] [listmaker] [SPACE] ']'
# atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# atom: '`' [SPACE] testlist1 [SPACE] '`'

# -

# testlist_comp: test
# testlist_comp: test [SPACE] comp_for
# testlist_comp: test ([SPACE] ',' [SPACE] test)*
# testlist_comp: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# yield_expr: déjà fait

# -

# listmaker: test
# listmaker: test [SPACE] list_for
# listmaker: test ([SPACE] ',' [SPACE] test)*
# listmaker: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

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

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE]
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)*)
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)* [SPACE] [','])

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] comp_for

# dictorsetmaker: test [SPACE] comp_for

# dictorsetmaker: test [SPACE]
# dictorsetmaker: test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)*
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

### classdef: 'class' SPACE NAME [SPACE] ['(' [SPACE] [testlist] [SPACE] ')'] [SPACE] ':' [SPACE] suite

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
# argument: test [SPACE comp_for]
# argument: test [SPACE] '=' [SPACE] test

# -

# list_iter: list_if
# list_iter: list_for

# -

# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe
# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe [SPACE list_iter]

# -

# list_if: 'if' SPACE old_test
# list_if: 'if' SPACE old_test [SPACE list_iter]

# -

# comp_iter: comp_if
# comp_iter: comp_for

# -

# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# -

# comp_if: 'if' SPACE old_test
# comp_if: 'if' SPACE old_test [SPACE comp_iter]

# -

# testlist1: test
# testlist1: test ([SPACE] ',' [SPACE] test)*
