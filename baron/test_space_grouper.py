from space_grouper import group as _group


def group(inp, out):
    assert _group(inp) == out


def test_empty():
    group([], [])


def test_int():
    "1"
    group([('INT', '1')],
          [('INT', '1')])


def test_name():
    "a"
    group([('NAME', 'a')],
          [('NAME', 'a')])


def test_string():
    '''
    "pouet pouet"
    """pouet pouet"""
    '''
    group([('STRING', '"pouet pouet"')],
          [('STRING', '"pouet pouet"')])
    group([('STRING', '"""pouet pouet"""')],
          [('STRING', '"""pouet pouet"""')])


def test_simple_import():
    "import   pouet"
    group([('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet')],
          [('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet')])


def test_import_basic_dot():
    "import   pouet.blob"
    group([('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')])


def test_import_more_dot():
    "import   pouet.blob .plop"
    group([('IMPORT', 'import'),
           ('SPACE', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('SPACE', ' '),
           ('DOT', '.'),
           ('NAME', 'plop')],
          [('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')])


def test_import_as():
    "import   pouet as  b"
    group([('IMPORT', 'import', '', '  '),
           ('SPACE', '  '),
           ('NAME', 'pouet'),
           ('SPACE', ' '),
           ('AS', 'as'),
           ('SPACE', '  '),
           ('NAME', 'b')],
          [('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'b')])


def test_import_a_b():
    "import a, b"
    group([('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('COMMA', ','),
           ('SPACE', ' '),
           ('NAME', 'b')],
          [('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')])


def test_import_a_b_as_c():
    "import a, b.d as  c"
    group([('IMPORT', 'import', '', ' '),
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
           ('NAME', 'c')],
          [('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')])


def test_import_a_b_c_d():
    "import a, b, c, d"
    group([('IMPORT', 'import', '', ' '),
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
           ('NAME', 'd')],
          [('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')])


def test_from_a_import_b():
    "from a import b"
    group([('FROM', 'from'),
           ('SPACE', ' '),
           ('NAME', 'a'),
           ('SPACE', ' '),
           ('IMPORT', 'import'),
           ('SPACE', ' '),
           ('NAME', 'b')],
          [('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')])
