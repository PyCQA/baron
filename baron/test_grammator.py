#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import (parse, space, inteu, endl, name, string, importeu,
                        dotted_as_name, dotted_name, dot, comma, from_import,
                        name_as_name, left_parenthesis, right_parenthesis,
                        star, binary_operator, unitary_operator, atomtrailers)

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
           ('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet')],
          [importeu([
                     dotted_as_name(dotted_name([name("pouet")]))
                    ],
                    space="  ")])

def test_import_basic_dot():
    "import   pouet.blob"
    parse([
           ('IMPORT', 'import'),
           ('SPACE', '  '),
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
           ('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('SPACE', ' '),
           ('DOT', '.'),
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
           ('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet'),
           ('SPACE', ' '),
           ('AS', 'as'),
           ('SPACE', '  '),
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
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('COMMA', ','),
           ('SPACE', ' '),
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
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('COMMA', ','),
           ('SPACE', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('SPACE', ' '),
           ('AS', 'as'),
           ('SPACE', '  '),
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
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('COMMA', ','),
           ('SPACE', ' '),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('SPACE', ' '),
           ('NAME', 'c'),
           ('COMMA', ','),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'b'),
           ('SPACE', ' '),
           ('AS', 'as'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('SPACE', ' '),
           ('RIGHT_PARENTHESIS', ')')
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('DOT', '.'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('FROM', 'from'),
           ('SPACE', ' '),
           ('DOT', '.'),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('IMPORT', 'import'),
           ('SPACE', ' '),
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
           ('SPACE', '  '),
           ('DOUBLE_STAR', '**'),
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
           ('DOUBLE_STAR', '**'),
           ('SPACE', ' '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
           ('NAME', 'b'),
           ('SPACE', '   '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '    '),
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
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
           ('NAME', 'b'),
           ('SPACE', '   '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '    '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('NAME', 'b'),
           ('SPACE', '   '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '    '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
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
           ('SPACE', ' '),
           ('DOUBLE_STAR', '**'),
           ('SPACE', '  '),
           ('TILDE', '~'),
           ('SPACE', ' '),
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

# stmt: simple_stmt
# stmt: compound_stmt

# simple_stmt: small_stmt [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

# small_stmt: expr_stmt
# small_stmt: print_stmt
# small_stmt: del_stmt
# small_stmt: pass_stmt
# small_stmt: flow_stmt
# small_stmt: import_stmt
# small_stmt: global_stmt
# small_stmt: exec_stmt
# small_stmt: assert_stmt

# expr_stmt: testlist
# expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
# -> assign(testlist, testlist)
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# -> assign(testlist, testlist)
# expr_stmt: testlist augassign yield_expr
# -> augassign(testlist, testlist)
# expr_stmt: testlist augassign testlist
# -> augassign(testlist, testlist)

# testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']
# -> testlist([...])

# test: lambdef
# test: or_test
# test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]
# -> ternaryOp(or_test, or_test, test)

# or_test: and_test
# or_test: and_test (SPACE 'or' SPACE and_test)*
# -> boolOP('or', not_test, not_test)

# and_test: not_test
# and_test: not_test (SPACE 'and' SPACE not_test)*
# -> boolOP('and', not_test, not_test)

# not_test: comparison
# not_test: 'not' SPACE not_test
# -> unitaryOp('not', not_test)

# comparison: expr
# -> expr
# comparison: expr (comp_op expr)*
# -> comparison(comp_or, expr, expr)

# comp_op: '<'
# comp_op: '>'
# comp_op: '=='
# comp_op: '>='
# comp_op: '<='
# comp_op: '<>'
# comp_op: '!='
# comp_op: 'in'
# comp_op: 'not' SPACE 'in'
# comp_op: 'is'
# comp_op: 'is' SPACE 'not'
# -> comp_op

# expr: xor_expr
# expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*
# -> binop('|', term, term)

# xor_expr: and_expr
# xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*
# -> binop('^', term, term)

# and_expr: shift_expr
# and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*
# -> binop('&', term, term)

# shift_expr: arith_expr
# shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*
# -> binop(('<<'|'>>'), term, term)

# arith_expr: term
# -> term
# arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*
# -> binop(('+'|'-'), term, term)

# term: factor
# -> factor
# term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*
# -> binop(('*'|'/'|'%'|'//'), factor, factor)

### factor: ('+'|'-'|'~') [SPACE] factor
### -> uniatryop(('+'|'-'|'~'), factor)
### factor: power
### -> power

### power: atom
### -> atom
# power: atom [SPACE] trailer*
# -> dépend du trailer (eg: dotted_name) -> doit être une liste
### power: atom [SPACE] '**' [SPACE] factor
### -> binop("**", atom, factor)
### power: atom [SPACE] '**' [SPACE] factor [SPACE] ** [SPACE] factor2
### -> binop("**", atom, binop("**", factor, factor2)))
### power: atom [[SPACE] '**' [SPACE] factor]
### -> binop("**", atom, factor)
# power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

# trailer: '.' [SPACE] NAME
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
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
