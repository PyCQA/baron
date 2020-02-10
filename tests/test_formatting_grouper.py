from .test_utils import zip_longest
from baron.formatting_grouper import group as _group


def group(inp, out):
    for i, j in zip_longest(_group(inp), out):
        assert i == j


def test_none():
    group([None], [])


def test_empty():
    group([], [])


def test_int():
    "1"
    group([('INT', '1')], [('INT', '1')])


def test_name():
    "a"
    group([('NAME', 'a')], [('NAME', 'a')])


def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    group([('STRING', '"pouet pouet"')], [('STRING', '"pouet pouet"')])
    group([('STRING', '"""pouet pouet"""')], [('STRING', '"""pouet pouet"""')])


def test_simple_import():
    "import   pouet"
    group([
        ('IMPORT', 'import'),
        ('SPACE', '  '),
        ('NAME', 'pouet')
    ], [
        ('IMPORT', 'import', [], [('SPACE', '  ')]),
        ('NAME', 'pouet')
    ])


def test_import_basic_dot():
    "import   pouet.blob"
    group([
        ('IMPORT', 'import'),
        ('SPACE', '  '),
        ('NAME', 'pouet'),
        ('DOT', '.'),
        ('NAME', 'blob')
    ], [
        ('IMPORT', 'import', [], [('SPACE', '  ')]),
        ('NAME', 'pouet'),
        ('DOT', '.'),
        ('NAME', 'blob')
    ])


def test_import_more_dot():
    "import   pouet.blob .plop"
    group([
        ('IMPORT', 'import'),
        ('SPACE', '  '),
        ('NAME', 'pouet'),
        ('DOT', '.'),
        ('NAME', 'blob'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('NAME', 'plop')
    ], [
        ('IMPORT', 'import', [], [('SPACE', '  ')]),
        ('NAME', 'pouet'),
        ('DOT', '.'),
        ('NAME', 'blob'),
        ('DOT', '.', [('SPACE', ' ')]),
        ('NAME', 'plop')
    ])


def test_import_as():
    "import   pouet as  b"
    group([
        ('IMPORT', 'import', [], [('SPACE', '  ')]),
        ('SPACE', '  '),
        ('NAME', 'pouet'),
        ('SPACE', ' '),
        ('AS', 'as'),
        ('SPACE', '  '),
        ('NAME', 'b')
    ], [
        ('IMPORT', 'import', [], [('SPACE', '  ')]),
        ('NAME', 'pouet'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b')
    ])


def test_import_a_b():
    "import a, b"
    group([
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_import_a_b_as_c():
    "import a, b.d as  c"
    group([
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
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
        ('NAME', 'c')
    ], [
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'd'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'c')
    ])


def test_import_a_b_c_d():
    "import a, b, c, d"
    group([
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
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
        ('NAME', 'd')
    ], [
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'd')
    ])


def test_from_a_import_b():
    "from a import b"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_a_dot_c_import_b():
    "from a.C import b"
    group([
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_a_dot_c_import_b_d():
    "from a.c import b, d"
    group([
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
        ('NAME', 'd')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'd')
    ])


def test_from_a_import_b_as_d():
    "from a import b as d"
    group([
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
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd')
    ])


def test_from_a_import_parenthesis_b():
    "from a import (b)"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')')
    ])


def test_from_a_import_parenthesis_b_without_space():
    "from a import(b)"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')]),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')')
    ])


def test_from_a_import_parenthesis_b_comma():
    "from a import (b,)"
    group([
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
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('RIGHT_PARENTHESIS', ')')
    ])


def test_from_a_import_parenthesis_b_space():
    "from a import (b )"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ])


def test_from_a_import_star():
    "from a import *"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('STAR', '*')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('STAR', '*')
    ])


def test_from_a_import_star_without_space():
    "from a import*"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('STAR', '*')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')]),
        ('STAR', '*')
    ])


def test_from_dot_a_import_b():
    "from .a import b"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('DOT', '.'),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_dot_dot_dot_a_import_b():
    "from ...a import b"
    group([
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
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('DOT', '.'),
        ('DOT', '.'),
        ('DOT', '.'),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_no_space_dot_a_import_b():
    "from.a import b"
    group([
        ('FROM', 'from'),
        ('DOT', '.'),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from'),
        ('DOT', '.'),
        ('NAME', 'a'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_dot_import_b():
    "from . import b"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('DOT', '.'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_dot_no_space_import_b():
    "from .import b"
    group([
        ('FROM', 'from'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from', [], [('SPACE', ' ')]),
        ('DOT', '.'),
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_no_space_dot_import_b():
    "from. import b"
    group([
        ('FROM', 'from'),
        ('DOT', '.'),
        ('SPACE', ' '),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from'),
        ('DOT', '.'),
        ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_from_no_space_dot_no_sapceimport_b():
    "from.import b"
    group([
        ('FROM', 'from'),
        ('DOT', '.'),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('FROM', 'from'),
        ('DOT', '.'),
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_simple_power():
    "a**b"
    group([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b')
    ])


def test_first_space_power():
    "a  **b"
    group([
        ('NAME', 'a'),
        ('SPACE', '  '),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', '  ')]),
        ('NAME', 'b')
    ])


def test_second_space_power():
    "a** b"
    group([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_spaces_power():
    "a **  b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b')
    ])


def test_power_power():
    "a **  b   **    c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('NAME', 'b'),
        ('SPACE', '   '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '    '),
        ('NAME', 'c')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ])


def test_power_power_spaces():
    "a**  b   **    c"
    group([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('NAME', 'b'),
        ('SPACE', '   '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '    '),
        ('NAME', 'c')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ])
    "a **b   **    c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('SPACE', '   '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '    '),
        ('NAME', 'c')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ])
    "a**b**c"
    group([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ])


def test_power_factor():
    "a **  +b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('PLUS', '+'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('PLUS', '+'),
        ('NAME', 'b')
    ])


def test_power_factor_minus():
    "a **  -b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('MINUS', '-'),
        ('NAME', 'b')
    ])


def test_power_factor_tild():
    "a **  ~b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('TILDE', '~'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('NAME', 'b')
    ])


def test_power_operator_madness():
    "a **  ~+-b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ])


def test_power_factor_tild_space():
    "a **  ~ b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_STAR', '**'),
        ('SPACE', '  '),
        ('TILDE', '~'),
        ('SPACE', ' '),
        ('NAME', 'b')
    ], [
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ])


def test_power_trailer():
    "a.b"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
    ])


def test_power_trailer_spaces():
    "a .b"
    "a.  b"
    "a  .   b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])

    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('SPACE', '  '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
    ])

    group([
        ('NAME', 'a'),
        ('SPACE', '   '),
        ('DOT', '.'),
        ('SPACE', '    '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'b'),
    ])


def test_power_trailers():
    "a.b.c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
    ])
    "a.b.c.d.e"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('DOT', '.'),
        ('NAME', 'd'),
        ('DOT', '.'),
        ('NAME', 'e'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('DOT', '.'),
        ('NAME', 'd'),
        ('DOT', '.'),
        ('NAME', 'e'),
    ])


def test_power_trailers_space():
    "a . b . c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('DOT', '.'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOT', '.', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_power_trailer_power():
    "a.b**c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c'),
    ])


def test_power_trailer_getitem_empty():
    "a[]"
    group([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ])


def test_power_trailer_getitem_empty_with_space():
    "a [ ]"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('LEFT_SQUARE_BRACKET', '['),
        ('SPACE', ' '),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '[', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ])


def test_power_trailer_call_empty():
    "a()"
    group([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
    ])


def test_power_trailer_call_empty_with_space():
    "a ( )"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('LEFT_PARENTHESIS', '('),
        ('SPACE', ' '),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
    ])


def test_term_mult():
    "a*b"
    group([
        ('NAME', 'a'),
        ('STAR', '*'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('STAR', '*'),
        ('NAME', 'b'),
    ])


def test_term_mult_first_space():
    "a *b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('STAR', '*'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_mult_second_space():
    "a* b"
    group([
        ('NAME', 'a'),
        ('STAR', '*'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('STAR', '*', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_mult_spaces():
    "a * b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('STAR', '*'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_mult_spaces_atomtrailers():
    "a.b * c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('STAR', '*'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('STAR', '*', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_term_div():
    "a/b"
    group([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
    ])


def test_term_div_first_space():
    "a /b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('SLASH', '/'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_div_second_space():
    "a/ b"
    group([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('SLASH', '/', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_div_spaces():
    "a / b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('SLASH', '/'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_div_spaces_atomtrailers():
    "a.b / c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('SLASH', '/'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SLASH', '/', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_term_modulo():
    "a%b"
    group([
        ('NAME', 'a'),
        ('PERCENT', '%'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PERCENT', '%'),
        ('NAME', 'b'),
    ])


def test_term_modulo_first_space():
    "a %b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('PERCENT', '%'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_modulo_second_space():
    "a% b"
    group([
        ('NAME', 'a'),
        ('PERCENT', '%'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PERCENT', '%', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_modulo_spaces():
    "a % b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('PERCENT', '%'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_modulo_spaces_atomtrailers():
    "a.b % c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('PERCENT', '%'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('PERCENT', '%', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_term_floor_division():
    "a//b"
    group([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//'),
        ('NAME', 'b'),
    ])


def test_term_floor_division_first_space():
    "a //b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_SLASH', '//'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_floor_division_second_space():
    "a// b"
    group([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_floor_division_spaces():
    "a // b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('DOUBLE_SLASH', '//'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_term_floor_division_spaces_atomtrailers():
    "a.b // c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('DOUBLE_SLASH', '//'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_combine_div_modulo_mult():
    "a/b%c*d"
    group([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ])


def test_arith_expr_plus():
    "a+b"
    group([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
    ])


def test_arith_expr_add_first_space():
    "a +b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('PLUS', '+'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_add_second_space():
    "a+ b"
    group([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PLUS', '+', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_add_spaces():
    "a + b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('PLUS', '+'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_add_spaces_atomtrailers():
    "a.b + c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('PLUS', '+'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_arith_expr_substract():
    "a-b"
    group([
        ('NAME', 'a'),
        ('MINUS', '-'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('MINUS', '-'),
        ('NAME', 'b'),
    ])


def test_arith_expr_substract_first_space():
    "a -b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('MINUS', '-'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_substract_second_space():
    "a- b"
    group([
        ('NAME', 'a'),
        ('MINUS', '-'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('MINUS', '-', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_substract_spaces():
    "a - b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('MINUS', '-'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_substract_spaces_atomtrailers():
    "a.b - c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('MINUS', '-'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_chained_add_substract():
    "a+b-c"
    group([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ])


def test_arith_expr_left_shift():
    "a<<b"
    group([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
    ])


def test_arith_expr_left_shift_first_space():
    "a <<b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_left_shift_second_space():
    "a<< b"
    group([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_left_shift_spaces():
    "a << b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('LEFT_SHIFT', '<<'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_right_shift():
    "a>>b"
    group([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'b'),
    ])


def test_arith_expr_right_shift_first_space():
    "a >>b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_right_shift_second_space():
    "a>> b"
    group([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_right_shift_spaces():
    "a >> b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_arith_expr_right_shift_spaces_atomtrailers():
    "a.b >> c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_chained_left_right_shift():
    "a<<b>>c"
    group([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ])


def test_and_expr():
    "a&b"
    group([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
    ])


def test_and_expr_first_space():
    "a &b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('AMPER', '&'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_and_expr_second_space():
    "a& b"
    group([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('AMPER', '&', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_and_expr_spaces():
    "a & b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('AMPER', '&'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_and_expr_spaces_atomtrailers():
    "a.b & c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('AMPER', '&'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('AMPER', '&', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_chained_left_and_expr():
    "a&b&c"
    group([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ])


def test_xor_expr():
    "a^b"
    group([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
    ])


def test_xor_expr_first_space():
    "a ^b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_xor_expr_second_space():
    "a^ b"
    group([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_xor_expr_spaces():
    "a ^ b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('CIRCUMFLEX', '^'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_xor_expr_spaces_atomtrailers():
    "a.b ^ c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('CIRCUMFLEX', '^'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_chained_left_xor_expr():
    "a^b^c"
    group([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ])


def test_expr():
    "a|b"
    group([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
    ])


def test_expr_first_space():
    "a |b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('VBAR', '|'),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_expr_second_space():
    "a| b"
    group([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('VBAR', '|', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_expr_spaces():
    "a | b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('VBAR', '|'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_expr_spaces_atomtrailers():
    "a.b | c"
    group([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('VBAR', '|'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('VBAR', '|', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_chained_left_expr():
    "a|b|c"
    group([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ])


comparison_tokens = (
    ('LESS', '<'),
    ('GREATER', '>'),
    ('EQUAL_EQUAL', '=='),
    ('LESS_EQUAL', '<='),
    ('GREATER_EQUAL', '>='),
    ('NOT_EQUAL', '<>'),
    ('NOT_EQUAL', '!='),
    ('IN', 'in'),
    ('IS', 'is'),
)


def test_comparison():
    "a<b"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
        ])


def test_comparison_first_space():
    "a <b"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            ('SPACE', ' '),
            (token_name, value),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')]),
            ('NAME', 'b'),
        ])


def test_comparison_second_space():
    "a< b"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            (token_name, value),
            ('SPACE', ' '),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value, [], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ])


def test_comparison_spaces():
    "a < b"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            ('SPACE', ' '),
            (token_name, value),
            ('SPACE', ' '),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ])


def test_comparison_spaces_atomtrailers():

    "a.b < c"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            ('DOT', '.'),
            ('NAME', 'b'),
            ('SPACE', ' '),
            (token_name, value),
            ('SPACE', ' '),
            ('NAME', 'c'),
        ], [
            ('NAME', 'a'),
            ('DOT', '.'),
            ('NAME', 'b'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'c'),
        ])


def test_chained_comparison():
    "a<b<c"
    for token_name, value in comparison_tokens:
        group([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ])


advanced_comparison_tokens = (
    (('NOT', 'not', [], [('SPACE', ' ')]), ('IN', 'in')),
    (('IS', 'is', [], [('SPACE', ' ')]), ('NOT', 'not')),
)


def test_advanced_comparison():
    "a not in b"
    "a is not b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        group([
            ('NAME', 'a'),
            ('SPACE', ' '),
            (token_name, value),
            after_space[0],
            (token_name2, value2),
            ('SPACE', ' '),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')], after_space),
            (token_name2, value2, [], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ])


def test_not():
    "not a"
    group([
        ('NOT', 'not'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_not_not():
    "not not a"
    group([
        ('NOT', 'not'),
        ('SPACE', ' '),
        ('NOT', 'not'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_and():
    "a and b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('AND', 'and'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_and_and():
    "a and b and c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('AND', 'and'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('AND', 'and'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_or():
    "a or b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('OR', 'or'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_or_or():
    "a or b or c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('OR', 'or'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('OR', 'or'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_ternary_operator():
    "a if b else c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IF', 'if'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('ELSE', 'else'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('ELSE', 'else', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_assignment():
    "a = b"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('EQUAL', '='),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_assignment_assignment():
    "a = b = c"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('EQUAL', '='),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('EQUAL', '='),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


augmented_assignment_tokens = (
    ('PLUS_EQUAL', '+='),
    ('MINUS_EQUAL', '-='),
    ('STAR_EQUAL', '*='),
    ('SLASH_EQUAL', '/='),
    ('PERCENT_EQUAL', '%='),
    ('AMPER_EQUAL', '&='),
    ('AT_EQUAL', '@='),
    ('VBAR_EQUAL', '|='),
    ('CIRCUMFLEX_EQUAL', '^='),
    ('LEFT_SHIFT_EQUAL', '<<='),
    ('RIGHT_SHIFT_EQUAL', '>>='),
    ('DOUBLE_STAR_EQUAL', '**='),
    ('DOUBLE_SLASH_EQUAL', '//='),
)


def test_augmented_assignment():
    "a += b"
    for token_name, value in augmented_assignment_tokens:
        group([
            ('NAME', 'a'),
            ('SPACE', ' '),
            (token_name, value),
            ('SPACE', ' '),
            ('NAME', 'b'),
        ], [
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ])


def test_expr_comma_list():
    "a or b,c+d"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('OR', 'or'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ], [
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ])


def test_expr_comma_list_3_items():
    "a or b,c+d,e"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('OR', 'or'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ])


def test_implicit_tuple_space():
    "a, b , c"
    group([
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_implicit_tuple_one_item():
    "a ,"
    group([
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COMMA', ','),
    ], [
        ('NAME', 'a'),
        ('COMMA', ',', [('SPACE', ' ')]),
    ])


def test_implicit_tuple_trailing_comma():
    "a, b ,"
    group([
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('COMMA', ','),
    ], [
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')]),
    ])


def test_return():
    "return"
    group([
        ('RETURN', 'return'),
    ], [
        ('RETURN', 'return'),
    ])


def test_return_a():
    "return a"
    group([
        ('RETURN', 'return'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('RETURN', 'return', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_yield():
    "yield"
    group([
        ('YIELD', 'yield'),
    ], [
        ('YIELD', 'yield'),
    ])


def test_yield_a():
    "yield a"
    group([
        ('YIELD', 'yield'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('YIELD', 'yield', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_del():
    "del a"
    group([
        ('DEL', 'del'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('DEL', 'del', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_break():
    "break"
    group([
        ('BREAK', 'break'),
    ], [
        ('BREAK', 'break'),
    ])


def test_continue():
    "continue"
    group([
        ('CONTINUE', 'continue'),
    ], [
        ('CONTINUE', 'continue'),
    ])


def test_pass():
    "pass"
    group([
        ('PASS', 'pass'),
    ], [
        ('PASS', 'pass'),
    ])


def test_assert():
    "assert a"
    group([
        ('ASSERT', 'assert'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('ASSERT', 'assert', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_assert_message():
    "assert a , b"
    group([
        ('ASSERT', 'assert', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('ASSERT', 'assert', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_raise_empty():
    "raise"
    group([
        ('RAISE', 'raise'),
    ], [
        ('RAISE', 'raise'),
    ])


def test_raise():
    "raise a"
    group([
        ('RAISE', 'raise'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('RAISE', 'raise', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_raise_instance():
    "raise a, b"
    group([
        ('RAISE', 'raise'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', 'comma'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('RAISE', 'raise', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', 'comma', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_raise_instance_traceback():
    "raise a, b, c"
    group([
        ('RAISE', 'raise'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', 'comma'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('COMMA', 'comma'),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('RAISE', 'raise', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', 'comma', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', 'comma', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_exec():
    "exec a"
    group([
        ('EXEC', 'exec'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('EXEC', 'exec', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_exec_in():
    "exec a in b"
    group([
        ('EXEC', 'exec'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IN', 'in'),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('EXEC', 'exec', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_exec_in_c():
    "exec a in b, c"
    group([
        ('EXEC', 'exec'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('IN', 'in'),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'c'),
    ], [
        ('EXEC', 'exec', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ])


def test_global():
    "global a"
    group([
        ('GLOBAL', 'global'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('GLOBAL', 'global', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_global_one():
    "global a, b"
    group([
        ('GLOBAL', 'global'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('GLOBAL', 'global', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_global_two():
    "global a, b ,  c"
    group([
        ('GLOBAL', 'global'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('COMMA', ','),
        ('SPACE', '  '),
        ('NAME', 'c'),
    ], [
        ('GLOBAL', 'global', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'c'),
    ])


def test_nonlocal():
    "global a"
    group([
        ('NONLOCAL', 'nonlocal'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('NONLOCAL', 'nonlocal', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_print():
    "print"
    group([
        ('PRINT', 'print'),
    ], [
        ('PRINT', 'print'),
    ])


def test_print_a():
    "print a"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_print_a_b():
    "print a, b"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_print_a_b_comma():
    "print a, b,"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('COMMA', ',', '', ''),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', '', ''),
    ])


def test_print_redirect():
    "print >> a"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ])


def test_print_redirect_ab():
    "print >> a , b"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ])


def test_print_redirect_ab_comma():
    "print >> a , b ,"
    group([
        ('PRINT', 'print'),
        ('SPACE', ' '),
        ('RIGHT_SHIFT', '>>'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COMMA', ','),
        ('SPACE', ' '),
        ('NAME', 'b'),
        ('SPACE', ' '),
        ('COMMA', ','),
    ], [
        ('PRINT', 'print', [], [('SPACE', ' ')]),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')]),
    ])


def test_if_a_pass():
    "if a : pass"
    group([
        ('IF', 'if'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COLON', ':'),
        ('SPACE', ' '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('PASS', 'pass'),
    ])


def test_if_a_pass_indent():
    """
    if a:
        pass
    """
    group([
        ('IF', 'if'),
        ('SPACE', ' '),
        ('NAME', 'a'),
        ('SPACE', ' '),
        ('COLON', ':'),
        ('ENDL', '\n'),
        ('INDENT', ''),
        ('SPACE', '    '),
        ('PASS', 'pass'),
    ], [
        ('IF', 'if', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('ENDL', '\n'),
        ('INDENT', '', [], [('SPACE', '    ')]),
        ('PASS', 'pass'),
    ])


def test_endl_backward():
    """
        """
    group([
        ('SPACE', '    '),
        ('ENDL', '\n'),
    ], [
        ('ENDL', '\n', [('SPACE', '    ')]),
    ])


def test_endl():
    """
        """
    group([
        ('ENDL', '\n'),
        ('SPACE', '    '),
        ('ENDL', '\n'),
    ], [
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('ENDL', '\n'),
    ])


def test_endl_import():
    """
        """
    group([
        ('ENDL', '\n'),
        ('SPACE', '    '),
        ('IMPORT', 'import'),
    ], [
        ('ENDL', '\n', [], [('SPACE', '    ')]),
        ('IMPORT', 'import'),
    ])


def test_while():
    """
        """
    group([
        ('WHILE', 'while'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('WHILE', 'while', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_elif():
    """
        """
    group([
        ('ELIF', 'elif'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('ELIF', 'elif', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_for():
    """
        """
    group([
        ('SPACE', '    '),
        ('FOR', 'for'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('FOR', 'for', [('SPACE', '    ')], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_async_for():
    """
        """
    group([
        ('NAME', 'async'),
        ('SPACE', '    '),
        ('FOR', 'for'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('NAME', 'async'),
        ('FOR', 'for', [('SPACE', '    ')], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_except():
    """
        """
    group([
        ('EXCEPT', 'except'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('EXCEPT', 'except', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_def():
    """
        """
    group([
        ('DEF', 'def'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('DEF', 'def', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_async_def():
    """
        """
    group([
        ('NAME', 'async'),
        ('SPACE', '    '),
        ('DEF', 'def'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('NAME', 'async'),
        ('SPACE', '    '),
        ('DEF', 'def', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_class():
    """
        """
    group([
        ('CLASS', 'class'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('CLASS', 'class', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_with():
    """
        """
    group([
        ('WITH', 'with'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('WITH', 'with', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_async_with():
    """
        """
    group([
        ('NAME', 'async'),
        ('SPACE', '    '),
        ('WITH', 'with'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('NAME', 'async'),
        ('SPACE', '    '),
        ('WITH', 'with', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_lambda():
    """
        """
    group([
        ('LAMBDA', 'lambda'),
        ('SPACE', '    '),
        ('NAME', 'a'),
    ], [
        ('LAMBDA', 'lambda', [], [('SPACE', '    ')]),
        ('NAME', 'a'),
    ])


def test_comment():
    """
        """
    group([
        ('SPACE', ' '),
        ('COMMENT', '#'),
    ], [
        ('COMMENT', '#', [('SPACE', ' ')]),
    ])


def test_repr():
    "` "
    group([
        ('BACKQUOTE', '`'),
        ('SPACE', ' '),
    ], [
        ('BACKQUOTE', '`', [], [('SPACE', ' ')]),
    ])


def test_semicolon():
    " ; "
    group([
        ('SPACE', ' '),
        ('SEMICOLON', ';'),
        ('SPACE', ' '),
    ], [
        ('SEMICOLON', ';', [('SPACE', ' ')], [('SPACE', ' ')]),
    ])


def test_strings():
    """
    I don't this because python allow to write stuff like 'qsd' rb"qsd" u'pouet'
    """
    for i in ('STRING', 'RAW_STRING', 'UNICODE_STRING', 'INTERPOLATED_STRING', 'UNICODE_RAW_STRING', 'BINARY_STRING', 'INTERPOLATED_RAW_STRING', 'BINARY_RAW_STRING'):
        group([
            ('SPACE', ' '),
            (i, 'dummy'),
            ('SPACE', ' '),
        ], [
            (i, 'dummy', [('SPACE', ' ')], [('SPACE', ' ')]),
        ])


def test_inconsistancy_on_space_grouping():
    group([
        ('LEFT_PARENTHESIS', '('),
        ('SPACE', ' '),
        ('INT', '1'),
        ('SPACE', ' '),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('INT', '1'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ])

    group([
        ('LEFT_PARENTHESIS', '('),
        ('SPACE', ' '),
        ('STRING', '"a"'),
        ('SPACE', ' '),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        ('LEFT_PARENTHESIS', '(', [], [('SPACE', ' ')]),
        ('STRING', '"a"'),
        ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
    ])


def test_space_before_comment_simple():
    group([
        ('ENDL', '\n'),
        ('SPACE', ' '),
        ('COMMENT', '# hello'),
        ('ENDL', '\n'),
    ], [
        ('ENDL', '\n', [], [('SPACE', ' ')]),
        ('COMMENT', '# hello'),
        ('ENDL', '\n'),
    ]

    )


def test_space_before_comment():
    group([
        ('ENDL', '\n'),
        ('SPACE', ' '),
        ('COMMENT', '# hello'),
        ('ENDL', '\n'),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 're'),
        ('ENDL', '\n'),
        ('COMMENT', '# hi'),
        ('ENDL', '\n'),
        ('IMPORT', 'import'),
        ('SPACE', ' '),
        ('NAME', 'sys'),
        ('ENDL', '\n'),
        ('ENDMARKER', ''),
    ], [
        ('ENDL', '\n', [], [('SPACE', ' ')]),
        ('COMMENT', '# hello'),
        ('ENDL', '\n'),
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 're'),
        ('ENDL', '\n'),
        ('COMMENT', '# hi'),
        ('ENDL', '\n'),
        ('IMPORT', 'import', [], [('SPACE', ' ')]),
        ('NAME', 'sys'),
        ('ENDL', '\n'),
        ('ENDMARKER', '')
    ]

    )


def test_right_arrow():
    " -> "
    group([
        ('SPACE', ' '),
        ('RIGHT_ARROW', '->'),
        ('SPACE', ' '),
    ], [
        ('RIGHT_ARROW', '->', [('SPACE', ' ')], [('SPACE', ' ')]),
    ])
