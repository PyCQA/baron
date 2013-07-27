from space_grouper import group as _group


def group(inp, out):
    assert _group(inp) == out


def test_empty():
    group([], [])


def test_int():
    "1"
    group([('INT', '1')],
          [('INT', '1')])
