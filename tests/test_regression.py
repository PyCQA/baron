import pytest

from baron import parse, parser, dumps


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


@pytest.mark.parametrize(
    'code',
    (
        'sss = "some str"\\\n# some comment\nprint(sss)',
        'sss = "some str"\\\n\nprint(sss)',
    ),
)
def test_eol_esc_no_continuation(code):
    """Test that parser reads escaped EOL continuation w/ empty line."""
    assert dumps(parse(code)) == code


def test_eol_esc_invalid_continuation():
    """Test that illegal escaped EOL continuation raises an error."""
    code = 'sss = "some str"\\\nprint(sss)'
    with pytest.raises(
            parser.ParsingError,
            match='^Error, got an unexpected token NAME here:',
    ):
        parse(code)
