# flake8: noqa

from baron.baron import parse
from baron.path import PathWalker, Position, BoundingBox
from baron.path import position_to_path, path_to_node, position_to_node
from baron.path import path_to_bounding_box, node_to_bounding_box
from baron.utils import string_instance


def test_position():
    pos1 = (1, 2)
    pos2 = Position((1, 2))
    pos3 = Position((1, 2))
    pos4 = Position(Position((1, 2)))

    assert pos1 == pos2
    assert pos2 == pos3
    assert pos3 == pos4

    assert isinstance(pos2, Position)
    assert isinstance(pos3, Position)
    assert isinstance(pos4, Position)


def test_position_compare():
    assert Position((1, 2)) < Position((1, 3))
    assert Position((0, 9)) < Position((1, 3))
    assert Position((1, 2)) <= Position((1, 3))
    assert Position((0, 9)) <= Position((1, 3))
    assert Position((1, 2)) <= Position((1, 2))
    assert Position((1, 2)) == Position((1, 2))

    assert Position((1, 4)) > Position((1, 3))
    assert Position((2, 0)) > Position((1, 3))
    assert Position((1, 4)) >= Position((1, 3))
    assert Position((2, 0)) >= Position((1, 3))
    assert Position((1, 4)) >= Position((1, 4))
    assert Position((1, 4)) == Position((1, 4))


def test_position_bool():
    assert bool(Position((1, 2)))
    assert not bool(Position((-1, 2)))
    assert not bool(Position((1, -2)))
    assert not bool(Position((-1, -2)))


def test_bounding_box():
    bb1 = ((1, 2), (3, 4))
    bb2 = BoundingBox(((1, 2), (3, 4)))
    bb3 = BoundingBox((Position((1, 2)), (3, 4)))
    bb4 = BoundingBox(((1, 2), Position((3, 4))))
    bb5 = BoundingBox((Position((1, 2)), Position((3, 4))))
    bb6 = BoundingBox(((1, 2), (3, 4)))
    bb7 = BoundingBox((Position((1, 2)), (3, 4)))
    bb8 = BoundingBox(((1, 2), Position((3, 4))))
    bb9 = BoundingBox((Position((1, 2)), Position((3, 4))))
    bb10 = BoundingBox(BoundingBox(((1, 2), (3, 4))))

    assert bb1 == bb2
    assert bb2 == bb3
    assert bb3 == bb4
    assert bb4 == bb5
    assert bb5 == bb6
    assert bb6 == bb7
    assert bb7 == bb8
    assert bb8 == bb9
    assert bb9 == bb10

    assert isinstance(bb2, BoundingBox)
    assert isinstance(bb3, BoundingBox)
    assert isinstance(bb4, BoundingBox)
    assert isinstance(bb5, BoundingBox)
    assert isinstance(bb6, BoundingBox)
    assert isinstance(bb7, BoundingBox)
    assert isinstance(bb8, BoundingBox)
    assert isinstance(bb9, BoundingBox)
    assert isinstance(bb10, BoundingBox)


simplecode = """vara = 1"""


bigcode = """\
def fun(arg1, arg2): 
    var *= 1

@deco("arg")
def fun2(arg1 = default, **kwargs):
    arg1.attr = 3
"""


splitcode = """var \\\n  = 2"""
windows_splitcode = """var \\\r\n  = 2"""


classcode = """\
class MyClass(BaseClass):
    def __init__(self, arg1):
        self.a = arg1

    def getA():
        return self.a
"""


class PathWalkerTester(PathWalker):
    """This class is used exclusively to test the PathWalker

    It works by walking along with the PathWalker and for each step,
    i.e. for each before, after and on_leaf method called, it checks if
    that step was indeed expected.
    To specify the expected steps, you should simply pass a list of
    tuples. The first field tells what kind of step it should be:
      * '>' for calling the `before` method, i.e. going down the tree,
      * '<' for calling the `after` method, i.e. going up the tree
    and the second is what the current path should be at that step.
    """
    def __init__(self, paths):
        super(PathWalkerTester, self).__init__(strict=True)
        self.paths = paths

    def before(self, *args):
        super(PathWalkerTester, self).before(*args)
        self.process_test('>')

    def after(self, *args):
        self.process_test('<')
        super(PathWalkerTester, self).after(*args)

    def process_test(self, node_type):
        _node_type, _path = self.paths.pop(0)
        assert _node_type == node_type
        assert _path == self.current_path


def check_path(code, positions, target_path):
    tree = parse(code)

    for position in positions:
        path = position_to_path(tree, position)
        assert path == target_path

        if path is None:
            assert position_to_node(tree, position) is None
            return

        node = path_to_node(tree, path)
        assert isinstance(node, string_instance)

        assert position_to_node(tree, position) is node

    if target_path is not None:
        bounding_box = (positions[0], positions[-1])
        assert path_to_bounding_box(tree, path) == bounding_box


def test_path_walker_assignment():
    node = parse("a = 1")
    # Indentation is purely visual sugar
    walker = PathWalkerTester([
        ('>', [0]),
        ('>', [0, 'target']),
        ('>', [0, 'target', 'value']),
        ('<', [0, 'target', 'value']),
        ('<', [0, 'target']),
        ('>', [0, 'first_formatting']),
        ('>', [0, 'first_formatting', 0]),
        ('>', [0, 'first_formatting', 0, 'value']),
        ('<', [0, 'first_formatting', 0, 'value']),
        ('<', [0, 'first_formatting', 0]),
        ('<', [0, 'first_formatting']),
        ('>', [0, '=']),
        ('<', [0, '=']),
        ('>', [0, 'second_formatting']),
        ('>', [0, 'second_formatting', 0]),
        ('>', [0, 'second_formatting', 0, 'value']),
        ('<', [0, 'second_formatting', 0, 'value']),
        ('<', [0, 'second_formatting', 0]),
        ('<', [0, 'second_formatting']),
        ('>', [0, 'value']),
        ('>', [0, 'value', 'value']),
        ('<', [0, 'value', 'value']),
        ('<', [0, 'value']),
        ('<', [0]),
    ])

    walker.walk(node)


def test_bb_name():
    node = parse("var")[0]
    assert node_to_bounding_box(node) == ((1, 1), (1, 3))


def test_bb_string():
    node = parse("\"hello\"")[0]
    assert path_to_bounding_box(node, []) == ((1, 1), (1, 7))


def test_bb_comment():
    node = parse("# comment")[0]
    assert path_to_bounding_box(node, None) == ((1, 1), (1, 9))


def test_bb_funcdef():
    node = parse(bigcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (4, 0))


def test_bb_class():
    node = parse(classcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (7, 0))


def test_bb_split_assignment():
    node = parse(splitcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (2, 5))


def test_sc_out_of_scope():
    check_path(simplecode, [(-1, 3), (1, -3), (3, 3), (1, 100)], None)


def test_sc_assignement_target():
    path = [0, "target", "value"]
    check_path(simplecode, [(1, 1), (1, 2), (1, 3), (1, 4)], path)


def test_sc_assignement_first_formatting():
    path = [0, "first_formatting", 0, "value"]
    check_path(simplecode, [(1, 5)], path)


def test_sc_assignement_operator():
    path = [0, "="]
    check_path(simplecode, [(1, 6)], path)


def test_sc_assignement_second_formatting():
    path = [0, "second_formatting", 0, "value"]
    check_path(simplecode, [(1, 7)], path)


def test_sc_assignement_value():
    path = [0, "value", "value"]
    check_path(simplecode, [(1, 8)], path)


def test_bc_l1_def():
    path = [0, "def"]
    check_path(bigcode, [(1, 1), (1, 2), (1, 3)], path)


def test_bc_l1_def_first_formatting():
    tree = parse(bigcode)
    path = [0, "first_formatting"]
    assert path_to_bounding_box(tree, path) == ((1, 4), (1, 4))

    path = [0, "first_formatting", 0]
    assert path_to_bounding_box(tree, path) == ((1, 4), (1, 4))

    path = [0, "first_formatting", 0, "value"]
    check_path(bigcode, [(1, 4)], path)


def test_bc_l1_def_name():
    path = [0, "name"]
    check_path(bigcode, [(1, 5), (1, 6), (1, 7)], path)


def test_bc_l1_def_second_formatting():
    path = [0, "second_formatting"]
    tree = parse(bigcode)
    assert path_to_bounding_box(tree, path) == ((1, 8), (1, 7))


def test_bc_l1_def_left_paren():
    path = [0, "("]
    check_path(bigcode, [(1, 8)], path)


def test_bc_l1_arg1():
    path = [0, "arguments", 0, "target", "value"]
    check_path(bigcode, [(1, 9), (1, 10), (1, 11), (1, 12)], path)


def test_bc_l1_comma():
    path = [0, "arguments", 1, ","]
    check_path(bigcode, [(1, 13)], path)


def test_bc_l1_comma_second_formatting():
    path = [0, "arguments", 1, "second_formatting", 0, "value"]
    check_path(bigcode, [(1, 14)], path)


def test_bc_l1_arg2():
    path = [0, "arguments", 2, "target", "value"]
    check_path(bigcode, [(1, 15), (1, 16), (1, 17), (1, 18)], path)


def test_bc_l1_right_paren():
    path = [0, ")"]
    check_path(bigcode, [(1, 19)], path)


def test_bc_l1_colon():
    path = [0, ":"]
    check_path(bigcode, [(1, 20)], path)


def test_bc_l1_space():
    path = [0, "value", 0, "formatting", 0, "value"]
    check_path(bigcode, [(1, 21)], path)


def test_bc_l1_out_of_scope():
    check_path(bigcode, [(1, 22), (2, 0)], None)


def test_bc_l2_endl():
    path = [0, "value", 0, "indent"]
    check_path(bigcode, [(2, 1), (2, 2), (2, 3), (2, 4)], path)


def test_bc_l2_assign_var():
    path = [0, "value", 1, "target", "value"]
    check_path(bigcode, [(2, 5), (2, 6), (2, 7)], path)


def test_bc_l2_assign_first_formatting():
    path = [0, "value", 1, "first_formatting", 0, "value"]
    check_path(bigcode, [(2, 8)], path)


def test_bc_l2_assign_operator():
    path = [0, "value", 1, "operator"]
    check_path(bigcode, [(2, 9)], path)


def test_bc_l2_assign_equal():
    path = [0, "value", 1, "="]
    check_path(bigcode, [(2, 10)], path)


def test_bc_l2_assign_second_formatting():
    path = [0, "value", 1, "second_formatting", 0, "value"]
    check_path(bigcode, [(2, 11)], path)


def test_bc_l2_assign_value():
    path = [0, "value", 1, "value", "value"]
    check_path(bigcode, [(2, 12)], path)


def test_bc_l2_out_of_scope():
    check_path(bigcode, [(2, 13), (3, 0)], None)


def test_bc_l3_empty():
    check_path(bigcode, [(3, 1)], None)


def test_bc_l4_decorator_at():
    path = [1, "decorators", 0, "@"]
    check_path(bigcode, [(4, 1)], path)


def test_bc_l4_decorator_name():
    path = [1, "decorators", 0, "value", "value", 0, "value"]
    check_path(bigcode, [(4, 2), (4, 3), (4, 4), (4, 5)], path)


def test_bc_l4_decorator_left_paren():
    path = [1, "decorators", 0, "call", "("]
    check_path(bigcode, [(4, 6)], path)


def test_bc_l4_decorator_arg1():
    path = [1, "decorators", 0, "call", "value", 0, "value", "value"]
    check_path(bigcode, [(4, 7), (4, 8), (4, 9), (4, 10), (4, 11)], path)


def test_bc_l4_decorator_right_paren():
    path = [1, "decorators", 0, "call", ")"]
    check_path(bigcode, [(4, 12)], path)


def test_bc_l4_out_of_scope():
    check_path(bigcode, [(4, 13), (5, 0)], None)


def test_bc_l5_def():
    path = [1, "def"]
    check_path(bigcode, [(5, 1), (5, 2), (5, 3)], path)


def test_bc_l5_def_first_formatting():
    path = [1, "first_formatting", 0, "value"]
    check_path(bigcode, [(5, 4)], path)


def test_bc_l5_def_name():
    path = [1, "name"]
    check_path(bigcode, [(5, 5), (5, 6), (5, 7), (5, 8)], path)


def test_bc_l5_left_paren():
    path = [1, "("]
    check_path(bigcode, [(5, 9)], path)


def test_bc_l5_arg1():
    path = [1, "arguments", 0, "target", "value"]
    check_path(bigcode, [(5, 10), (5, 11), (5, 12), (5, 13)], path)


def test_bc_l5_arg1_first_formatting():
    path = [1, "arguments", 0, "first_formatting", 0, "value"]
    check_path(bigcode, [(5, 14)], path)


def test_bc_l5_arg1_equal():
    path = [1, "arguments", 0, "="]
    check_path(bigcode, [(5, 15)], path)


def test_bc_l5_arg1_second_formatting():
    path = [1, "arguments", 0, "second_formatting", 0, "value"]
    check_path(bigcode, [(5, 16)], path)


def test_bc_l5_arg1_value():
    path = [1, "arguments", 0, "value", "value"]
    check_path(bigcode, [(5, 17), (5, 18), (5, 19), (5, 20), (5, 21), (5, 22), (5, 23)], path)


def test_bc_l5_args_comma():
    path = [1, "arguments", 1, ","]
    check_path(bigcode, [(5, 24)], path)


def test_bc_l5_args_comma_second_formatting():
    path = [1, "arguments", 1, "second_formatting", 0, "value"]
    check_path(bigcode, [(5, 25)], path)


def test_bc_l5_arg2_operator():
    path = [1, "arguments", 2, "**"]
    check_path(bigcode, [(5, 26), (5, 27)], path)


def test_bc_l5_arg2_name():
    path = [1, "arguments", 2, "value", "value"]
    check_path(bigcode, [(5, 28), (5, 29), (5, 30), (5, 31), (5, 32), (5, 33)], path)


def test_bc_l5_right_paren():
    path = [1, ")"]
    check_path(bigcode, [(5, 34)], path)


def test_bc_l5_colon():
    path = [1, ":"]
    check_path(bigcode, [(5, 35)], path)


def test_bc_l5_out_of_scope():
    check_path(bigcode, [(5, 36), (6, 0)], None)


def test_bc_l6_endl():
    path = [1, "value", 0, "indent"]
    check_path(bigcode, [(6, 1), (6, 2), (6, 3), (6, 4)], path)


def test_bc_l6_assign_var():
    path = [1, "value", 1, "target", "value", 0, "value"]
    check_path(bigcode, [(6, 5), (6, 6), (6, 7), (6, 8)], path)


def test_bc_l6_assign_var_dot():
    path = [1, "value", 1, "target", "value", 1, "."]
    check_path(bigcode, [(6, 9)], path)


def test_bc_l6_assign_var_dot_name():
    path = [1, "value", 1, "target", "value", 2, "value"]
    check_path(bigcode, [(6, 10), (6, 11), (6, 12), (6, 13)], path)


def test_bc_l6_assign_first_formatting():
    path = [1, "value", 1, "first_formatting", 0, "value"]
    check_path(bigcode, [(6, 14)], path)


def test_bc_l6_assign_equal():
    path = [1, "value", 1, "="]
    check_path(bigcode, [(6, 15)], path)


def test_bc_l6_assign_second_formatting():
    path = [1, "value", 1, "second_formatting", 0, "value"]
    check_path(bigcode, [(6, 16)], path)


def test_bc_l6_assign_value():
    path = [1, "value", 1, "value", "value"]
    check_path(bigcode, [(6, 17)], path)


def test_bc_l6_out_of_scope():
    check_path(bigcode, [(6, 18), (7, 0)], None)


def test_sc_l1_var():
    path = [0, "target", "value"]
    check_path(splitcode, [(1, 1), (1, 2), (1, 3)], path)


def test_sc_l1_var_win():
    path = [0, "target", "value"]
    check_path(windows_splitcode, [(1, 1), (1, 2), (1, 3)], path)


def test_sc_l1_l2_first_space():
    path = [0, "first_formatting", 0, "value"]
    check_path(splitcode, [(1, 4), (1, 5), (2, 1), (2, 2)], path)


def test_sc_l1_l2_first_space_win():
    path = [0, "first_formatting", 0, "value"]
    check_path(windows_splitcode, [(1, 4), (1, 5), (2, 1), (2, 2)], path)


def test_sc_l1_out_of_scope():
    check_path(splitcode, [(1, 6), (2, 0)], None)


def test_sc_l1_out_of_scope_win():
    check_path(windows_splitcode, [(1, 6), (2, 0)], None)


def test_sc_l2_operator():
    path = [0, "="]
    check_path(splitcode, [(2, 3)], path)


def test_sc_l2_operator_win():
    path = [0, "="]
    check_path(windows_splitcode, [(2, 3)], path)


def test_sc_l2_second_space():
    path = [0, "second_formatting", 0, "value"]
    check_path(splitcode, [(2, 4)], path)


def test_sc_l2_second_space_win():
    path = [0, "second_formatting", 0, "value"]
    check_path(windows_splitcode, [(2, 4)], path)


def test_sc_l2_value():
    path = [0, "value", "value"]
    check_path(splitcode, [(2, 5)], path)


def test_sc_l2_value_win():
    path = [0, "value", "value"]
    check_path(windows_splitcode, [(2, 5)], path)


def test_sc_l2_out_of_scope():
    check_path(splitcode, [(2, 6), (3, 0)], None)


def test_sc_l2_out_of_scope_win():
    check_path(windows_splitcode, [(2, 6), (3, 0)], None)


def test_position_equality():
    assert Position((1, 2)) == Position((1, 2))
    assert Position((1, 2)) == (1, 2)
    assert Position((1, 2)) != Position((2, 1))
    assert Position((1, 2)) != (2, 1)


def test_position_opposite():
    assert Position((1, 2)) == - Position((-1, -2))


def test_position_arithmetic():
    assert Position((1, 2)) + Position((1, 2)) == (2, 4)
    assert Position((1, 2)) + (1, 2) == (2, 4)
    assert Position((1, 2)) - Position((2, 1)) == (-1, 1)
    assert Position((1, 2)) - (2, 1) == (-1, 1)


def test_position_advance():
    position = Position((1, 1))
    position.advance_columns(3)
    assert position == (1, 4)
    position.advance_line()
    assert position == (2, 1)
    position.advance_columns(4)
    assert position == (2, 5)


def test_position_left():
    assert Position((1, 2)).left == (1, 1)


def test_position_right():
    assert Position((1, 2)).right == (1, 3)


def test_postion_around_the_world():
    assert Position((1, 2)) == Position(Position((1, 2)).to_tuple())
