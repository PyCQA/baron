#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import (parse, space, expression, inteu, endl, name, string,
                        importeu, dotted_as_name, dotted_name, dot, comma)

def test_empty():
    ""
    parse([], [])

def test_space():
    "   "
    parse([('SPACE', '   ')], [space("   ")])

def test_int():
    "1"
    parse([('INT', '1')], [expression(inteu("1"))])

def test_endl():
    "\n"
    parse([('ENDL', '\n')], [endl("\n", before_space="")])

def test_space_endl():
    "    \n"
    parse([('SPACE', '   '), ('ENDL', '\n')], [endl("\n", before_space="   ")])

def test_some_stuff():
    "3    \n42"
    parse([('INT', '3'), ('SPACE', '   '), ('ENDL', '\n'), ('INT', '42')], [expression(inteu("3")), endl("\n", before_space="   "), expression(inteu("42"))])

def test_name():
    "a"
    parse([('NAME', 'a')], [expression(name("a"))])

def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    parse([('STRING', '"pouet pouet"')], [expression(string('"pouet pouet"'))])
    parse([('STRING', '"""pouet pouet"""')], [expression(string('"""pouet pouet"""'))])

def test_simple_import():
    "import   pouet"
    parse([('IMPORT', 'import'), ('SPACE', '  '), ('NAME', 'pouet')], [importeu([dotted_as_name(dotted_name([name("pouet")]))], space="  ")])

def test_import_basic_dot():
    "import   pouet.blob"
    parse([('IMPORT', 'import'), ('SPACE', '  '), ('NAME', 'pouet'), ('DOT', '.'), ('NAME', 'blob')], [importeu([dotted_as_name(dotted_name([name("pouet"), dot(), name("blob")]))], space="  ")])

def test_import_more_dot():
    "import   pouet.blob .plop"
    parse([('IMPORT', 'import'), ('SPACE', '  '), ('NAME', 'pouet'), ('DOT', '.'), ('NAME', 'blob'), ('SPACE', ' '), ('DOT', '.'), ('NAME', 'plop')], [importeu([dotted_as_name(dotted_name([name("pouet"), dot(), name("blob"), space(" "), dot(), name("plop")]))], space="  ")])

def test_import_as():
    "import   pouet as  b"
    parse([('IMPORT', 'import'), ('SPACE', '  '), ('NAME', 'pouet'), ('SPACE', ' '), ('AS', 'as'), ('SPACE', '  '), ('NAME', 'b')], [importeu([dotted_as_name(dotted_name([name("pouet")]), before_space=" ", as_=True, after_space="  ", target='b')], space="  ")])

def test_import_a_b():
    "import a, b"
    parse([('IMPORT', 'import'), ('SPACE', ' '), ('NAME', 'a'), ('COMMA', ','), ('SPACE', ' '), ('NAME', 'b')], [importeu([dotted_as_name(dotted_name([name('a')])), comma(), space(), dotted_as_name(dotted_name([name('b')]))], space=" ")])

def test_import_a_b_as_c():
    "import a, b.d as  c"
    parse([('IMPORT', 'import'), ('SPACE', ' '), ('NAME', 'a'), ('COMMA', ','), ('SPACE', ' '), ('NAME', 'b'), ('DOT', '.'), ('NAME', 'd'), ('SPACE', ' '), ('AS', 'as'), ('SPACE', '  '), ('NAME', 'c')], [importeu([dotted_as_name(dotted_name([name('a')])), comma(), space(), dotted_as_name(dotted_name([name('b'), dot(), name('d')]), as_=True, before_space=" ", after_space="  ", target="c")], space=" ")])

### dotted_name: NAME
### dotted_name: NAME.NAME
### dotted_name: NAME(.NAME)+

### dotted_as_name: dotted_name
### dotted_as_name: dotted_name SPACE 'as' SPACE NAME

### dotted_as_names: dotted_as_name
# dotted_as_names: dotted_as_name [SPACE] ',' [SPACE] dotted_as_name
# dotted_as_names: dotted_as_name ([SPACE] ',' [SPACE] dotted_as_name)*

# don't think I need this one
# import_as_name: NAME
# import_as_name: NAME SPACE 'as' SPACE NAME

# neither this one
# import_as_names: import_as_name
# import_as_names: import_as_name [SPACE] ',' [SPACE] import_as_name
# import_as_names: import_as_name ([SPACE] ',' [SPACE] import_as_name)*
# import_as_names: import_as_name ([SPACE] ',' [SPACE] import_as_name)* [SPACE] [',']

# but I this one is correct
# import_name: 'import' SPACE dotted_as_names

# import_from: 'from' SPACE dotted_name SPACE 'import' SPACE import_as_names
# import_from: 'from' SPACE dotted_name SPACE 'import' [SPACE] '(' [SPACE] import_as_names [SPACE] ')'
# import_from: 'from' SPACE dotted_name SPACE 'import' [SPACE] '*'

# import_from: 'from' [SPACE] '.'* [SPACE] dotted_name SPACE 'import' ...........
# import_from: 'from' [SPACE] '.'+ [SPACE] 'import' ...........

# ----------

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
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# expr_stmt: testlist augassign yield_expr
# expr_stmt: testlist augassign testlist

# testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# test: lambdef
# test: or_test
# test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]

# or_test: and_test
# or_test: and_test (SPACE 'or' SPACE and_test)*

# and_test: not_test
# and_test: not_test (SPACE 'and' SPACE not_test)*

# not_test: 'not' SPACE not_test
# not_test: comparison

# comparison: expr
# comparison: expr (comp_op expr)*

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

# expr: xor_expr
# expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*

# xor_expr: and_expr
# xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*

# and_expr: shift_expr
# and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*

# shift_expr: arith_expr
# shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*

# arith_expr: term
# arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*

# term: factor
# term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*

# factor: ('+'|'-'|'~') [SPACE] factor
# factor: power

# power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

# trailer: '.' [SPACE] NAME
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
# atom: '[' [SPACE] [listmaker] [SPACE] ']'
# atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# atom: '`' [SPACE] testlist1 [SPACE] '`'
### atom: NAME
### atom: NUMBER
### atom: STRING+
