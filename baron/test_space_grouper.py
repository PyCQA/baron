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
