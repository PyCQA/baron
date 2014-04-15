from baron.baron import parse
import baron.finder as finder
import json

simplecode = """vara = 1"""

def make_path(path, type, pos):
    return json.dumps({"path":path, "type":type, "position_in_rendering_list":pos})


def check_path(code, line, column, target_node):
    assert finder.path_to_location(parse(code), line, column) == target_node


def test_sc_line_before_scope():
    check_path(simplecode, -1, 3, None)


def test_sc_column_before_scope():
    check_path(simplecode, 1, -3, None)


def test_sc_line_after_scope():
    check_path(simplecode, 3, 3, None)


def test_sc_column_after_scope():
    check_path(simplecode, 1, 100, None)


def test_sc_assignment():
    check_path(simplecode, 1, 100, None)


def test_sc_assignement_target():
    path = make_path([0, "target", "value"], "name", 1)
    check_path(simplecode, 1, 1, path)
    check_path(simplecode, 1, 2, path)
    check_path(simplecode, 1, 3, path)
    check_path(simplecode, 1, 4, path)


def test_sc_assignement_first_formatting():
    path = make_path([0, "first_formatting"], "assignment", 2)
    check_path(simplecode, 1, 5, path)


def test_sc_assignement_operator():
    path = make_path([0], "assignment", 3)
    check_path(simplecode, 1, 6, path)


def test_sc_assignement_second_formatting():
    path = make_path([0, "second_formatting"], "assignment", 4)
    check_path(simplecode, 1, 7, path)


def test_sc_assignement_target():
    path = make_path([0, "value", "value"], "int", 1)
    check_path(simplecode, 1, 8, path)
