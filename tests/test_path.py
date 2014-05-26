from baron.baron import parse
from baron.path import position_to_path, path_to_node, position_to_node
from baron.render import get_node_at_position_in_rendering_list
from baron.utils import string_instance

simplecode = """vara = 1"""


bigcode = """def fun(arg1, arg2): 
    var *= 1

@deco("arg")
def fun2(arg1 = default, **kwargs):
    arg1.attr = 3
"""


splitcode = """var \\\n  = 2"""


def make_path(path, type, pos):
    return {"path": path, "type": type, "position_in_rendering_list": pos}


def check_path(code, line, column, target_path):
    tree = parse(code)
    path = position_to_path(tree, line, column)
    assert path == target_path

    if not path:
        assert position_to_node(tree, line, column) is None
    else:
        node = path_to_node(tree, path)
        assert not isinstance(node, string_instance)
        targetted_child = get_node_at_position_in_rendering_list(node, path['position_in_rendering_list'])
        assert isinstance(targetted_child, string_instance)

        assert position_to_node(tree, line, column) is node


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
    path = make_path([0, "target"], "name", 0)
    check_path(simplecode, 1, 1, path)
    check_path(simplecode, 1, 2, path)
    check_path(simplecode, 1, 3, path)
    check_path(simplecode, 1, 4, path)


def test_sc_assignement_first_formatting():
    path = make_path([0, "first_formatting", 0], "space", 0)
    check_path(simplecode, 1, 5, path)


def test_sc_assignement_operator():
    path = make_path([0], "assignment", 3)
    check_path(simplecode, 1, 6, path)


def test_sc_assignement_second_formatting():
    path = make_path([0, "second_formatting", 0], "space", 0)
    check_path(simplecode, 1, 7, path)


def test_sc_assignement_value():
    path = make_path([0, "value"], "int", 0)
    check_path(simplecode, 1, 8, path)


def test_bc_l1_def():
    path = make_path([0], "funcdef", 1)
    check_path(bigcode, 1, 1, path)
    check_path(bigcode, 1, 2, path)
    check_path(bigcode, 1, 3, path)


def test_bc_l1_def_first_formatting():
    path = make_path([0, "first_formatting", 0], "space", 0)
    check_path(bigcode, 1, 4, path)


def test_bc_l1_def_name():
    path = make_path([0], "funcdef", 3)
    check_path(bigcode, 1, 5, path)
    check_path(bigcode, 1, 6, path)
    check_path(bigcode, 1, 7, path)


def test_bc_l1_def_left_paren():
    path = make_path([0], "funcdef", 5)
    check_path(bigcode, 1, 8, path)


def test_bc_l1_arg1():
    path = make_path([0, "arguments", 0], "def_argument", 0)
    check_path(bigcode, 1, 9, path)
    check_path(bigcode, 1, 10, path)
    check_path(bigcode, 1, 11, path)
    check_path(bigcode, 1, 12, path)


def test_bc_l1_comma():
    path = make_path([0, "arguments", 1], "comma", 1)
    check_path(bigcode, 1, 13, path)


def test_bc_l1_comma_second_formatting():
    path = make_path([0, "arguments", 1, "second_formatting", 0], "space", 0)
    check_path(bigcode, 1, 14, path)


def test_bc_l1_arg2():
    path = make_path([0, "arguments", 2], "def_argument", 0)
    check_path(bigcode, 1, 15, path)
    check_path(bigcode, 1, 16, path)
    check_path(bigcode, 1, 17, path)
    check_path(bigcode, 1, 18, path)


def test_bc_l1_right_paren():
    path = make_path([0], "funcdef", 9)
    check_path(bigcode, 1, 19, path)


def test_bc_l1_colon():
    path = make_path([0], "funcdef", 11)
    check_path(bigcode, 1, 20, path)


def test_bc_l1_space():
    path = make_path([0, "value", 0, "formatting", 0], "space", 0)
    check_path(bigcode, 1, 21, path)


def test_bc_l1_out_of_scope():
    check_path(bigcode, 1, 22, None)
    check_path(bigcode, 2, 0, None)


def test_bc_l2_endl():
    path = make_path([0, "value", 0], "endl", 2)
    check_path(bigcode, 2, 1, path)
    check_path(bigcode, 2, 2, path)
    check_path(bigcode, 2, 3, path)
    check_path(bigcode, 2, 4, path)


def test_bc_l2_assign_var():
    path = make_path([0, "value", 1, "target"], "name", 0)
    check_path(bigcode, 2, 5, path)
    check_path(bigcode, 2, 6, path)
    check_path(bigcode, 2, 7, path)


def test_bc_l2_assign_first_formatting():
    path = make_path([0, "value", 1, "first_formatting", 0], "space", 0)
    check_path(bigcode, 2, 8, path)


def test_bc_l2_assign_operator():
    path = make_path([0, "value", 1], "assignment", 2)
    check_path(bigcode, 2, 9, path)


def test_bc_l2_assign_equal():
    path = make_path([0, "value", 1], "assignment", 3)
    check_path(bigcode, 2, 10, path)


def test_bc_l2_assign_second_formatting():
    path = make_path([0, "value", 1, "second_formatting", 0], "space", 0)
    check_path(bigcode, 2, 11, path)


def test_bc_l2_assign_value():
    path = make_path([0, "value", 1, "value"], "int", 0)
    check_path(bigcode, 2, 12, path)


def test_bc_l2_out_of_scope():
    check_path(bigcode, 2, 13, None)
    check_path(bigcode, 3, 0, None)


def test_bc_l3_empty():
    check_path(bigcode, 3, 1, None)


def test_bc_l4_decorator_at():
    path = make_path([1, "decorators", 0], "decorator", 0)
    check_path(bigcode, 4, 1, path)


def test_bc_l4_decorator_name():
    path = make_path([1, "decorators", 0, "value", "value", 0], "name", 0)
    check_path(bigcode, 4, 2, path)
    check_path(bigcode, 4, 3, path)
    check_path(bigcode, 4, 4, path)
    check_path(bigcode, 4, 5, path)


def test_bc_l4_decorator_left_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 1)
    check_path(bigcode, 4, 6, path)


def test_bc_l4_decorator_arg1():
    path = make_path([1, "decorators", 0, "call", "value", 0, "value"], "string", 1)
    check_path(bigcode, 4, 7, path)
    check_path(bigcode, 4, 8, path)
    check_path(bigcode, 4, 9, path)
    check_path(bigcode, 4, 10, path)
    check_path(bigcode, 4, 11, path)


def test_bc_l4_decorator_right_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 5)
    check_path(bigcode, 4, 12, path)


def test_bc_l4_out_of_scope():
    check_path(bigcode, 4, 13, None)
    check_path(bigcode, 5, 0, None)


def test_bc_l5_def():
    path = make_path([1], "funcdef", 1)
    check_path(bigcode, 5, 1, path)
    check_path(bigcode, 5, 2, path)
    check_path(bigcode, 5, 3, path)


def test_bc_l5_def_first_formatting():
    path = make_path([1, "first_formatting", 0], "space", 0)
    check_path(bigcode, 5, 4, path)


def test_bc_l5_def_name():
    path = make_path([1], "funcdef", 3)
    check_path(bigcode, 5, 5, path)
    check_path(bigcode, 5, 6, path)
    check_path(bigcode, 5, 7, path)
    check_path(bigcode, 5, 8, path)


def test_bc_l5_left_paren():
    path = make_path([1], "funcdef", 5)
    check_path(bigcode, 5, 9, path)


def test_bc_l5_arg1():
    path = make_path([1, "arguments", 0], "def_argument", 0)
    check_path(bigcode, 5, 10, path)
    check_path(bigcode, 5, 11, path)
    check_path(bigcode, 5, 12, path)
    check_path(bigcode, 5, 13, path)


def test_bc_l5_arg1_first_formatting():
    path = make_path([1, "arguments", 0, "first_formatting", 0], "space", 0)
    check_path(bigcode, 5, 14, path)


def test_bc_l5_arg1_equal():
    path = make_path([1, "arguments", 0], "def_argument", 2)
    check_path(bigcode, 5, 15, path)


def test_bc_l5_arg1_second_formatting():
    path = make_path([1, "arguments", 0, "second_formatting", 0], "space", 0)
    check_path(bigcode, 5, 16, path)


def test_bc_l5_arg1_value():
    path = make_path([1, "arguments", 0, "value"], "name", 0)
    check_path(bigcode, 5, 17, path)
    check_path(bigcode, 5, 18, path)
    check_path(bigcode, 5, 19, path)
    check_path(bigcode, 5, 20, path)
    check_path(bigcode, 5, 21, path)
    check_path(bigcode, 5, 22, path)
    check_path(bigcode, 5, 23, path)


def test_bc_l5_args_comma():
    path = make_path([1, "arguments", 1], "comma", 1)
    check_path(bigcode, 5, 24, path)


def test_bc_l5_args_comma_second_formatting():
    path = make_path([1, "arguments", 1, "second_formatting", 0], "space", 0)
    check_path(bigcode, 5, 25, path)


def test_bc_l5_arg2_operator():
    path = make_path([1, "arguments", 2], "dict_argument", 0)
    check_path(bigcode, 5, 26, path)
    check_path(bigcode, 5, 27, path)


def test_bc_l5_arg2_name():
    path = make_path([1, "arguments", 2, "value"], "name", 0)
    check_path(bigcode, 5, 28, path)
    check_path(bigcode, 5, 29, path)
    check_path(bigcode, 5, 30, path)
    check_path(bigcode, 5, 31, path)
    check_path(bigcode, 5, 32, path)
    check_path(bigcode, 5, 33, path)


def test_bc_l5_right_paren():
    path = make_path([1], "funcdef", 9)
    check_path(bigcode, 5, 34, path)


def test_bc_l5_colon():
    path = make_path([1], "funcdef", 11)
    check_path(bigcode, 5, 35, path)


def test_bc_l5_out_of_scope():
    check_path(bigcode, 5, 36, None)
    check_path(bigcode, 6, 0, None)


def test_bc_l6_endl():
    path = make_path([1, "value", 0], "endl", 2)
    check_path(bigcode, 6, 1, path)
    check_path(bigcode, 6, 2, path)
    check_path(bigcode, 6, 3, path)
    check_path(bigcode, 6, 4, path)


def test_bc_l6_assign_var():
    path = make_path([1, "value", 1, "target", "value", 0], "name", 0)
    check_path(bigcode, 6, 5, path)
    check_path(bigcode, 6, 6, path)
    check_path(bigcode, 6, 7, path)
    check_path(bigcode, 6, 8, path)


def test_bc_l6_assign_var_dot():
    path = make_path([1, "value", 1, "target", "value", 1], "dot", 1)
    check_path(bigcode, 6, 9, path)


def test_bc_l6_assign_var_dot_name():
    path = make_path([1, "value", 1, "target", "value", 2], "name", 0)
    check_path(bigcode, 6, 10, path)
    check_path(bigcode, 6, 11, path)
    check_path(bigcode, 6, 12, path)
    check_path(bigcode, 6, 13, path)


def test_bc_l6_assign_first_formatting():
    path = make_path([1, "value", 1, "first_formatting", 0], "space", 0)
    check_path(bigcode, 6, 14, path)


def test_bc_l6_assign_equal():
    path = make_path([1, "value", 1], "assignment", 3)
    check_path(bigcode, 6, 15, path)


def test_bc_l6_assign_second_formatting():
    path = make_path([1, "value", 1, "second_formatting", 0], "space", 0)
    check_path(bigcode, 6, 16, path)


def test_bc_l6_assign_value():
    path = make_path([1, "value", 1, "value"], "int", 0)
    check_path(bigcode, 6, 17, path)


def test_bc_l6_out_of_scope():
    check_path(bigcode, 6, 18, None)
    check_path(bigcode, 7, 0, None)


def test_sc_l1_var():
    path = make_path([0, "target"], "name", 0)
    check_path(splitcode, 1, 1, path)
    check_path(splitcode, 1, 2, path)
    check_path(splitcode, 1, 3, path)


def test_sc_l1_first_space():
    path = make_path([0, "first_formatting", 0], "space", 0)
    check_path(splitcode, 1, 4, path)
    check_path(splitcode, 1, 5, path)


def test_sc_l1_out_of_scope():
    check_path(splitcode, 1, 6, None)
    check_path(splitcode, 2, 0, None)


def test_sc_l2_first_space():
    path = make_path([0, "first_formatting", 0], "space", 0)
    check_path(splitcode, 2, 1, path)
    check_path(splitcode, 2, 2, path)


def test_sc_l2_operator():
    path = make_path([0], "assignment", 3)
    check_path(splitcode, 2, 3, path)


def test_sc_l2_second_space():
    path = make_path([0, "second_formatting", 0], "space", 0)
    check_path(splitcode, 2, 4, path)


def test_sc_l2_value():
    path = make_path([0, "value"], "int", 0)
    check_path(splitcode, 2, 5, path)


def test_sc_l2_out_of_scope():
    check_path(splitcode, 2, 6, None)
    check_path(splitcode, 3, 0, None)

