#!/usr/bin/python
# -*- coding:Utf-8 -*-

from utils import return_, yield_
from test_utils import (parse_simple, space, inteu, endl, name, string, comma,
                        parse_multi, semicolon)

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

def test_return():
    "return"
    parse_simple([
           ('RETURN', 'return'),
          ],
         [return_()])

def test_return_a():
    "return a"
    parse_simple([
           ('RETURN', 'return', '', ' '),
           ('NAME', 'a'),
          ],
         [return_(name('a'), space=" ")])

def test_yield():
    "yield"
    parse_simple([
           ('YIELD', 'yield'),
          ],
         [yield_()])

def test_yield_a():
    "yield a"
    parse_simple([
           ('YIELD', 'yield', '', ' '),
           ('NAME', 'a'),
          ],
         [yield_(name('a'), space=" ")])

def test_del():
    "del a"
    parse_simple([
           ('DEL', 'del', '', ' '),
           ('NAME', 'a'),
          ],
          [
           {
            "type": "del",
            "value": name('a'),
            "space": " ",
           }
          ])

def test_break():
    "break"
    parse_simple([
           ('BREAK', 'break'),
          ],
          [{
            "type": "break",
          }])

def test_continue():
    "continue"
    parse_simple([
           ('CONTINUE', 'continue'),
          ],
          [{
            "type": "continue",
          }])

def test_pass():
    "pass"
    parse_simple([
           ('PASS', 'pass'),
          ],
          [{
            "type": "pass",
          }])

def test_assert():
    "assert a"
    parse_simple([
           ('ASSERT', 'assert', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "assert",
            "value": name('a'),
            "message": None,
            "first_space": " ",
            "second_space": "",
            "third_space": ""
          }])

def test_assert_message():
    "assert a , b"
    parse_simple([
           ('ASSERT', 'assert', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "assert",
            "value": name('a'),
            "message": name('b'),
            "first_space": " ",
            "second_space": " ",
            "third_space": " "
          }])

def test_raise_empty():
    "raise"
    parse_simple([
           ('RAISE', 'raise', '', ' '),
          ],
          [{
            "type": "raise",
            "value": None,
            "instance": None,
            "traceback": None,
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
          }])

def test_raise():
    "raise a"
    parse_simple([
           ('RAISE', 'raise', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "raise",
            "value": name('a'),
            "instance": None,
            "traceback": None,
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
          }])

def test_raise_instance():
    "raise a, b"
    parse_simple([
           ('RAISE', 'raise', '', ' '),
           ('NAME', 'a'),
           ('COMMA', 'comma', '', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "raise",
            "value": name('a'),
            "instance": name('b'),
            "traceback": None,
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "forth_space": "",
            "fith_space": ""
          }])

def test_raise_instance_traceback():
    "raise a, b, c"
    parse_simple([
           ('RAISE', 'raise', '', ' '),
           ('NAME', 'a'),
           ('COMMA', 'comma', '', ' '),
           ('NAME', 'b'),
           ('COMMA', 'comma', '', ' '),
           ('NAME', 'c'),
          ],
          [{
            "type": "raise",
            "value": name('a'),
            "instance": name('b'),
            "traceback": name('c'),
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])

def test_exec():
    "exec a"
    parse_simple([
           ('EXEC', 'exec', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "exec",
            "value": name('a'),
            "globals": None,
            "locals": None,
            "first_space": " ",
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
          }])

def test_exec_in():
    "exec a in b"
    parse_simple([
           ('EXEC', 'exec', '', ' '),
           ('NAME', 'a'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "exec",
            "value": name('a'),
            "globals": name('b'),
            "locals": None,
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": ""
          }])

def test_exec_in_c():
    "exec a in b, c"
    parse_simple([
           ('EXEC', 'exec', '', ' '),
           ('NAME', 'a'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
          ],
          [{
            "type": "exec",
            "value": name('a'),
            "globals": name('b'),
            "locals": name('c'),
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])

def test_global():
    "global a"
    parse_simple([
           ('GLOBAL', 'global', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "global",
            "space": " ",
            "value": [
                      name('a'),
                     ]
          }])

def test_global_one():
    "global a, b"
    parse_simple([
           ('GLOBAL', 'global', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "global",
            "space": " ",
            "value": [
                      name('a'),
                      comma(),
                      space(),
                      name('b'),
                     ]
          }])

def test_global_two():
    "global a, b ,  c"
    parse_simple([
           ('GLOBAL', 'global', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', '  '),
           ('NAME', 'c'),
          ],
          [{
            "type": "global",
            "space": " ",
            "value": [
                      name('a'),
                      comma(),
                      space(),
                      name('b'),
                      space(),
                      comma(),
                      space("  "),
                      name('c'),
                     ]
          }])

def test_print():
    "print"
    parse_simple([
           ('PRINT', 'print', '', ''),
          ],
          [{
            "type": "print",
            "space": "",
            "value": None,
            "destination_space": "",
            "destination": None,
          }])

def test_print_a():
    "print a"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": [name('a')],
            "destination_space": "",
            "destination": None,
          }])

def test_print_a_b():
    "print a, b"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": [
                      name('a'),
                      comma(),
                      space(),
                      name('b'),
                     ],
            "destination_space": "",
            "destination": None,
          }])

def test_print_a_b_comma():
    "print a, b,"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ''),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": [
                      name('a'),
                      comma(),
                      space(),
                      name('b'),
                      comma(),
                     ],
            "destination_space": "",
            "destination": None,
          }])

def test_print_redirect():
    "print >> a"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('RIGHT_SHIFT', '>>', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": None,
            "destination_space": " ",
            "destination": name('a'),
          }])

def test_print_redirect_ab():
    "print >> a , b"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('RIGHT_SHIFT', '>>', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": [
                      space(),
                      comma(),
                      space(),
                      name('b'),
                     ],
            "destination": name('a'),
            "destination_space": " ",
          }])

def test_print_redirect_ab_comma():
    "print >> a , b ,"
    parse_simple([
           ('PRINT', 'print', '', ' '),
           ('RIGHT_SHIFT', '>>', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', ''),
          ],
          [{
            "type": "print",
            "space": " ",
            "value": [
                      space(),
                      comma(),
                      space(),
                      name('b'),
                      space(),
                      comma(),
                     ],
            "destination": name('a'),
            "destination_space": " ",
          }])

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

def test_if_stmt():
    "if a: pass"
    parse_multi([
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
              "value": [{
                  "type": "pass",
              },{
                 "type": "endl",
                 "value": "\n"
              }],
             }],
          }])

def test_if_stmt_indent():
    """
    if a:
        pass
    """
    parse_multi([
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
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
          }]}])

def test_if_stmt_indent_two_endls():
    """
    if a:

        pass
    """
    parse_multi([
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
              "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": ""
              },{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
              },{
                  "type": "pass",
              },{
                 "type": "endl",
                 "value": "\n"
              }],
          }]}])

def test_if_stmt_indent_multiple_endls():
    """
    if a:


        pass
    """
    parse_multi([
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n'),
           ('ENDL', '\n', '', '  '),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
              "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": ""
              },{
                 "type": "endl",
                 "value": "\n",
                 "indent": "  "
              },{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
              },{
                  "type": "pass",
              },{
                 "type": "endl",
                 "value": "\n"
              }],
          }]}])

def test_if_else_stmt_indent():
    """
    if a:
        pass
    else:
        pass
    """
    parse_multi([
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELSE', 'else'),
           ('COLON', ':', " "),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
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
            },{
               "type": "else",
               "space": " ",
               "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
                 },{
                 "type": "pass",
                 },{
                 "type": "endl",
                 "value": "\n",
                 }
               ]
            }]
           }])

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
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELIF', 'elif', '', ' '),
           ('NAME', 'b'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELIF', 'elif', '', ' '),
           ('NAME', 'c'),
           ('COLON', ':', " "),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
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
            },{
              "type": "elif",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "b",
              },
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
            },{
              "type": "elif",
              "first_space": " ",
              "second_space": " ",
              "test": {
                  "type": "name",
                  "value": "c",
              },
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
            }]
           }])

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
           ('IF', 'if', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELIF', 'elif', '', ' '),
           ('NAME', 'b'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELIF', 'elif', '', ' '),
           ('NAME', 'c'),
           ('COLON', ':', " "),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELSE', 'else'),
           ('COLON', ':', " "),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "ifelseblock",
            "value": [{
              "type": "if",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "a",
              },
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
            },{
              "type": "elif",
              "first_space": " ",
              "second_space": "",
              "test": {
                  "type": "name",
                  "value": "b",
              },
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
            },{
              "type": "elif",
              "first_space": " ",
              "second_space": " ",
              "test": {
                  "type": "name",
                  "value": "c",
              },
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
            },{
               "type": "else",
               "space": " ",
               "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
                 },{
                 "type": "pass",
                 },{
                 "type": "endl",
                 "value": "\n",
                 }
               ]
            }]
           }])

def test_while_stmt_indent():
    """
    while a:
        pass
    """
    parse_multi([
           ('WHILE', 'while', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "while",
            "first_space": " ",
            "second_space": "",
            "else": {},
            "test": {
                "type": "name",
                "value": "a",
            },
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

def test_while_else_stmt_indent():
    """
    while a:
        pass
    else:
        pass
    """
    parse_multi([
           ('WHILE', 'while', '', ' '),
           ('NAME', 'a'),
           ('COLON', ':'),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
           ('ELSE', 'else'),
           ('COLON', ':', " "),
           ('ENDL', '\n', '', '    '),
           ('INDENT', ''),
           ('PASS', 'pass'),
           ('ENDL', '\n'),
           ('DEDENT', ''),
          ],
          [{
            "type": "while",
            "first_space": " ",
            "second_space": "",
            "test": {
                "type": "name",
                "value": "a",
            },
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
            "else": {
             "type": "else",
             "space": " ",
             "value": [{
               "type": "endl",
               "value": "\n",
               "indent": "    "
               },{
               "type": "pass",
               },{
               "type": "endl",
               "value": "\n",
               }]
             }
           }])

def test_for_stmt_indent():
    """
    for i in a:
        pass
    """
    parse_multi([
            ('FOR', 'for', '', ' '),
            ('NAME', 'i'),
            ('IN', 'in', ' ', ' '),
            ('NAME', 'a'),
            ('COLON', ':', '', ' '),
            ('ENDL', '\n', '', '    '),
            ('INDENT', ''),
            ('PASS', 'pass'),
            ('ENDL', '\n'),
            ('DEDENT', ''),
          ],
          [{
            "type": "for",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "else": {},
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "a",
            },
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

def test_for_else_stmt_indent():
    """
    for i in b:
        pass
    else:
        pass
    """
    parse_multi([
             ('FOR', 'for', '', ' '),
             ('NAME', 'i'),
             ('IN', 'in', ' ', ' '),
             ('NAME', 'b'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('ELSE', 'else'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "for",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "else": {
              "type": "else",
              "space": "",
              "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
                },{
                  "type": "pass",
                },{
                  "type": "endl",
                  "value": "\n",
                }]
            },
            "iterator": {
                "type": "name",
                "value": "i",
            },
            "target": {
                "type": "name",
                "value": "b",
            },
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

def test_try_finally_stmt_indent():
    """
    try :
        pass
    finally :
        pass
    """
    parse_multi([
             ('TRY', 'try'),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('FINALLY', 'finally'),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {},
            "finally": {
                "type": "finally",
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
                "space": " ",
            },
            "excepts": [],
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
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'Exception'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {},
            "finally": {},
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": "",
               "forth_space": "",
               "delimiteur": "",
               "target": {},
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
            },{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": "",
               "forth_space": "",
               "delimiteur": "",
               "target": {},
               "exceptions": {
                  "type": "name",
                  "value": "Exception",
               },
               "value": [{
                  "type": "endl",
                  "value": "\n",
                  "indent": "    "
               },{
                   "type": "pass",
               },{
                  "type": "endl",
                  "value": "\n"
               }]
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

def test_try_except_comma_stmt_indent():
    """
    try :
        pass
    except IOError, e:
        pass
    """
    parse_multi([
             ('TRY', 'try'),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('COMMA', ',', '', ' '),
             ('NAME', 'a'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {},
            "finally": {},
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": " ",
               "forth_space": "",
               "delimiteur": ",",
               "target": {
                    "type": "name",
                    "value": "a"
               },
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
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
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('COMMA', ',', '', ' '),
             ('NAME', 'a'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('ELSE', 'else'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {
              "type": "else",
              "space": "",
              "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
                },{
                  "type": "pass",
                },{
                  "type": "endl",
                  "value": "\n",
                }]
            },
            "finally": {},
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": " ",
               "forth_space": "",
               "delimiteur": ",",
               "target": {
                    "type": "name",
                    "value": "a"
               },
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
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
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('COMMA', ',', '', ' '),
             ('NAME', 'a'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('ELSE', 'else'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('FINALLY', 'finally'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {
              "type": "else",
              "space": "",
              "value": [{
                 "type": "endl",
                 "value": "\n",
                 "indent": "    "
                },{
                  "type": "pass",
                },{
                  "type": "endl",
                  "value": "\n",
                }]
            },
            "finally": {
                "type": "finally",
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
                "space": "",
            },
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": " ",
               "forth_space": "",
               "delimiteur": ",",
               "target": {
                    "type": "name",
                    "value": "a"
               },
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
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
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('COMMA', ',', '', ' '),
             ('NAME', 'a'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('FINALLY', 'finally'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {},
            "finally": {
                "type": "finally",
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
                "space": "",
            },
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": "",
               "third_space": " ",
               "forth_space": "",
               "delimiteur": ",",
               "target": {
                    "type": "name",
                    "value": "a"
               },
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
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

def test_try_except_as_stmt_indent():
    """
    try :
        pass
    except IOError as e:
        pass
    """
    parse_multi([
             ('TRY', 'try'),
             ('COLON', ':', ' '),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
             ('EXCEPT', 'except', '', ' '),
             ('NAME', 'IOError'),
             ('AS', 'as', ' ', ' '),
             ('NAME', 'a'),
             ('COLON', ':'),
             ('ENDL', '\n', '', '    '),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
             ('DEDENT', ''),
          ],
          [{
            "type": "try",
            "space": " ",
            "else": {},
            "finally": {},
            "excepts": [{
               "type": "except",
               "first_space": " ",
               "second_space": " ",
               "third_space": " ",
               "forth_space": "",
               "delimiteur": "as",
               "target": {
                    "type": "name",
                    "value": "a"
               },
               "exceptions": {
                  "type": "name",
                  "value": "IOError",
               },
                "value": [{
                    "type": "endl",
                    "value": "\n",
                    "indent": "    "
                 },{
                     "type": "pass",
                 },{
                    "type": "endl",
                    "value": "\n"
                 }]
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
