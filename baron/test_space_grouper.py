from space_grouper import group as _group


def group(inp, out):
    assert _group(inp) == out


def test_empty():
    group([], [])
