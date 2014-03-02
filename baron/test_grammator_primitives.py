#!/usr/bin/python
# -*- coding:Utf-8 -*-
from utils import return_, yield_
from test_utils import parse_simple


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
         [return_({ "type": "name", "value": 'a', }, space=" ")])

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
         [yield_({ "type": "name", "value": 'a', }, space=" ")])

def test_del():
    "del a"
    parse_simple([
           ('DEL', 'del', '', ' '),
           ('NAME', 'a'),
          ],
          [
           {
            "type": "del",
            "value": { "type": "name", "value": 'a', },
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
            "value": { "type": "name", "value": 'a', },
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
            "value": { "type": "name", "value": 'a', },
            "message": {"type": "name", "value": 'b'},
            "first_space": " ",
            "second_space": " ",
            "third_space": " "
          }])
    parse_simple([
           ('ASSERT', 'assert', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "assert",
            "value": {"type": "name", "value": 'a'},
            "message": { "type": "name", "value": 'b', },
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
            "value": { "type": "name", "value": 'a', },
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
            "value": { "type": "name", "value": 'a', },
            "instance": {"type": "name", "value": 'b'},
            "traceback": None,
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "forth_space": "",
            "fith_space": ""
          }])
    parse_simple([
           ('RAISE', 'raise', '', ' '),
           ('NAME', 'a'),
           ('COMMA', 'comma', '', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "raise",
            "value": {"type": "name", "value": 'a'},
            "instance": { "type": "name", "value": 'b', },
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
            "value": { "type": "name", "value": 'a', },
            "instance": {"type": "name", "value": 'b'},
            "traceback": {"type": "name", "value": 'c'},
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])
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
            "value": {"type": "name", "value": 'a'},
            "instance": { "type": "name", "value": 'b', },
            "traceback": {"type": "name", "value": 'c'},
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])
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
            "value": {"type": "name", "value": 'a'},
            "instance": {"type": "name", "value": 'b'},
            "traceback": { "type": "name", "value": 'c', },
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
            "value": { "type": "name", "value": 'a', },
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
            "value": { "type": "name", "value": 'a', },
            "globals": {"type": "name", "value": 'b'},
            "locals": None,
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": ""
          }])
    parse_simple([
           ('EXEC', 'exec', '', ' '),
           ('NAME', 'a'),
           ('IN', 'in', ' ', ' '),
           ('NAME', 'b'),
          ],
          [{
            "type": "exec",
            "value": {"type": "name", "value": 'a'},
            "globals": { "type": "name", "value": 'b', },
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
            "value": { "type": "name", "value": 'a', },
            "globals": {"type": "name", "value": 'b'},
            "locals": {"type": "name", "value": 'c'},
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])
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
            "value": {"type": "name", "value": 'a'},
            "globals": { "type": "name", "value": 'b', },
            "locals": {"type": "name", "value": 'c'},
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "forth_space": "",
            "fith_space": " "
          }])
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
            "value": {"type": "name", "value": 'a'},
            "globals": {"type": "name", "value": 'b'},
            "locals": { "type": "name", "value": 'c', },
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
                      { "type": "name", "value": 'a', },
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
                      { "type": "name", "value": 'a', },
                      { "type": "comma", "value": ",", },
                      { "type": "space", "value": " ", },
                      {"type": "name", "value": 'b'},
                     ]
          }])
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
                      {"type": "name", "value": 'a'},
                      { "type": "comma", "value": ",", },
                      { "type": "space", "value": " ", },
                      { "type": "name", "value": 'b', },
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
                     ]
          }])
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
                      {"type": "name", "value": "a"},
                     {"type": "comma", "value": ","},
                      {"type": "space", "value": " "},
                      {"type": "name", "value": "b"},
                      {"type": "space", "value": " "},
                      {"type": "comma", "value": ","},
                      {"type": "space", "value": "  "},
                      {"type": "name", "value": "c"},
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
            "value": [{ "type": "name", "value": 'a', }],
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
                      { "type": "name", "value": 'a', },
                      {"type": "comma", "first_space": "", "second_space": " "},
                      {"type": "name", "value": 'b'},
                     ],
            "destination_space": "",
            "destination": None,
          }])
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
                      {"type": "name", "value": 'a'},
                      {"type": "comma", "first_space": "", "second_space": " "},
                      { "type": "name", "value": 'b', },
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
                      { "type": "name", "value": 'a', },
                      {"type": "comma", "first_space": "", "second_space": " "},
                      {"type": "name", "value": 'b'},
                      {"type": "comma", "first_space": "", "second_space": ""},
                     ],
            "destination_space": "",
            "destination": None,
          }])
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
                      {"type": "name", "value": 'a'},
                      {"type": "comma", "first_space": "", "second_space": " "},
                      { "type": "name", "value": 'b', },
                      {"type": "comma", "first_space": "", "second_space": ""},
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
            "destination": { "type": "name", "value": 'a', },
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
                      {"type": "comma", "first_space": " ", "second_space": " "},
                      { "type": "name", "value": 'b', },
                     ],
            "destination": {"type": "name", "value": 'a'},
            "destination_space": " ",
          }])
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
                      {"type": "comma", "first_space": " ", "second_space": " "},
                      {"type": "name", "value": 'b'},
                     ],
            "destination": { "type": "name", "value": 'a', },
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
                      {"type": "comma", "first_space": " ", "second_space": " "},
                      { "type": "name", "value": 'b', },
                      {"type": "comma", "first_space": " ", "second_space": ""},
                     ],
            "destination": {"type": "name", "value": 'a'},
            "destination_space": " ",
          }])
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
                      {"type": "comma", "first_space": " ", "second_space": " "},
                      {"type": "name", "value": 'b'},
                      {"type": "comma", "first_space": " ", "second_space": ""},
                     ],
            "destination": { "type": "name", "value": 'a', },
            "destination_space": " ",
          }])

def test_lambda():
    "lambda : a"
    parse_simple([
           ('LAMBDA', 'lambda', '', ' '),
           ('COLON', ':', '', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "lambda",
            "first_space": " ",
            "second_space": "",
            "third_space": " ",
            "value": {
                "type": "name",
                "value": "a",
            },
            "arguments": []
          }])

def test_lambda_arguments():
    "lambda argument : a"
    parse_simple([
           ('LAMBDA', 'lambda', '', ' '),
           ('NAME', 'argument'),
           ('COLON', ':', ' ', ' '),
           ('NAME', 'a'),
          ],
          [{
            "type": "lambda",
            "first_space": " ",
            "second_space": " ",
            "third_space": " ",
            "value": {
                "type": "name",
                "value": "a",
            },
            "arguments": [{
                "default": {},
                "first_space": "",
                "second_space": "",
                "type": "argument",
                "value": {
                    "type": "name",
                    "value": "argument",
                },
            }]
          }])
