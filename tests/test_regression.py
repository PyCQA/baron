from baron import parse


def test_regression_trailing_comment_after_colon():
    assert parse("def a(): # pouf\n    pass")


def test_regression_trailing_comment_after_colon_no_space():
    assert parse("def a():# pouf\n    pass")
