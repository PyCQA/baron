#!/usr/bin/python
# -*- coding:Utf-8 -*-

import pytest
from utils import (comparison, boolean_operator, ternary_operator, assignment,
                   augmented_assignment, tuple_, return_, yield_)
from test_utils import (parse_simple, space, inteu, endl, name, string, importeu,
                        dotted_as_name, dotted_name, dot, comma, from_import,
                        name_as_name, left_parenthesis, right_parenthesis,
                        star, binary_operator, unitary_operator, atomtrailers,
                        getitem, call, parse_multi, semicolon)

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

def test_simple_import():
    "import   pouet"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet')],
          [importeu([
                     dotted_as_name(dotted_name([name("pouet")]))
                    ],
                    space="  ")])

def test_import_basic_dot():
    "import   pouet.blob"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [importeu([
                     dotted_as_name(dotted_name([
                                                 name("pouet"),
                                                 dot(),
                                                 name("blob")
                                                ])
                                   )
                    ],
                    space="  "
                   )])

def test_import_more_dot():
    "import   pouet.blob .plop"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [importeu([
                     dotted_as_name(dotted_name([
                                                 name("pouet"),
                                                 dot(),
                                                 name("blob"),
                                                 space(" "),
                                                 dot(),
                                                 name("plop")
                                                ])
                                   )
                    ],
                    space="  ")])

def test_import_as():
    "import   pouet as  b"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'b')],
          [importeu([
                     dotted_as_name(dotted_name([name("pouet")]),
                                    before_space=" ",
                                    as_=True,
                                    after_space="  ",
                                    target='b')
                    ],
                    space="  "
                   )])

def test_import_a_b():
    "import a, b"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')],
          [importeu([
                     dotted_as_name(dotted_name([name('a')])),
                     comma(),
                     space(),
                     dotted_as_name(dotted_name([name('b')]))
                    ],
                    space=" ")])

def test_import_a_b_as_c():
    "import a, b.d as  c"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [importeu([
                     dotted_as_name(dotted_name([name('a')])),
                     comma(),
                     space(),
                     dotted_as_name(
                                    dotted_name([
                                                 name('b'),
                                                 dot(),
                                                 name('d')
                                                ]),
                                    as_=True,
                                    before_space=" ",
                                    after_space="  ",
                                    target="c"
                                   )
                    ],
                    space=" "
                   )])

def test_import_a_b_c_d():
    "import a, b, c, d"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [importeu([
                     dotted_as_name(dotted_name([name('a')])),
                     comma(),
                     space(),
                     dotted_as_name(dotted_name([name('b')])),
                     comma(),
                     space(),
                     dotted_as_name(dotted_name([name('c')])),
                     comma(),
                     space(),
                     dotted_as_name(dotted_name([name('d')]))
                    ],
                    space=" "
                   )])

def test_from_a_import_b():
    "from a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_a_dot_c_import_b():
    "from a.C import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')],
          [from_import(
                       dotted_name([
                                    name('a'),
                                    dot(),
                                    name('c')
                                   ]),
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_a_dot_c_import_b_d():
    "from a.c import b, d"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [from_import(
                       dotted_name([
                                    name('a'),
                                    dot(),
                                    name('c')
                                   ]),
                       targets=[
                                name_as_name('b'),
                                comma(),
                                space(),
                                name_as_name('d')
                               ]
                      )])

def test_from_a_import_b_as_d():
    "from a import b as d"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b'),
           ('AS', 'as', ' ', ' '),
           ('NAME', 'd')
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                name_as_name(
                                             'b',
                                             as_=True,
                                             before_space=" ",
                                             after_space=" ",
                                             target="d"
                                            )
                               ]
                      )])

def test_from_a_import_parenthesis_b():
    "from a import (b)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                left_parenthesis(),
                                name_as_name('b'),
                                right_parenthesis()
                               ]
                      )])

def test_from_a_import_parenthesis_b_without_space():
    "from a import(b)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ''),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                left_parenthesis(),
                                name_as_name('b'),
                                right_parenthesis()
                               ],
                       after_space=""
                      )])

def test_from_a_import_parenthesis_b_comma():
    "from a import (b,)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                left_parenthesis(),
                                name_as_name('b'),
                                comma(),
                                right_parenthesis()
                               ]
                      )])

def test_from_a_import_parenthesis_b_space():
    "from a import (b )"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                left_parenthesis(),
                                name_as_name('b'),
                                space(),
                                right_parenthesis()
                               ]
                      )])

def test_from_a_import_star():
    "from a import *"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('STAR', '*')
          ],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                star()
                               ]
                      )])

def test_from_a_import_star_without_space():
    "from a import*"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ''),
           ('STAR', '*')],
          [from_import(
                       dotted_name([
                                    name('a')
                                   ]),
                       targets=[
                                star()
                               ],
                       after_space=""
                      )])

def test_from_dot_a_import_b():
    "from .a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       dotted_name([
                                    dot(),
                                    name('a')
                                   ]),
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_dot_dot_dot_a_import_b():
    "from ...a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       dotted_name([
                                    dot(),
                                    dot(),
                                    dot(),
                                    name('a')
                                   ]),
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_no_space_dot_a_import_b():
    "from.a import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(dotted_name([
                                    dot(),
                                    name('a')
                                   ]),
                       targets=[
                                name_as_name('b')
                               ],
                       before_space=""
                      )])

def test_from_dot_import_b():
    "from . import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       dotted_name([
                                    dot()
                                   ]),
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_dot_no_space_import_b():
    "from .import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'b')
          ],
          [from_import(dotted_name([
                                    dot()
                                   ]),
                       targets=[
                                name_as_name('b')
                               ],
                       middle_space=""
                      )])

def test_from_no_space_dot_import_b():
    "from. import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       dotted_name([
                                    dot()
                                   ]),
                       targets=[
                                name_as_name('b')
                               ],
                       before_space=""
                      )])

def test_from_no_space_dot_no_sapceimport_b():
    "from.import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'b')],
          [from_import(dotted_name([
                                    dot()
                                   ]),
                       targets=[
                                name_as_name('b')
                               ],
                       middle_space="",
                       before_space=""
                      )])

# TODO: 'from. .import*

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
          [atomtrailers([
                  name('a'),
                  dot(),
                  name('b')
                 ]
                )])

def test_power_trailer_spaces():
    "a .b"
    "a.  b"
    "a  .   b"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', ' ', ''),
           ('NAME', 'b'),
          ],
          [atomtrailers([
                  name('a'),
                  space(),
                  dot(),
                  name('b')
                 ]
                )])

    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', '', '  '),
           ('NAME', 'b'),
          ],
          [atomtrailers([
                  name('a'),
                  dot(),
                  space("  "),
                  name('b')
                 ]
                )])

    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', '   ', '    '),
           ('NAME', 'b'),
          ],
          [atomtrailers([
                  name('a'),
                  space("   "),
                  dot(),
                  space("    "),
                  name('b')
                 ]
                )])

def test_power_trailers():
    "a.b.c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'c'),
          ],
          [atomtrailers([
                  name('a'),
                  dot(),
                  name('b'),
                  dot(),
                  name('c')
                 ]
                )])
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
          [atomtrailers([
                  name('a'),
                  dot(),
                  name('b'),
                  dot(),
                  name('c'),
                  dot(),
                  name('d'),
                  dot(),
                  name('e'),
                 ]
                )])

def test_power_trailers_space():
    "a . b . c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.', ' ', ' '),
           ('NAME', 'b'),
           ('DOT', '.', ' ', ' '),
           ('NAME', 'c'),
          ],
          [atomtrailers([
                  name('a'),
                  space(),
                  dot(),
                  space(),
                  name('b'),
                  space(),
                  dot(),
                  space(),
                  name('c')
                 ]
                )])

def test_power_trailer_power():
    "a.b**c"
    parse_simple([
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'b'),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'c'),
          ],
          [binary_operator(
                           '**',
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b')
                                              ]),
                           second=name('c'),
                           first_space="",
                           second_space="",
                          )])

def test_power_trailer_getitem_empty():
    "a[]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '['),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [atomtrailers([
                         name('a'),
                         getitem(),
                        ])])

def test_power_trailer_getitem_empty_with_space():
    "a [ ]"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_SQUARE_BRACKET', '[', ' ', ' '),
           ('RIGHT_SQUARE_BRACKET', ']'),
          ],
          [atomtrailers([
                         name('a'),
                         space(),
                         getitem(
                                 first_space=" "
                         ),
                        ])])

def test_power_trailer_call_empty():
    "a()"
    parse_simple([
           ('NAME', 'a'),
           ('LEFT_PARENTHESIS', '('),
           ('RIGHT_PARENTHESIS', ')'),
          ],
          [atomtrailers([
                         name('a'),
                         call(),
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
                         space(),
                         call(
                              first_space=" "
                         ),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                           first=atomtrailers([
                                               name('a'),
                                               dot(),
                                               name('b'),
                                              ]),
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
                          first=atomtrailers([
                                              name('a'),
                                              dot(),
                                              name('b'),
                                             ]),
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
                          first=atomtrailers([
                                              name('a'),
                                              dot(),
                                              name('b'),
                                             ]),
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
          [tuple_([
                   boolean_operator(
                                    'or',
                                    first=name('a'),
                                    second=name('b'),
                                    first_space=" ",
                                    second_space=" ",
                                   ),
                   comma(),
                   binary_operator(
                                   '+',
                                   first=name('c'),
                                   second=name('d'),
                                   first_space="",
                                   second_space="",
                                  )
                  ],
                  with_parenthesis=False,
                 )])

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
          [tuple_([
                   boolean_operator(
                                    'or',
                                    first=name('a'),
                                    second=name('b'),
                                    first_space=" ",
                                    second_space=" ",
                                   ),
                   comma(),
                   binary_operator(
                                   '+',
                                   first=name('c'),
                                   second=name('d'),
                                   first_space="",
                                   second_space="",
                                  ),
                   comma(),
                   name('e'),
                  ],
                  with_parenthesis=False,
                 )])

def test_implicit_tuple_space():
    "a, b , c"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', ' '),
           ('NAME', 'c'),
          ],
          [tuple_([
                   name('a'),
                   comma(),
                   space(),
                   name('b'),
                   space(),
                   comma(),
                   space(),
                   name('c'),
                  ],
                  with_parenthesis=False,
                 )])

def test_implicit_tuple_one_item():
    "a ,"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', ' ', ''),
          ],
          [tuple_([
                   name('a'),
                   space(),
                   comma(),
                  ],
                  with_parenthesis=False,
                 )])

def test_implicit_tuple_trailing_comma():
    "a, b ,"
    parse_simple([
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', ' ', ''),
          ],
          [tuple_([
                   name('a'),
                   comma(),
                   space(),
                   name('b'),
                   space(),
                   comma(),
                  ],
                  with_parenthesis=False,
                 )])

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

# XXX finish tuples
# too long time I haven't coded on this
# don't see the difference between tuple and () with a comma in it

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

### atom: '(' ')'
### atom: '(' SPACE ')'
# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'

# testlist_comp: test
# testlist_comp: test [SPACE] comp_for
# testlist_comp: test ([SPACE] ',' [SPACE] test)*
# testlist_comp: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# test: lambdef
### test: or_test
### test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]

# lambdef: 'lambda' [SPACE] ':' [SPACE] test
# lambdef: 'lambda' [SPACE] [varargslist] [SPACE] ':' [SPACE] test

# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# exprlist: expr
# exprlist: expr [SPACE] [',']
# exprlist: expr ([SPACE] ',' [SPACE] expr)*
# exprlist: expr ([SPACE] ',' [SPACE] expr)* [SPACE] [',']

### expr: xor_expr
### expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*

### or_test: and_test
### or_test: and_test (SPACE 'or' SPACE and_test)*

# comp_iter: comp_if
# comp_iter: comp_for

# comp_if: 'if' SPACE old_test
# comp_if: 'if' SPACE old_test [SPACE comp_iter]

# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# old_test: or_test
# old_test: old_lambdef

# old_lambdef: 'lambda' [SPACE] ':' [SPACE] old_test
# old_lambdef: 'lambda' SPACE [varargslist] [SPACE] ':' [SPACE] old_test

# ---------------------

### file_input: ([SPACE] NEWLINE | stmt)* [SPACE] ENDMARKER

### stmt: simple_stmt
# stmt: compound_stmt

### simple_stmt: small_stmt [SPACE] NEWLINE
### simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
### simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
### simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

### expr_stmt: testlist
### expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
### -> assign(testlist, testlist)
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# -> assign(testlist, testlist)
# expr_stmt: testlist augassign yield_expr
# -> augassign(testlist, testlist)
### expr_stmt: testlist augassign testlist
### -> augassign(testlist, testlist)

# test: lambdef
### test: or_test
### test: or_test [SPACE -> 'if' <- SPACE or_test SPACE -> 'else' <- SPACE test]
### -> ternaryOp(or_test, or_test, test)

### trailer: '.' [SPACE] NAME
### trailer: '[' [SPACE] ']'
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
### trailer: '(' [SPACE] ')'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# -> tuple([values])
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
# -> ???(yieldexpr) a("yield a") == a("(yield a)"))
# atom: '[' [SPACE] [listmaker] [SPACE] ']'
# -> list([values])
# atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# -> dict(zip([keys], [values]))
# atom: '`' [SPACE] testlist1 [SPACE] '`'
# -> repr([testlist1])
### atom: NAME
### atom: NUMBER
# all sort of numbers!
### atom: STRING+
