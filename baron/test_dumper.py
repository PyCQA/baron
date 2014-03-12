#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import check_dumps


def test_empty():
    check_dumps("")


def test_var():
    check_dumps("hello")


def test_int():
    check_dumps("1")


def test_assign():
    check_dumps("a = 2")


def test_binary_operator():
    check_dumps("z +  42")
    check_dumps("z   -  42")


def test_while():
    check_dumps("while a  : pass")


def test_while_else():
    check_dumps("while a  : pass\nelse : pass")


def test_while_indent():
    check_dumps("while a:\n    pass")


def test_if():
    check_dumps("if a:\n    pass")


def test_if_elif():
    check_dumps("if a: \n    pass\nelif b: pass")


def test_if_elif_else():
    check_dumps("if a: \n    pass\nelif b: pass\nelse :   \n	pouet")


def test_import():
    check_dumps("import  a")


def test_import_madness():
    check_dumps("import  a.B .   c as  saucisse")


def test_from_import():
    check_dumps("from b   import  a  as   rev")


def test_print():
    check_dumps("print pouet")


def test_print_madness():
    check_dumps("print >>  qsd, pouet, zdzd,")


def test_atom_trailers_call():
    check_dumps("a.c(b)")


def test_atom_trailers_call_default():
    check_dumps("caramba(s, b=2)")


def test_string():
    check_dumps("'ama string!'")
