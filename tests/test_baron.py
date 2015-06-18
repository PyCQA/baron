# -*- coding: utf-8 -*-

from baron import parse, BaronError, ParsingError, UnExpectedFormattingToken, GroupingError, UntreatedError
import pytest


def test_dummy_parse():
    parse("pouet")


def test_error_parsing_error():
    with pytest.raises(ParsingError):
        parse("(")
    with pytest.raises(BaronError):
        parse("(")


def test_error_unexpected_formatting():
    with pytest.raises(UnExpectedFormattingToken):
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

