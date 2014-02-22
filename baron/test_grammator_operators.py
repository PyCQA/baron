#!/usr/bin/python
# -*- coding:Utf-8 -*-


import pytest
from utils import comparison, boolean_operator, ternary_operator, assignment, augmented_assignment
from test_utils import parse_simple, name, binary_operator, unitary_operator, atomtrailers


def test_simple_power():
    "a**b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=""
                          )])

def test_first_space_power():
    "a  **b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', '  ', ''),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=name('b'),
                           first_space="  ",
                           second_space=""
                          )])

def test_second_space_power():
    "a** b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', '', ' '),
           ('NAME', 'b')],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" "
                          )])

def test_spaces_power():
    "a **  b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_power():
    "a **  b   **    c"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**', '   ', '    '),
           ('NAME', 'c')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=binary_operator(
                                                  '**',
                                                  first=name('b'),
                                                  second=name('c'),
                                                  first_space="   ",
                                                  second_space="    "
                                                 ),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_power_spaces():
    "a**  b   **    c"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', '', '  '),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**', '   ', '    '),
           ('NAME', 'c')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=binary_operator(
                                                  '**',
                                                  first=name('b'),
                                                  second=name('c'),
                                                  first_space="   ",
                                                  second_space="    "
                                                 ),
                           first_space="",
                           second_space="  "
                          )])
    "a **b   **    c"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', ''),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**', '   ', '    '),
           ('NAME', 'c')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=binary_operator(
                                                  '**',
                                                  first=name('b'),
                                                  second=name('c'),
                                                  first_space="   ",
                                                  second_space="    "
                                                 ),
                           first_space=" ",
                           second_space=""
                          )])
    "a**b**c"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'c')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=binary_operator(
                                                  '**',
                                                  first=name('b'),
                                                  second=name('c'),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space=""
                          )])

def test_power_factor():
    "a **  +b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('PLUS', '+'),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=unitary_operator('+', name('b'), space=""),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_factor_minus():
    "a **  -b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('MINUS', '-'),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=unitary_operator('-', name('b'), space=""),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_factor_tild():
    "a **  ~b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('TILDE', '~'),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=unitary_operator('~', name('b'), space=""),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_operator_madness():
    "a **  ~+-b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('TILDE', '~'),
           ('PLUS', '+'),
           ('MINUS', '-'),
           ('NAME', 'b')
          ],
          [binary_operator(
                   '**',
                   first=name('a'),
                   second=unitary_operator(
                                           '~',
                                           unitary_operator(
                                                           '+',
                                                           unitary_operator(
                                                                    '-',
                                                                    name('b'),
                                                                    space=""
                                                                   ),
                                                           space=""
                                           ),
                                           space=""
                                          ),
                   first_space=" ",
                   second_space="  "
              )])

def test_power_factor_tild_space():
    "a **  ~ b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_STAR', '**', ' ', '  '),
           ('TILDE', '~', '', ' '),
           ('NAME', 'b')
          ],
          [binary_operator(
                           '**',
                           first=name('a'),
                           second=unitary_operator('~', name('b'), space=" "),
                           first_space=" ",
                           second_space="  "
                          )])

def test_power_trailer():
    "a.b"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
          }])

def test_power_trailer_spaces():
    "a .b"
    "a.  b"
    "a  .   b"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', ' ', ''),
           ('NAME', 'b'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": " ",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
          }])

    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', '', '  '),
           ('NAME', 'b'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "  ",
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
          }])

    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', '   ', '    '),
           ('NAME', 'b'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": "   ",
                    "second_space": "    ",
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
          }])

def test_power_trailers():
    "a.b.c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'c'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "c",
                },
            ],
          }])
    "a.b.c.d.e"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('DOT', '.'),
           ('NAME', 'e'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "c",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "d",
                },
                {
                    "type": "dot",
                    "first_space": "",
                    "second_space": "",
                },
                {
                    "type": "name",
                    "value": "e",
                },
            ],
          }])

def test_power_trailers_space():
    "a . b . c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', ' ', ' '),
           ('NAME', 'b'),
           ('DOT', '.', ' ', ' '),
           ('NAME', 'c'),
          ],
          [{
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_space": " ",
                    "second_space": " ",
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_space": " ",
                    "second_space": " ",
                },
                {
                    "type": "name",
                    "value": "c",
                },
            ],
          }])

def test_power_trailer_power():
    "a.b**c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'c'),
          ],
          [{
            "type": "binary_operator",
            "value": "**",
            "first_space": "",
            "second_space": "",
            "first": {
                "type": "atomtrailers",
                "value": [{
                   "type": "name",
                   "value": "a",
                },{
                   "type": "dot",
                   "first_space": "",
                   "second_space": "",
                },{
                   "type": "name",
                   "value": "b",
                }],
            },
            "second": {
                "type": "name",
                "value": "c",
            }
          }])

def test_power_trailer_call_empty():
    "a()"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_PARENTHESIS', '('),
           ('RIGHT_PARENTHESIS', ')'),
          ],
          [atomtrailers([
                         name('a'),
                         {
                          "type": "call",
                          "first_space": "",
                          "second_space": "",
                          "third_space": "",
                          "value": None,
                         }
                        ])])

def test_power_trailer_call_empty_with_space():
    "a ( )"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_PARENTHESIS', '(', ' ', ' '),
           ('RIGHT_PARENTHESIS', ')'),
          ],
          [atomtrailers([
                         name('a'),
                         {
                          "type": "call",
                          "first_space": " ",
                          "second_space": " ",
                          "third_space": "",
                          "value": None,
                         }
                        ])])

def test_term_mult():
    "a*b"
    parse_simple([
           ('NAME', 'a'),
           ('STAR', '*'),
           ('NAME', 'b'),
          ],
          [binary_operator('*',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_term_mult_first_space():
    "a *b"
    parse_simple([
           ('NAME', 'a'),
           ('STAR', '*', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('*',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_term_mult_second_space():
    "a* b"
    parse_simple([
           ('NAME', 'a'),
           ('STAR', '*', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('*',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_term_mult_spaces():
    "a * b"
    parse_simple([
           ('NAME', 'a'),
           ('STAR', '*', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('*',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_mult_spaces_atomtrailers():
    "a.b * c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('STAR', '*', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('*',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_div():
    "a/b"
    parse_simple([
           ('NAME', 'a'),
           ('SLASH', '/'),
           ('NAME', 'b'),
          ],
          [binary_operator('/',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_term_div_first_space():
    "a /b"
    parse_simple([
           ('NAME', 'a'),
           ('SLASH', '/', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('/',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_term_div_second_space():
    "a/ b"
    parse_simple([
           ('NAME', 'a'),
           ('SLASH', '/', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('/',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_term_div_spaces():
    "a / b"
    parse_simple([
           ('NAME', 'a'),
           ('SLASH', '/', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('/',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_div_spaces_atomtrailers():
    "a.b / c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('SLASH', '/', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('/',
                           first={
                                "type": "atomtrailers",
                                "value": [{
                                    "type": "name",
                                    "value": "a",
                                },{
                                    "type": "dot",
                                    "first_space": "",
                                    "second_space": "",
                                },{
                                   "type": "name",
                                   "value": "b",
                                }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_modulo():
    "a%b"
    parse_simple([
           ('NAME', 'a'),
           ('PERCENT', '%'),
           ('NAME', 'b'),
          ],
          [binary_operator('%',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_term_modulo_first_space():
    "a %b"
    parse_simple([
           ('NAME', 'a'),
           ('PERCENT', '%', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('%',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_term_modulo_second_space():
    "a% b"
    parse_simple([
           ('NAME', 'a'),
           ('PERCENT', '%', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('%',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_term_modulo_spaces():
    "a % b"
    parse_simple([
           ('NAME', 'a'),
           ('PERCENT', '%', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('%',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_modulo_spaces_atomtrailers():
    "a.b % c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('PERCENT', '%', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('%',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_floor_division():
    "a//b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_SLASH', '//'),
           ('NAME', 'b'),
          ],
          [binary_operator('//',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_term_floor_division_first_space():
    "a //b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_SLASH', '//', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('//',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_term_floor_division_second_space():
    "a// b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_SLASH', '//', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('//',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_term_floor_division_spaces():
    "a // b"
    parse_simple([
           ('NAME', 'a'),
           ('DOUBLE_SLASH', '//', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('//',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_term_floor_division_spaces_atomtrailers():
    "a.b // c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOUBLE_SLASH', '//', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('//',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_combine_div_modulo_mult():
    "a/b%c*d"
    parse_simple([
           ('NAME', 'a'),
           ('SLASH', '/'),
           ('NAME', 'b'),
           ('PERCENT', '%'),
           ('NAME', 'c'),
           ('STAR', '*'),
           ('NAME', 'd'),
          ],
          [binary_operator('/',
                           first= name('a'),
                           second=binary_operator('%',
                                  first=name('b'),
                                  second=binary_operator('*',
                                             first=name("c"),
                                             second=name('d'),
                                             first_space="",
                                             second_space="",
                                            ),
                                  first_space="",
                                  second_space="",
                                 ),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_plus():
    "a+b"
    parse_simple([
           ('NAME', 'a'),
           ('PLUS', '+'),
           ('NAME', 'b'),
          ],
          [binary_operator('+',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_add_first_space():
    "a +b"
    parse_simple([
           ('NAME', 'a'),
           ('PLUS', '+', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('+',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_arith_expr_add_second_space():
    "a+ b"
    parse_simple([
           ('NAME', 'a'),
           ('PLUS', '+', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('+',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_arith_expr_add_spaces():
    "a + b"
    parse_simple([
           ('NAME', 'a'),
           ('PLUS', '+', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('+',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_add_spaces_atomtrailers():
    "a.b + c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('PLUS', '+', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('+',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_substract():
    "a-b"
    parse_simple([
           ('NAME', 'a'),
           ('MINUS', '-'),
           ('NAME', 'b'),
          ],
          [binary_operator('-',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_substract_first_space():
    "a -b"
    parse_simple([
           ('NAME', 'a'),
           ('MINUS', '-', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('-',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_arith_expr_substract_second_space():
    "a- b"
    parse_simple([
           ('NAME', 'a'),
           ('MINUS', '-', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('-',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_arith_expr_substract_spaces():
    "a - b"
    parse_simple([
           ('NAME', 'a'),
           ('MINUS', '-', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('-',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_substract_spaces_atomtrailers():
    "a.b - c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('MINUS', '-', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('-',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])


def test_chained_add_substract():
    "a+b-c"
    parse_simple([
           ('NAME', 'a'),
           ('PLUS', '+'),
           ('NAME', 'b'),
           ('MINUS', '-'),
           ('NAME', 'c'),
          ],
          [binary_operator('+',
                           first=name('a'),
                           second=binary_operator('-',
                                                  first=name("b"),
                                                  second=name("c"),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_left_shift():
    "a<<b"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SHIFT', '<<'),
           ('NAME', 'b'),
          ],
          [binary_operator('<<',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_left_shift_first_space():
    "a <<b"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SHIFT', '<<', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('<<',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_arith_expr_left_shift_second_space():
    "a<< b"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SHIFT', '<<', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('<<',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_arith_expr_left_shift_spaces():
    "a << b"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SHIFT', '<<', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('<<',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_left_shift_spaces_atomtrailers():
    "a.b << c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('LEFT_SHIFT', '<<', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('<<',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_right_shift():
    "a>>b"
    parse_simple([
           ('NAME', 'a'),
           ('RIGHT_SHIFT', '>>'),
           ('NAME', 'b'),
          ],
          [binary_operator('>>',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_arith_expr_right_shift_first_space():
    "a >>b"
    parse_simple([
           ('NAME', 'a'),
           ('RIGHT_SHIFT', '>>', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('>>',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_arith_expr_right_shift_second_space():
    "a>> b"
    parse_simple([
           ('NAME', 'a'),
           ('RIGHT_SHIFT', '>>', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('>>',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_arith_expr_right_shift_spaces():
    "a >> b"
    parse_simple([
           ('NAME', 'a'),
           ('RIGHT_SHIFT', '>>', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('>>',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_arith_expr_right_shift_spaces_atomtrailers():
    "a.b >> c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('RIGHT_SHIFT', '>>', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('>>',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_chained_left_right_shift():
    "a<<b>>c"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SHIFT', '<<'),
           ('NAME', 'b'),
           ('RIGHT_SHIFT', '>>'),
           ('NAME', 'c'),
          ],
          [binary_operator('<<',
                           first=name('a'),
                           second=binary_operator('>>',
                                                  first=name("b"),
                                                  second=name("c"),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space="",
                          )])

def test_and_expr():
    "a&b"
    parse_simple([
           ('NAME', 'a'),
           ('AMPER', '&'),
           ('NAME', 'b'),
          ],
          [binary_operator('&',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_and_expr_first_space():
    "a &b"
    parse_simple([
           ('NAME', 'a'),
           ('AMPER', '&', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('&',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_and_expr_second_space():
    "a& b"
    parse_simple([
           ('NAME', 'a'),
           ('AMPER', '&', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('&',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_and_expr_spaces():
    "a & b"
    parse_simple([
           ('NAME', 'a'),
           ('AMPER', '&', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('&',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_and_expr_spaces_atomtrailers():
    "a.b & c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('AMPER', '&', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('&',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_chained_left_and_expr():
    "a&b&c"
    parse_simple([
           ('NAME', 'a'),
           ('AMPER', '&'),
           ('NAME', 'b'),
           ('AMPER', '&'),
           ('NAME', 'c'),
          ],
          [binary_operator('&',
                           first=name('a'),
                           second=binary_operator('&',
                                                  first=name("b"),
                                                  second=name("c"),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space="",
                          )])

def test_xor_expr():
    "a^b"
    parse_simple([
           ('NAME', 'a'),
           ('CIRCUMFLEX', '^'),
           ('NAME', 'b'),
          ],
          [binary_operator('^',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_xor_expr_first_space():
    "a ^b"
    parse_simple([
           ('NAME', 'a'),
           ('CIRCUMFLEX', '^', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('^',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_xor_expr_second_space():
    "a^ b"
    parse_simple([
           ('NAME', 'a'),
           ('CIRCUMFLEX', '^', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('^',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_xor_expr_spaces():
    "a ^ b"
    parse_simple([
           ('NAME', 'a'),
           ('CIRCUMFLEX', '^', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('^',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_xor_expr_spaces_atomtrailers():
    "a.b ^ c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('CIRCUMFLEX', '^', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('^',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_chained_left_xor_expr():
    "a^b^c"
    parse_simple([
           ('NAME', 'a'),
           ('CIRCUMFLEX', '^'),
           ('NAME', 'b'),
           ('CIRCUMFLEX', '^'),
           ('NAME', 'c'),
          ],
          [binary_operator('^',
                           first=name('a'),
                           second=binary_operator('^',
                                                  first=name("b"),
                                                  second=name("c"),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space="",
                          )])

def test_expr():
    "a|b"
    parse_simple([
           ('NAME', 'a'),
           ('VBAR', '|'),
           ('NAME', 'b'),
          ],
          [binary_operator('|',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space="",
                          )])

def test_expr_first_space():
    "a |b"
    parse_simple([
           ('NAME', 'a'),
           ('VBAR', '|', ' ', ''),
           ('NAME', 'b'),
          ],
          [binary_operator('|',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space="",
                          )])

def test_expr_second_space():
    "a| b"
    parse_simple([
           ('NAME', 'a'),
           ('VBAR', '|', '', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('|',
                           first=name('a'),
                           second=name('b'),
                           first_space="",
                           second_space=" ",
                          )])

def test_expr_spaces():
    "a | b"
    parse_simple([
           ('NAME', 'a'),
           ('VBAR', '|', ' ', ' '),
           ('NAME', 'b'),
          ],
          [binary_operator('|',
                           first=name('a'),
                           second=name('b'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_expr_spaces_atomtrailers():
    "a.b | c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('VBAR', '|', ' ', ' '),
           ('NAME', 'c'),
          ],
          [binary_operator('|',
                           first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                           second=name('c'),
                           first_space=" ",
                           second_space=" ",
                          )])

def test_chained_left_expr():
    "a|b|c"
    parse_simple([
           ('NAME', 'a'),
           ('VBAR', '|'),
           ('NAME', 'b'),
           ('VBAR', '|'),
           ('NAME', 'c'),
          ],
          [binary_operator('|',
                           first=name('a'),
                           second=binary_operator('|',
                                                  first=name("b"),
                                                  second=name("c"),
                                                  first_space="",
                                                  second_space=""
                                                 ),
                           first_space="",
                           second_space="",
                          )])

comparison_tokens = (
    ('LESS', '<'),
    ('GREATER', '>'),
    ('EQUAL_EQUAL', '=='),
    ('LESS_EQUAL', '<='),
    ('GREATER_EQUAL', '>='),
    ('LESS_GREATER', '<>'),
    ('NOT_EQUAL', '!='),
    ('IN', 'in'),
    ('IS', 'is'),
)

def test_comparison():
    "a<b"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value),
               ('NAME', 'b'),
              ],
              [comparison(value,
                          first=name('a'),
                          second=name('b'),
                          first_space="",
                          second_space="",
                         )])

def test_comparison_first_space():
    "a <b"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, ' ', ''),
               ('NAME', 'b'),
              ],
              [comparison(value,
                          first=name('a'),
                          second=name('b'),
                          first_space=" ",
                          second_space="",
                         )])

def test_comparison_second_space():
    "a< b"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, '', ' '),
               ('NAME', 'b'),
              ],
              [comparison(value,
                          first=name('a'),
                          second=name('b'),
                          first_space="",
                          second_space=" ",
                         )])

def test_comparison_spaces():
    "a < b"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, ' ', ' '),
               ('NAME', 'b'),
              ],
              [comparison(value,
                          first=name('a'),
                          second=name('b'),
                          first_space=" ",
                          second_space=" ",
                         )])

def test_comparison_spaces_atomtrailers():
    "a.b < c"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               ('DOT', '.'),
               ('NAME', 'b'),
               (token_name, value, ' ', ' '),
               ('NAME', 'c'),
              ],
              [comparison(value,
                          first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                          second=name('c'),
                          first_space=" ",
                          second_space=" ",
                         )])

def test_chained_comparison():
    "a<b<c"
    for token_name, value in comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value),
               ('NAME', 'b'),
               (token_name, value),
               ('NAME', 'c'),
              ],
              [comparison(value,
                          first=name('a'),
                          second=comparison(value,
                                            first=name("b"),
                                            second=name("c"),
                                            first_space="",
                                            second_space=""
                                           ),
                          first_space="",
                          second_space="",
                         )])

advanced_comparison_tokens = (
    (('NOT', 'not', '', ' '), ('IN', 'in')),
    (('IS', 'is', '', ' '), ('NOT', 'not')),
)

def test_advanced_comparison():
    "a<b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, "", after_space),
               (token_name2, value2),
               ('NAME', 'b'),
              ],
              [comparison(value + " " + value2,
                          first=name('a'),
                          second=name('b'),
                          first_space="",
                          second_space="",
                          middle_space=after_space,
                         )])

def test_advanced_comparison_first_space():
    "a <b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, " ", after_space),
               (token_name2, value2),
               ('NAME', 'b'),
              ],
              [comparison(value + " " + value2,
                          first=name('a'),
                          second=name('b'),
                          first_space=" ",
                          second_space="",
                          middle_space=after_space,
                         )])

def test_advanced_comparison_second_space():
    "a< b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, "", after_space),
               (token_name2, value2, "", " "),
               ('NAME', 'b'),
              ],
              [comparison(value + " " + value2,
                          first=name('a'),
                          second=name('b'),
                          first_space="",
                          second_space=" ",
                          middle_space=after_space,
                         )])

def test_advanced_comparison_spaces():
    "a < b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, " ", after_space),
               (token_name2, value2, "", " "),
               ('NAME', 'b'),
              ],
              [comparison(value + " " + value2,
                          first=name('a'),
                          second=name('b'),
                          first_space=" ",
                          second_space=" ",
                          middle_space=after_space,
                         )])

def test_advanced_comparison_spaces_atomtrailers():
    "a.b < c"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               ('DOT', '.'),
               ('NAME', 'b'),
               (token_name, value, " ", after_space),
               (token_name2, value2, "", " "),
               ('NAME', 'c'),
              ],
              [comparison(value + " " + value2,
                          first={
                            "type": "atomtrailers",
                            "value": [{
                                "type": "name",
                                "value": "a",
                            },{
                                "type": "dot",
                                "first_space": "",
                                "second_space": "",
                            },{
                               "type": "name",
                               "value": "b",
                            }],
                           },
                          second=name('c'),
                          first_space=" ",
                          second_space=" ",
                          middle_space=after_space,
                         )])

def test_chained_advanced_comparison():
    "a<b<c"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, "", after_space),
               (token_name2, value2),
               ('NAME', 'b'),
               (token_name, value, "", after_space),
               (token_name2, value2),
               ('NAME', 'c'),
              ],
              [comparison(value + " " + value2,
                          first=name('a'),
                          second=comparison(value + " " + value2,
                                            first=name("b"),
                                            second=name("c"),
                                            first_space="",
                                            second_space="",
                                            middle_space=after_space,
                                           ),
                          first_space="",
                          second_space="",
                          middle_space=after_space,
                         )])

def test_not():
    "not a"
    parse_simple([
           ('NOT', 'not', '', ' '),
           ('NAME', 'a'),
          ],
          [unitary_operator(
                            'not',
                            target=name('a'),
                            space=" ",
                           )])

def test_not_not():
    "not not a"
    parse_simple([
           ('NOT', 'not', '', ' '),
           ('NOT', 'not', '', ' '),
           ('NAME', 'a'),
          ],
          [unitary_operator(
                            'not',
                            target=unitary_operator(
                                                    'not',
                                                    target=name('a'),
                                                    space=" ",
                            ),
                            space=" ",
                           )])

def test_and():
    "a and b"
    parse_simple([
           ('NAME', 'a'),
           ('AND', 'and', ' ', ' '),
           ('NAME', 'b'),
          ],
          [boolean_operator(
                            'and',
                            first=name('a'),
                            second=name('b'),
                            first_space=" ",
                            second_space=" ",
                           )])

def test_and_and():
    "a and b and c"
    parse_simple([
           ('NAME', 'a'),
           ('AND', 'and', ' ', ' '),
           ('NAME', 'b'),
           ('AND', 'and', ' ', ' '),
           ('NAME', 'c'),
          ],
          [boolean_operator(
                            'and',
                            first=name('a'),
                            second=boolean_operator(
                                                    'and',
                                                    first=name('b'),
                                                    second=name('c'),
                                                    first_space=" ",
                                                    second_space=" ",
                            ),
                            first_space=" ",
                            second_space=" ",
                           )])

def test_or():
    "a or b"
    parse_simple([
           ('NAME', 'a'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'b'),
          ],
          [boolean_operator(
                            'or',
                            first=name('a'),
                            second=name('b'),
                            first_space=" ",
                            second_space=" ",
                           )])

def test_or_or():
    "a or b or c"
    parse_simple([
           ('NAME', 'a'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'b'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'c'),
          ],
          [boolean_operator(
                            'or',
                            first=name('a'),
                            second=boolean_operator(
                                                    'or',
                                                    first=name('b'),
                                                    second=name('c'),
                                                    first_space=" ",
                                                    second_space=" ",
                            ),
                            first_space=" ",
                            second_space=" ",
                           )])

def test_or_and():
    "a or b and c"
    parse_simple([
           ('NAME', 'a'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'b'),
           ('AND', 'and', ' ', ' '),
           ('NAME', 'c'),
          ],
          [boolean_operator(
                            'or',
                            first=name('a'),
                            second=boolean_operator(
                                                    'and',
                                                    first=name('b'),
                                                    second=name('c'),
                                                    first_space=" ",
                                                    second_space=" ",
                            ),
                            first_space=" ",
                            second_space=" ",
                           )])


def test_ternary_operator():
    "a if b else c"
    parse_simple([
           ('NAME', 'a'),
           ('IF', 'if', ' ', ' '),
           ('NAME', 'b'),
           ('ELSE', 'else', ' ', ' '),
           ('NAME', 'c'),
          ],
          [ternary_operator(
                            name('b'),
                            first=name('a'),
                            second=name('c'),
                            first_space=" ",
                            second_space=" ",
                            third_space=" ",
                            forth_space=" ",
                           )])

def test_assignment():
    "a = b"
    parse_simple([
           ('NAME', 'a'),
           ('EQUAL', '=', ' ', ' '),
           ('NAME', 'b'),
          ],
          [assignment(
                      value=name('b'),
                      target=name('a'),
                      first_space=" ",
                      second_space=" ",
                     )])

def test_assignment_assignment():
    "a = b = c"
    parse_simple([
           ('NAME', 'a'),
           ('EQUAL', '=', ' ', ' '),
           ('NAME', 'b'),
           ('EQUAL', '=', ' ', ' '),
           ('NAME', 'c'),
          ],
          [assignment(
                      value=assignment(
                                       value=name('c'),
                                       target=name('b'),
                                       first_space=" ",
                                       second_space=" ",
                                      ),
                      target=name('a'),
                      first_space=" ",
                      second_space=" ",
                     )])

augmented_assignment_tokens = (
    ('PLUS_EQUAL', '+='),
    ('MINUS_EQUAL', '-='),
    ('STAR_EQUAL', '*='),
    ('SLASH_EQUAL', '/='),
    ('PERCENT_EQUAL', '%='),
    ('AMPER_EQUAL', '&='),
    ('VBAR_EQUAL', '|='),
    ('CIRCUMFLEX_EQUAL', '^='),
    ('LEFT_SHIFT_EQUAL', '<<='),
    ('RIGHT_SHIFT_EQUAL', '>>='),
    ('DOUBLE_STAR_EQUAL', '**='),
    ('DOUBLE_SLASH_EQUAL', '//='),
)

def test_augmented_assignment():
    "a += b"
    for token_name, value in augmented_assignment_tokens:
        parse_simple([
               ('NAME', 'a'),
               (token_name, value, ' ', ' '),
               ('NAME', 'b'),
              ],
              [augmented_assignment(
                                    operator=value[:-1],
                                    value=name('b'),
                                    target=name('a'),
                                    first_space=" ",
                                    second_space=" ",
                                   )])

def test_augmented_assignment_augmented_assignment():
    "a += b"
    for token_name, value in augmented_assignment_tokens:
        with pytest.raises(Exception):
            parse_simple([
                   ('NAME', 'a'),
                   (token_name, value, ' ', ' '),
                   ('NAME', 'b'),
                   (token_name, value, ' ', ' '),
                   ('NAME', 'c'),
                  ],
                  [augmented_assignment(
                                operator=value[:-1],
                                value=augmented_assignment(
                                                       operator=value[:-1],
                                                       value=name('c'),
                                                       target=name('b'),
                                                       first_space=" ",
                                                       second_space=" ",
                                                      ),
                                target=name('a'),
                                first_space=" ",
                                second_space=" ",
                               )])

def test_expr_comma_list():
    "a or b,c+d"
    parse_simple([
           ('NAME', 'a'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('NAME', 'c'),
           ('PLUS', '+'),
           ('NAME', 'd'),
          ],
          [{
            "type": "tuple",
            "with_parenthesis": False,
            "first_space": "",
            "second_space": "",
            "value": [
                   boolean_operator(
                                    'or',
                                    first=name('a'),
                                    second=name('b'),
                                    first_space=" ",
                                    second_space=" ",
                                   ),
                   {"type": "comma", "first_space": "", "second_space": ""},
                   binary_operator(
                                   '+',
                                   first=name('c'),
                                   second=name('d'),
                                   first_space="",
                                   second_space="",
                                  )
                  ],
           }
                 ])

def test_expr_comma_list_3_items():
    "a or b,c+d,e"
    parse_simple([
           ('NAME', 'a'),
           ('OR', 'or', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('NAME', 'c'),
           ('PLUS', '+'),
           ('NAME', 'd'),
           ('COMMA', ','),
           ('NAME', 'e'),
          ],
          [{
            "type": "tuple",
            "with_parenthesis": False,
            "first_space": "",
            "second_space": "",
            "value": [boolean_operator(
                                    'or',
                                    first=name('a'),
                                    second=name('b'),
                                    first_space=" ",
                                    second_space=" ",
                                   ),
                   {"type": "comma", "first_space": "", "second_space": ""},
                   binary_operator(
                                   '+',
                                   first=name('c'),
                                   second=name('d'),
                                   first_space="",
                                   second_space="",
                                  ),
                   {"type": "comma", "first_space": "", "second_space": ""},
                   name('e'),
                  ],
            }])

def test_implicit_tuple_space():
    "a, b , c"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'c'),
          ],
          [{
            "type": "tuple",
            "with_parenthesis": False,
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
               "first_space": " ",
               "second_space": " ",
            },{
                "type": "name",
                "value": "c",
            }],
           }])

def test_implicit_tuple_one_item():
    "a ,"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ''),
          ],
          [{
            "type": "tuple",
            "with_parenthesis": False,
            "first_space": "",
            "second_space": "",
            "value": [{
                     "type": "name",
                     "value": "a",
                   },{
                      "type": "comma",
                      "first_space": " ",
                      "second_space": "",
                   }]
           }])

def test_implicit_tuple_trailing_comma():
    "a, b ,"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', ''),
          ],
          [{
            "type": "tuple",
            "with_parenthesis": False,
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
                      "first_space": " ",
                      "second_space": "",
                   }]
           }])

def test_subscript_ellipsis():
    "a[...]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "ellipsis",
                   "first_space": "",
                   "second_space": "",
               }
            }]
           }])

def test_subscript_ellipsis_space():
    "a[. .  .   ]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('DOT', '.', '', ' '),
           ('DOT', '.', '', '  '),
           ('DOT', '.'),
           ('RIGHT_SQUARE_BRACKET', ']', '   ', ''),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "   ",
               "value": {
                   "type": "ellipsis",
                   "first_space": " ",
                   "second_space": "  ",
               }
            }]
           }])

def test_subscript_test():
    "a[b]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('NAME', 'b'),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "name",
                   "value": "b",
               }
            }]
           }])

def test_subscript_slice_empty():
    "a[:]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('COLON', ':'),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "slice",
                   "lower": None,
                   "upper": None,
                   "step": None,
                   "has_two_colons": False,
                   "first_space": "",
                   "second_space": "",
                   "third_space": "",
                   "forth_space": "",
               }
            }]
           }])

def test_subscript_slice_empty_both():
    "a[: :]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('COLON', ':', '', ' '),
           ('COLON', ':'),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "slice",
                   "lower": None,
                   "upper": None,
                   "step": None,
                   "has_two_colons": True,
                   "first_space": "",
                   "second_space": " ",
                   "third_space": "",
                   "forth_space": "",
               }
            }]
           }])

def test_subscript_slice_one():
    "a[b :]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('NAME', 'b'),
           ('COLON', ':', ' ', ''),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "slice",
                   "lower": {
                        "type": "name",
                        "value": "b",
                   },
                   "upper": None,
                   "step": None,
                   "has_two_colons": False,
                   "first_space": " ",
                   "second_space": "",
                   "third_space": "",
                   "forth_space": "",
               }
            }]
           }])

def test_subscript_slice_both_one():
    "a[b : : ]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('NAME', 'b'),
           ('COLON', ':', ' ', ' '),
           ('COLON', ':', '', ''),
           ('RIGHT_SQUARE_BRACKET', ']', ' ', ''),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": " ",
               "value": {
                   "type": "slice",
                   "lower": {
                        "type": "name",
                        "value": "b",
                   },
                   "upper": None,
                   "step": None,
                   "has_two_colons": True,
                   "first_space": " ",
                   "second_space": " ",
                   "third_space": "",
                   "forth_space": "",
               }
            }]
           }])

def test_subscript_slice_upper():
    "a[:b]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('COLON', ':'),
           ('NAME', 'b'),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "slice",
                   "upper": {
                        "type": "name",
                        "value": "b",
                   },
                   "lower": None,
                   "step": None,
                   "has_two_colons": False,
                   "first_space": "",
                   "second_space": "",
                   "third_space": "",
                   "forth_space": "",
               }
            }]
           }])

def test_subscript_slice_upper_both():
    "a[:b :]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('COLON', ':'),
           ('NAME', 'b'),
           ('COLON', ':', ' ', ''),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [{
            "type": "atomtrailers",
            "value": [{
               "type": "name",
               "value": "a",
            },{
               "type": "getitem",
               "first_space": "",
               "second_space": "",
               "value": {
                   "type": "slice",
                   "upper": {
                        "type": "name",
                        "value": "b",
                   },
                   "lower": None,
                   "step": None,
                   "has_two_colons": True,
                   "first_space": "",
                   "second_space": "",
                   "third_space": " ",
                   "forth_space": "",
               }
            }]
           }])

### trailer: '.' [SPACE] NAME
### trailer: '[' [SPACE] ']'
### trailer: '[' [SPACE] subscriptlist [SPACE] ']'
### trailer: '(' [SPACE] ')'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# -

# subscriptlist: subscript
# subscriptlist: subscript [SPACE] [',']
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)*
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)* [SPACE] [',']

# -

# subscript: test
### subscript: '.' [SPACE] '.' [SPACE] '.'
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
