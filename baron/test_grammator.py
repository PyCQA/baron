#!/usr/bin/python
# -*- coding:Utf-8 -*-
from test_utils import parse_simple, parse_multi

def test_empty():
    ""
    parse_simple([

    ], [])

def test_int():
    "1"
    parse_simple([
           ('INT', '1')],
          [{
            "type": "int",
            "section": "number",
            "value": "1",
           }])

def test_name():
    "a"
    parse_simple([
           ('NAME', 'a')],
          [{ "type": "name", "value": "a", }])

def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    parse_simple([
           ('STRING', '"pouet pouet"')],
          [{
            "type": "string",
            "value": '"pouet pouet"',
            "first_formatting": [],
            "second_formatting": [],
           }])
    parse_simple([
           ('STRING', '"""pouet pouet"""')],
          [{
            "type": "string",
            "value": '"""pouet pouet"""',
            "first_formatting": [],
            "second_formatting": [],
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
           { "type": "name", "value": 'a', },
           { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
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
           { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
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
           { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
           { "type": "name", "value": 'a', }, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
          ])
    parse_multi([
           ('NAME', 'a'), ('ENDL', '\n'),
           ('ENDL', '\n'),
           ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           {"type": "endl", "value": "\n", "indent": "", "formatting": []},
           { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])

def test_file_input_simple_stmt_one_item_semicolon():
    """
    a;
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])

def test_file_input_simple_stmt_two_items_semicolon():
    """
    a;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])

def test_file_input_simple_stmt_three_items_semicolon():
    """
    a;b;a
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, {"type": "name", "value": 'b'}, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, { "type": "name", "value": 'b', }, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, {"type": "name", "value": 'b'}, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, {"type": "name", "value": 'b'}, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, { "type": "name", "value": 'b', }, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, {"type": "name", "value": 'a'}, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';'), ('NAME', 'b'), ('SEMICOLON', ';'), ('NAME', 'a'), ('ENDL', '\n'),
        ],[
           {"type": "name", "value": 'a'}, {"type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": []}, {"type": "name", "value": 'b'}, { "type": "semicolon", "value": ";", "before_formatting": [], "after_formatting": [], }, { "type": "name", "value": 'a', }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
          ])

def test_file_input_simple_stmt_one_item_semicolon_space():
    """
    a ;
    """
    parse_multi([
           ('NAME', 'a'), ('SEMICOLON', ';', [('SPACE', ' ')], [('SPACE', ' ')]), ('ENDL', '\n'),
        ],[
           { "type": "name", "value": 'a', }, { "type": "semicolon", "value": ";", "before_formatting": [{"type": "space", "value": ' '}], "after_formatting": [{"type": "space", "value": ' '}], }, { "type": "endl", "value": "\n", "formatting": [], "indent": "", },
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
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "formatting": [],
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
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "forth_formatting": [{"type": "space", "value": " "}],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [{
                "type": "argument",
                "first_formatting": [],
                "second_formatting": [],
                "name": "x",
                "value": {},
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "formatting": [],
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
          ],
          [{
            "type": "funcdef",
            "decorators": [],
            "name": "a",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "forth_formatting": [{"type": "space", "value": " "}],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [{
                "type": "argument",
                "first_formatting": [],
                "second_formatting": [],
                "name": "x",
                "value": {},
            },{
                "type": "comma",
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "type": "endl",
               "formatting": [],
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
          ],
          [{
            "type": "funcdef",
            "decorators": [],
            "name": "a",
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "forth_formatting": [{"type": "space", "value": " "}],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "arguments": [{
                "type": "argument",
                "first_formatting": [],
                "second_formatting": [],
                "name": "x",
                "value": {
                    "type": "int",
                    "value": "1",
                    "section": "number",
                },
            },{
                "type": "comma",
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
             ('CLASS', 'class', [], [('SPACE', ' ')]),
             ('NAME', 'A'),
             ('COLON', ':'),
             ('ENDL', '\n', [], [('SPACE', '    ')]),
             ('INDENT', ''),
             ('PASS', 'pass'),
             ('ENDL', '\n', [], []),
             ('DEDENT', ''),
          ],
          [{
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": False,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": [],
            "sixth_formatting": [],
            "inherit_from": [],
            "value": [{
               "type": "endl",
               "formatting": [],
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "forth_formatting": [],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [],
            "value": [{
               "type": "endl",
               "formatting": [],
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "type": "class",
            "name": "A",
            "decorators": [],
            "parenthesis": True,
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "forth_formatting": [{"type": "space", "value": " "}],
            "fith_formatting": [{"type": "space", "value": " "}],
            "sixth_formatting": [],
            "inherit_from": [{
                "type": "name",
                "value": "B"
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [{
                "type": "list_argument",
                "first_formatting": [],
                "value": "b",
            }],
            "value": [{
               "type": "endl",
               "value": "\n",
               "formatting": [],
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "type": "funcdef",
            "name": "a",
            "decorators": [],
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "arguments": [{
                "type": "dict_argument",
                "first_formatting": [],
                "second_formatting": [],
                "value": "b",
            }],
            "value": [{
               "type": "endl",
               "formatting": [],
               "value": "\n",
               "indent": "    "
            },{
                "type": "pass",
            },{
               "formatting": [],
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
             ('COMMENT', '# comment', [('SPACE', '  ')]),
             ('ENDL', '\n'),
          ],
          [{
            "formatting": [{"type": "space", "value": "  "}],
            "type": "comment",
            "value": "# comment",
          },{
            "formatting": [],
            "indent": "",
            "type": "endl",
            "value": "\n",
          }])

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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "contexts": [{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "a",
                },
                "first_formatting": [],
                "second_formatting": [],
                "as": {},
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
             ('WITH', 'with', [], [('SPACE', ' ')]),
             ('NAME', 'a'),
             ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
             ('NAME', 'b'),
             ('COLON', ':', [], [('SPACE', ' ')]),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "contexts": [{
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
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
             ('WITH', 'with', [], [('SPACE', ' ')]),
             ('NAME', 'a'),
             ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
             ('NAME', 'b'),
             ('COMMA', ',', [], [('SPACE', ' ')]),
             ('NAME', 'c'),
             ('COLON', ':', [], [('SPACE', ' ')]),
             ('PASS', 'pass'),
             ('ENDL', '\n'),
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [{"type": "space", "value": " "}],
            "type": "with",
            "contexts": [{
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
            },{
               "type": "comma",
                "first_formatting": [],
                "second_formatting": [{"type": "space", "value": " "}],
            },{
                "type": "with_context_item",
                "value": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": [],
                "as": {},
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "formatting": [],
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "formatting": [],
                "call": {
                    "third_formatting": [],
                    "type": "call",
                    "first_formatting": [],
                    "value": [],
                    "second_formatting": [],
                },
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "formatting": [],
                "call": {
                    "third_formatting": [],
                    "type": "call",
                    "first_formatting": [],
                    "value": [{
                        "name": {},
                        "first_formatting": [],
                        "second_formatting": [],
                        "type": "argument",
                        "value": {
                            "type": "name",
                            "value": "c",
                        },
                    }],
                    "second_formatting": [],
                },
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [],
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "formatting": [],
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            },{
                "type": "decorator",
                "formatting": [{"type": "space", "value": " "}],
                "call": {},
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "c",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "call": {},
                "formatting": [],
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "class",
            "inherit_from": [],
            "parenthesis": True,
            "name": "b",
            "decorators": [{
                "type": "decorator",
                "call": {},
                "formatting": [],
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "a",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            },{
                "type": "decorator",
                "call": {},
                "formatting": [{"type": "space", "value": " "}],
                "value": {
                    "type": "dotted_name",
                    "value": [{
                    "type": "name",
                    "value": "c",
                    }],
                }
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [{
                "type": "argument",
                "value": {},
                "first_formatting": [],
                "second_formatting": [],
                "name": {
                    "type": "tuple",
                    "first_formatting": [],
                    "second_formatting": [],
                    "value": [{
                        "type": "argument",
                        "value": {},
                        "first_formatting": [],
                        "second_formatting": [],
                        "name": "b",
                    },{
                        "type": "comma",
                        "first_formatting": [],
                        "second_formatting": [],
                    }],
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [{
                "type": "argument",
                "value": {},
                "first_formatting": [],
                "second_formatting": [],
                "name": {
                    "type": "tuple",
                    "first_formatting": [],
                    "second_formatting": [],
                    "value": [{
                        "type": "argument",
                        "value": {},
                        "first_formatting": [],
                        "second_formatting": [],
                        "name": "b",
                    },{
                        "type": "comma",
                        "first_formatting": [],
                        "second_formatting": [],
                    },{
                        "type": "argument",
                        "value": {},
                        "first_formatting": [],
                        "second_formatting": [],
                        "name": "c",
                    }],
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
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
          ],
          [{
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [],
            "third_formatting": [],
            "fith_formatting": [],
            "forth_formatting": [],
            "sixth_formatting": [{"type": "space", "value": " "}],
            "type": "funcdef",
            "arguments": [{
                "type": "associative_parenthesis",
                "first_formatting": [],
                "second_formatting": [],
                "value": {
                    "value": {},
                    "type": "argument",
                    "first_formatting": [],
                    "second_formatting": [],
                    "name": "b",
                }
            }],
            "name": "a",
            "decorators": [],
            "value": [{
               "type": "pass",
            },{
               "formatting": [],
               "indent": "",
               "type": "endl",
               "value": "\n",
            }],
          }])
