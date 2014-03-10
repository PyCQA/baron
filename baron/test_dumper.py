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
