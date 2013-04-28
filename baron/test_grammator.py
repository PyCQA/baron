#!/usr/bin/python
# -*- coding:Utf-8 -*-

import pytest
from utils import (comparison, boolean_operator, ternary_operator, assignment,
                   augmented_assignment, tuple_)
from test_utils import (parse, space, inteu, endl, name, string, importeu,
                        dotted_as_name, dotted_name, dot, comma, from_import,
                        name_as_name, left_parenthesis, right_parenthesis,
                        star, binary_operator, unitary_operator, atomtrailers,
                        getitem, call)

def test_empty():
    ""
    parse([

    ], [])

def test_space():
    "   "
    parse([
           ('SPACE', '   ')],
          [space("   ")])

def test_int():
    "1"
    parse([
           ('INT', '1')],
          [inteu("1")])

def test_endl():
    "\n"
    parse([
           ('ENDL', '\n')],
          [endl("\n", before_space="")])

def test_name():
    "a"
    parse([
           ('NAME', 'a')],
          [name("a")])

def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    parse([
           ('STRING', '"pouet pouet"')],
          [string('"pouet pouet"')])
    parse([
           ('STRING', '"""pouet pouet"""')],
          [string('"""pouet pouet"""')])

def test_simple_import():
    "import   pouet"
    parse([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet')],
          [importeu([
                     dotted_as_name(dotted_name([name("pouet")]))
                    ],
                    space="  ")])

def test_import_basic_dot():
    "import   pouet.blob"
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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

    parse([
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

    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
        parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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
    parse([
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


def test_ternary_operator():
    "a if b else c"
    parse([
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
    parse([
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
    "a = b"
    parse([
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
        parse([
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
            parse([
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
    parse([
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
    parse([
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
    parse([
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


# stmt: simple_stmt
# simple_stmt: small_stmt [SPACE] NEWLINE
### small_stmt: expr_stmt
### expr_stmt: testlist
### testlist: test
### test: or_test
### or_test: and_test
### and_test: not_test
### not_test: comparison
### comparison: expr
### expr: xor_expr
### xor_expr: and_expr
### and_expr: shift_expr
### shift_expr: arith_expr
### arith_expr: term
### term: factor
### factor: power
### power: atom

# stmt: simple_stmt
# stmt: compound_stmt

# simple_stmt: small_stmt [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

### small_stmt: expr_stmt
# small_stmt: print_stmt
# small_stmt: del_stmt
# small_stmt: pass_stmt
# small_stmt: flow_stmt
# small_stmt: import_stmt
# small_stmt: global_stmt
# small_stmt: exec_stmt
# small_stmt: assert_stmt

### expr_stmt: testlist
### expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
### -> assign(testlist, testlist)
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# -> assign(testlist, testlist)
# expr_stmt: testlist augassign yield_expr
# -> augassign(testlist, testlist)
### expr_stmt: testlist augassign testlist
### -> augassign(testlist, testlist)

### augassign: '+='
### augassign: '-='
### augassign: '*='
### augassign: '/='
### augassign: '%='
### augassign: '&='
### augassign: '|='
### augassign: '^='
### augassign: '<<='
### augassign: '>>='
### augassign: '**='
### augassign: '//='

### testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']
# -> tuple([...])

# test: lambdef
### test: or_test
### test: or_test [SPACE -> 'if' <- SPACE or_test SPACE -> 'else' <- SPACE test]
### -> ternaryOp(or_test, or_test, test)

### or_test: and_test
### or_test: and_test (SPACE 'or' SPACE and_test)*
### -> boolOP('or', not_test, not_test)

### and_test: not_test
### and_test: not_test (SPACE 'and' SPACE not_test)*
### -> boolOP('and', not_test, not_test)

### not_test: comparison
### not_test: 'not' SPACE not_test
### -> unitaryOp('not', not_test)

### comparison: expr
### -> expr
### comparison: expr (comp_op expr)*
### -> comparison(comp_or, expr, expr)

### comp_op: '<'
### comp_op: '>'
### comp_op: '=='
### comp_op: '>='
### comp_op: '<='
### comp_op: '<>'
### comp_op: '!='
### comp_op: 'in'
### comp_op: 'not' SPACE 'in'
### comp_op: 'is'
### comp_op: 'is' SPACE 'not'
### -> comp_op

### expr: xor_expr
### expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*
### -> binop('|', term, term)

### xor_expr: and_expr
### xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*
### -> binop('^', term, term)

### and_expr: shift_expr
### and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*
### -> binop('&', term, term)

### shift_expr: arith_expr
### shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*
### -> binop(('<<'|'>>'), term, term)

### arith_expr: term
### -> term
### arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*
### -> binop(('+'|'-'), term, term)

### term: factor
### -> factor
### term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*
### -> binop(('*'|'/'|'%'|'//'), factor, factor)

### factor: ('+'|'-'|'~') [SPACE] factor
### -> uniatryop(('+'|'-'|'~'), factor)
### factor: power
### -> power

### power: atom
### -> atom
### power: atom [SPACE] trailer*
### -> atomtrailers([atom, [space], trailer*

### power: atom [SPACE] '**' [SPACE] factor
### -> binop("**", atom, factor)
### power: atom [SPACE] '**' [SPACE] factor [SPACE] ** [SPACE] factor2
### -> binop("**", atom, binop("**", factor, factor2)))
### power: atom [[SPACE] '**' [SPACE] factor]
### -> binop("**", atom, factor)
### power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

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
