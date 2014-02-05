#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import parse_multi


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

