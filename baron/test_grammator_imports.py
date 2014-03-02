#!/usr/bin/python
# -*- coding:Utf-8 -*-
from test_utils import parse_simple, space, name, importeu, dotted_as_name, dotted_name, dot, comma, from_import, name_as_name, left_parenthesis, right_parenthesis


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
                                { "type": "star", "value": "*", }
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
                                { "type": "star", "value": "*", }
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
