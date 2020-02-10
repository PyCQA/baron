# -*- coding: utf-8 -*-

from baron import (parse, BaronError, ParsingError,
                   GroupingError, UntreatedError)
import pytest


def test_dummy_parse():
    parse("pouet")


def test_error_parsing_error():
    with pytest.raises(ParsingError):
        parse("(")
    with pytest.raises(BaronError):
        parse("(")


def test_error_unexpected_formatting():
    with pytest.raises(ParsingError):
        parse("   a\nb")
    with pytest.raises(BaronError):
        parse("   a\nb")


def test_error_grouping():
    with pytest.raises(GroupingError):
        parse("   (a\n b")
    with pytest.raises(BaronError):
        parse("   (a\n b")


def test_error_untreated_error():
    with pytest.raises(UntreatedError):
        parse("?")
    with pytest.raises(BaronError):
        parse("?")


def test_missing_quote_yields_error():
    with pytest.raises(UntreatedError):
        parse("'")
    with pytest.raises(UntreatedError):
        parse("'\n")
    with pytest.raises(BaronError):
        parse("'\n")


def test_error_bad_indentation():
    """ Regression test case

    It shows a discrepency between python2 and python3 in string
    comparisons with None.
    """
    with pytest.raises(ParsingError):
        parse("def fun():\nass")
    with pytest.raises(BaronError):
        parse("def fun():\nass")
