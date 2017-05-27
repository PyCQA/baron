from baron import parse, dumps


def test_regression_trailing_comment_after_colon():
    assert parse("def a(): # pouf\n    pass")


def test_regression_trailing_comment_after_colon_no_space():
    assert parse("def a():# pouf\n    pass")


def test_regression_trailing_comment_after_colon_dump():
    code = "def a(): # pouf\n    pass\n"
    assert dumps(parse(code)) == code


def test_regression_trailing_comment_after_colon_no_space_dump():
    code = "def a():# pouf\n    pass\n"
    assert dumps(parse(code)) == code


def test_comment_in_middle_of_ifelseblock():
    code = 'if a:\n    pass\n# comment\nelse:\n    pass\n'
    assert dumps(parse(code)) == code
