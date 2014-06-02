from baron.baron import parse
from baron.path import path, PathWalker
from baron.path import position_to_path, path_to_node, position_to_node
from baron.path import path_to_bounding_box, node_to_bounding_box
from baron.render import get_node_at_position_in_rendering_list
from baron.utils import string_instance


simplecode = """vara = 1"""


bigcode = """\
def fun(arg1, arg2): 
    var *= 1

@deco("arg")
def fun2(arg1 = default, **kwargs):
    arg1.attr = 3
"""


splitcode = """var \\\n  = 2"""


funcdefcode = """\
def function(arg1):
    a = 1
    b = 2
"""


classcode = """\
class MyClass(BaseClass):
    def __init__(self, arg1):
        self.a = arg1

    def getA():
        return self.a
"""


def make_path(path, type, pos):
    return {"path": path, "type": type, "position_in_rendering_list": pos}


class PathWalkerTester(PathWalker):
    def __init__(self, paths):
        self.paths = paths

    def before(self, *args):
        self.process_test('>')

    def after(self, *args):
        self.process_test('<')

    def on_leaf(self, *args):
        self.process_test('-')

    def process_test(self, type):
        first = self.paths.pop(0)
        assert first[0] == type
        assert first[1] == self.current_path


def check_path(code, positions, target_path):
    tree = parse(code)

    for (line, column) in positions:
        path = position_to_path(tree, line, column)
        assert path == target_path

        if path is None:
            assert position_to_node(tree, line, column) is None
            return

        node = path_to_node(tree, path)
        assert not isinstance(node, string_instance)

        targetted_child = get_node_at_position_in_rendering_list(node, path['position_in_rendering_list'])
        assert isinstance(targetted_child, string_instance)

        assert position_to_node(tree, line, column) is node

    if target_path is not None:
        bounding_box = (positions[0], positions[-1])
        assert path_to_bounding_box(tree, path) == bounding_box


def test_path_walker_assignment():
    node = parse("a = 1")
    walker = PathWalkerTester([
    ('>', path([0], 'assignment', 0)),
        ('>', path([0, 'target'], 'name', 0)),
            ('-', path([0, 'target', 'value'], 'name', 0)),
        ('<', path([0, 'target'], 'name', 0)),
        ('>', path([0, 'first_formatting'], 'formatting', 1)),
            ('>', path([0, 'first_formatting', 0], 'space', 0)),
                ('-', path([0, 'first_formatting', 0, 'value'], 'space', 0)),
            ('<', path([0, 'first_formatting', 0], 'space', 0)),
        ('<', path([0, 'first_formatting'], 'formatting', 1)),
        ('-', path([0], 'assignment', 3)),
        ('>', path([0, 'second_formatting'], 'formatting', 4)),
            ('>', path([0, 'second_formatting', 0], 'space', 0)),
                ('-', path([0, 'second_formatting', 0, 'value'], 'space', 0)),
            ('<', path([0, 'second_formatting', 0], 'space', 0)),
        ('<', path([0, 'second_formatting'], 'formatting', 4)),
        ('>', path([0, 'value'], 'int', 5)),
            ('-', path([0, 'value', 'value'], 'int', 0)),
        ('<', path([0, 'value'], 'int', 5)),
    ('<', path([0], 'assignment', 0)),
    ])

    walker.walk(node)


def test_bb_name():
    node = parse("var")[0]
    assert node_to_bounding_box(node) == ((1, 1), (1, 3))


def test_bb_string():
    node = parse("\"hello\"")[0]
    assert node_to_bounding_box(node) == ((1, 1), (1, 7))


def test_bb_comment():
    node = parse("# comment")[0]
    assert node_to_bounding_box(node) == ((1, 1), (1, 9))


def test_bb_funcdef():
    node = parse(funcdefcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (3, 9))


def test_bb_class():
    node = parse(classcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (6, 21))


def test_bb_split_assignment():
    node = parse(splitcode)[0]
    assert node_to_bounding_box(node) == ((1, 1), (2, 5))


def test_bb_constant():
    node = "="
    assert node_to_bounding_box(node) == ((1, 1), (1, 1))


def test_bb_constant_2():
    node = "+="
    assert node_to_bounding_box(node) == ((1, 1), (1, 2))


def test_sc_out_of_scope():
    check_path(simplecode, [(-1, 3), (1, -3), (3, 3), (1, 100)], None)


def test_sc_assignement_target():
    path = make_path([0, "target", "value"], "name", 0)
    check_path(simplecode, [(1, 1), (1, 2), (1, 3), (1, 4)], path)


def test_sc_assignement_first_formatting():
    path = make_path([0, "first_formatting", 0, "value"], "space", 0)
    check_path(simplecode, [(1, 5)], path)


def test_sc_assignement_operator():
    path = make_path([0], "assignment", 3)
    check_path(simplecode, [(1, 6)], path)


def test_sc_assignement_second_formatting():
    path = make_path([0, "second_formatting", 0, "value"], "space", 0)
    check_path(simplecode, [(1, 7)], path)


def test_sc_assignement_value():
    path = make_path([0, "value", "value"], "int", 0)
    check_path(simplecode, [(1, 8)], path)


def test_bc_l1_def():
    path = make_path([0], "funcdef", 1)
    check_path(bigcode, [(1, 1), (1, 2), (1, 3)], path)


def test_bc_l1_def_first_formatting():
    path = make_path([0, "first_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(1, 4)], path)


def test_bc_l1_def_name():
    path = make_path([0, "name"], "funcdef", 3)
    check_path(bigcode, [(1, 5), (1, 6), (1, 7)], path)


def test_bc_l1_def_left_paren():
    path = make_path([0], "funcdef", 5)
    check_path(bigcode, [(1, 8)], path)


def test_bc_l1_arg1():
    path = make_path([0, "arguments", 0, "name"], "def_argument", 0)
    check_path(bigcode, [(1, 9), (1, 10), (1, 11), (1, 12)], path)


def test_bc_l1_comma():
    path = make_path([0, "arguments", 1], "comma", 1)
    check_path(bigcode, [(1, 13)], path)


def test_bc_l1_comma_second_formatting():
    path = make_path([0, "arguments", 1, "second_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(1, 14)], path)


def test_bc_l1_arg2():
    path = make_path([0, "arguments", 2, "name"], "def_argument", 0)
    check_path(bigcode, [(1, 15), (1, 16), (1, 17), (1, 18)], path)


def test_bc_l1_right_paren():
    path = make_path([0], "funcdef", 9)
    check_path(bigcode, [(1, 19)], path)


def test_bc_l1_colon():
    path = make_path([0], "funcdef", 11)
    check_path(bigcode, [(1, 20)], path)


def test_bc_l1_space():
    path = make_path([0, "value", 0, "formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(1, 21)], path)


def test_bc_l1_out_of_scope():
    check_path(bigcode, [(1, 22), (2, 0)], None)


def test_bc_l2_endl():
    path = make_path([0, "value", 0, "indent"], "endl", 2)
    check_path(bigcode, [(2, 1), (2, 2), (2, 3), (2, 4)], path)


def test_bc_l2_assign_var():
    path = make_path([0, "value", 1, "target", "value"], "name", 0)
    check_path(bigcode, [(2, 5), (2, 6), (2, 7)], path)


def test_bc_l2_assign_first_formatting():
    path = make_path([0, "value", 1, "first_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(2, 8)], path)


def test_bc_l2_assign_operator():
    path = make_path([0, "value", 1, "operator"], "assignment", 2)
    check_path(bigcode, [(2, 9)], path)


def test_bc_l2_assign_equal():
    path = make_path([0, "value", 1], "assignment", 3)
    check_path(bigcode, [(2, 10)], path)


def test_bc_l2_assign_second_formatting():
    path = make_path([0, "value", 1, "second_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(2, 11)], path)


def test_bc_l2_assign_value():
    path = make_path([0, "value", 1, "value", "value"], "int", 0)
    check_path(bigcode, [(2, 12)], path)


def test_bc_l2_out_of_scope():
    check_path(bigcode, [(2, 13), (3, 0)], None)


def test_bc_l3_empty():
    check_path(bigcode, [(3, 1)], None)


def test_bc_l4_decorator_at():
    path = make_path([1, "decorators", 0], "decorator", 0)
    check_path(bigcode, [(4, 1)], path)


def test_bc_l4_decorator_name():
    path = make_path([1, "decorators", 0, "value", "value", 0, "value"], "name", 0)
    check_path(bigcode, [(4, 2), (4, 3), (4, 4), (4, 5)], path)


def test_bc_l4_decorator_left_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 1)
    check_path(bigcode, [(4, 6)], path)


def test_bc_l4_decorator_arg1():
    path = make_path([1, "decorators", 0, "call", "value", 0, "value", "value"], "string", 1)
    check_path(bigcode, [(4, 7), (4, 8), (4, 9), (4, 10), (4, 11)], path)


def test_bc_l4_decorator_right_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 5)
    check_path(bigcode, [(4, 12)], path)


def test_bc_l4_out_of_scope():
    check_path(bigcode, [(4, 13), (5, 0)], None)


def test_bc_l5_def():
    path = make_path([1], "funcdef", 1)
    check_path(bigcode, [(5, 1), (5, 2), (5, 3)], path)


def test_bc_l5_def_first_formatting():
    path = make_path([1, "first_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(5, 4)], path)


def test_bc_l5_def_name():
    path = make_path([1, "name"], "funcdef", 3)
    check_path(bigcode, [(5, 5), (5, 6), (5, 7), (5, 8)], path)


def test_bc_l5_left_paren():
    path = make_path([1], "funcdef", 5)
    check_path(bigcode, [(5, 9)], path)


def test_bc_l5_arg1():
    path = make_path([1, "arguments", 0, "name"], "def_argument", 0)
    check_path(bigcode, [(5, 10), (5, 11), (5, 12), (5, 13)], path)


def test_bc_l5_arg1_first_formatting():
    path = make_path([1, "arguments", 0, "first_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(5, 14)], path)


def test_bc_l5_arg1_equal():
    path = make_path([1, "arguments", 0], "def_argument", 2)
    check_path(bigcode, [(5, 15)], path)


def test_bc_l5_arg1_second_formatting():
    path = make_path([1, "arguments", 0, "second_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(5, 16)], path)


def test_bc_l5_arg1_value():
    path = make_path([1, "arguments", 0, "value", "value"], "name", 0)
    check_path(bigcode, [(5, 17), (5, 18), (5, 19), (5, 20), (5, 21), (5, 22), (5, 23)], path)


def test_bc_l5_args_comma():
    path = make_path([1, "arguments", 1], "comma", 1)
    check_path(bigcode, [(5, 24)], path)


def test_bc_l5_args_comma_second_formatting():
    path = make_path([1, "arguments", 1, "second_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(5, 25)], path)


def test_bc_l5_arg2_operator():
    path = make_path([1, "arguments", 2], "dict_argument", 0)
    check_path(bigcode, [(5, 26), (5, 27)], path)


def test_bc_l5_arg2_name():
    path = make_path([1, "arguments", 2, "value", "value"], "name", 0)
    check_path(bigcode, [(5, 28), (5, 29), (5, 30), (5, 31), (5, 32), (5, 33)], path)


def test_bc_l5_right_paren():
    path = make_path([1], "funcdef", 9)
    check_path(bigcode, [(5, 34)], path)


def test_bc_l5_colon():
    path = make_path([1], "funcdef", 11)
    check_path(bigcode, [(5, 35)], path)


def test_bc_l5_out_of_scope():
    check_path(bigcode, [(5, 36), (6, 0)], None)


def test_bc_l6_endl():
    path = make_path([1, "value", 0, "indent"], "endl", 2)
    check_path(bigcode, [(6, 1), (6, 2), (6, 3), (6, 4)], path)


def test_bc_l6_assign_var():
    path = make_path([1, "value", 1, "target", "value", 0, "value"], "name", 0)
    check_path(bigcode, [(6, 5), (6, 6), (6, 7), (6, 8)], path)


def test_bc_l6_assign_var_dot():
    path = make_path([1, "value", 1, "target", "value", 1], "dot", 1)
    check_path(bigcode, [(6, 9)], path)


def test_bc_l6_assign_var_dot_name():
    path = make_path([1, "value", 1, "target", "value", 2, "value"], "name", 0)
    check_path(bigcode, [(6, 10), (6, 11), (6, 12), (6, 13)], path)


def test_bc_l6_assign_first_formatting():
    path = make_path([1, "value", 1, "first_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(6, 14)], path)


def test_bc_l6_assign_equal():
    path = make_path([1, "value", 1], "assignment", 3)
    check_path(bigcode, [(6, 15)], path)


def test_bc_l6_assign_second_formatting():
    path = make_path([1, "value", 1, "second_formatting", 0, "value"], "space", 0)
    check_path(bigcode, [(6, 16)], path)


def test_bc_l6_assign_value():
    path = make_path([1, "value", 1, "value", "value"], "int", 0)
    check_path(bigcode, [(6, 17)], path)


def test_bc_l6_out_of_scope():
    check_path(bigcode, [(6, 18), (7, 0)], None)


def test_sc_l1_var():
    path = make_path([0, "target", "value"], "name", 0)
    check_path(splitcode, [(1, 1), (1, 2), (1, 3)], path)


def test_sc_l1_l2_first_space():
    path = make_path([0, "first_formatting", 0, "value"], "space", 0)
    check_path(splitcode, [(1, 4), (1, 5), (2, 1), (2, 2)], path)


def test_sc_l1_out_of_scope():
    check_path(splitcode, [(1, 6), (2, 0)], None)


def test_sc_l2_operator():
    path = make_path([0], "assignment", 3)
    check_path(splitcode, [(2, 3)], path)


def test_sc_l2_second_space():
    path = make_path([0, "second_formatting", 0, "value"], "space", 0)
    check_path(splitcode, [(2, 4)], path)


def test_sc_l2_value():
    path = make_path([0, "value", "value"], "int", 0)
    check_path(splitcode, [(2, 5)], path)


def test_sc_l2_out_of_scope():
    check_path(splitcode, [(2, 6), (3, 0)], None)

