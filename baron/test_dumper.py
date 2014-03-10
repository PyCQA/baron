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
