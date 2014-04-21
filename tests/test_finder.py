from baron.baron import parse
import baron.finder as finder
import json

simplecode = """vara = 1"""

bigcode = """def fun(arg1, arg2): 
    var *= 1

@deco("arg")
def fun2(arg1 = default, **kwargs):
    arg1.attr = 3
"""


def make_path(path, type, pos):
    return {"path": path, "type": type, "position_in_rendering_list": pos}


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
    path = make_path([0], "assignment", 4)
    check_path(simplecode, 1, 6, path)


def test_sc_assignement_second_formatting():
    path = make_path([0, "second_formatting"], "assignment", 5)
    check_path(simplecode, 1, 7, path)


def test_sc_assignement_target():
    path = make_path([0, "value", "value"], "int", 1)
    check_path(simplecode, 1, 8, path)


def test_bc_l1_def():
    path = make_path([0], "funcdef", 2)
    check_path(bigcode, 1, 1, path)
    check_path(bigcode, 1, 2, path)
    check_path(bigcode, 1, 3, path)


def test_bc_l1_def_first_formatting():
    path = make_path([0, "first_formatting"], "funcdef", 3)
    check_path(bigcode, 1, 4, path)


def test_bc_l1_def_name():
    path = make_path([0, "name"], "funcdef", 4)
    check_path(bigcode, 1, 5, path)
    check_path(bigcode, 1, 6, path)
    check_path(bigcode, 1, 7, path)


def test_bc_l1_def_left_paren():
    path = make_path([0], "funcdef", 6)
    check_path(bigcode, 1, 8, path)


def test_bc_l1_arg1():
    path = make_path([0, "arguments", 0, "name"], "def_argument", 1)
    check_path(bigcode, 1, 9, path)
    check_path(bigcode, 1, 10, path)
    check_path(bigcode, 1, 11, path)
    check_path(bigcode, 1, 12, path)


def test_bc_l1_comma():
    path = make_path([0, "arguments", 1], "comma", 2)
    check_path(bigcode, 1, 13, path)


def test_bc_l1_comma_second_formatting():
    path = make_path([0, "arguments", 1, "second_formatting"], "comma", 3)
    check_path(bigcode, 1, 14, path)


def test_bc_l1_arg2():
    path = make_path([0, "arguments", 2, "name"], "def_argument", 1)
    check_path(bigcode, 1, 15, path)
    check_path(bigcode, 1, 16, path)
    check_path(bigcode, 1, 17, path)
    check_path(bigcode, 1, 18, path)


def test_bc_l1_right_paren():
    path = make_path([0], "funcdef", 10)
    check_path(bigcode, 1, 19, path)


def test_bc_l1_colon():
    path = make_path([0], "funcdef", 12)
    check_path(bigcode, 1, 20, path)


def test_bc_l1_space():
    path = make_path([0, "value", 0, "formatting"], "endl", 1)
    check_path(bigcode, 1, 21, path)


def test_bc_l1_out_of_scope():
    check_path(bigcode, 1, 22, None)
    check_path(bigcode, 2, 0, None)


def test_bc_l2_endl():
    path = make_path([0, "value", 0, "indent"], "endl", 3)
    check_path(bigcode, 2, 1, path)
    check_path(bigcode, 2, 2, path)
    check_path(bigcode, 2, 3, path)
    check_path(bigcode, 2, 4, path)


def test_bc_l2_assign_var():
    path = make_path([0, "value", 1, "target", "value"], "name", 1)
    check_path(bigcode, 2, 5, path)
    check_path(bigcode, 2, 6, path)
    check_path(bigcode, 2, 7, path)


def test_bc_l2_assign_first_formatting():
    path = make_path([0, "value", 1, "first_formatting"], "assignment", 2)
    check_path(bigcode, 2, 8, path)


def test_bc_l2_assign_operator():
    path = make_path([0, "value", 1, "operator"], "assignment", 3)
    check_path(bigcode, 2, 9, path)


def test_bc_l2_assign_equal():
    path = make_path([0, "value", 1], "assignment", 4)
    check_path(bigcode, 2, 10, path)


def test_bc_l2_assign_second_formatting():
    path = make_path([0, "value", 1, "second_formatting"], "assignment", 5)
    check_path(bigcode, 2, 11, path)


def test_bc_l2_assign_value():
    path = make_path([0, "value", 1, "value", "value"], "int", 1)
    check_path(bigcode, 2, 12, path)


def test_bc_l2_out_of_scope():
    check_path(bigcode, 2, 13, None)
    check_path(bigcode, 3, 0, None)


def test_bc_l3_empty():
    check_path(bigcode, 3, 1, None)


def test_bc_l4_decorator_at():
    path = make_path([1, "decorators", 0], "decorator", 1)
    check_path(bigcode, 4, 1, path)


def test_bc_l4_decorator_name():
    path = make_path([1, "decorators", 0, "value", "value", 0, "value"], "name", 1)
    check_path(bigcode, 4, 2, path)
    check_path(bigcode, 4, 3, path)
    check_path(bigcode, 4, 4, path)
    check_path(bigcode, 4, 5, path)


def test_bc_l4_decorator_left_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 2)
    check_path(bigcode, 4, 6, path)


def test_bc_l4_decorator_arg1():
    path = make_path([1, "decorators", 0, "call", "value", 0, "value", "value"], "string", 2)
    check_path(bigcode, 4, 7, path)
    check_path(bigcode, 4, 8, path)
    check_path(bigcode, 4, 9, path)
    check_path(bigcode, 4, 10, path)
    check_path(bigcode, 4, 11, path)


def test_bc_l4_decorator_right_paren():
    path = make_path([1, "decorators", 0, "call"], "call", 6)
    check_path(bigcode, 4, 12, path)


def test_bc_l4_out_of_scope():
    check_path(bigcode, 4, 13, None)
    check_path(bigcode, 5, 0, None)


def test_bc_l5_def():
    path = make_path([1], "funcdef", 2)
    check_path(bigcode, 5, 1, path)
    check_path(bigcode, 5, 2, path)
    check_path(bigcode, 5, 3, path)


def test_bc_l5_def_first_formatting():
    path = make_path([1, "first_formatting"], "funcdef", 3)
    check_path(bigcode, 5, 4, path)


def test_bc_l5_def_name():
    path = make_path([1, "name"], "funcdef", 4)
    check_path(bigcode, 5, 5, path)
    check_path(bigcode, 5, 6, path)
    check_path(bigcode, 5, 7, path)
    check_path(bigcode, 5, 8, path)


def test_bc_l5_left_paren():
    path = make_path([1], "funcdef", 6)
    check_path(bigcode, 5, 9, path)


def test_bc_l5_arg1():
    path = make_path([1, "arguments", 0, "name"], "def_argument", 1)
    check_path(bigcode, 5, 10, path)
    check_path(bigcode, 5, 11, path)
    check_path(bigcode, 5, 12, path)
    check_path(bigcode, 5, 13, path)


def test_bc_l5_arg1_first_formatting():
    path = make_path([1, "arguments", 0, "first_formatting"], "def_argument", 2)
    check_path(bigcode, 5, 14, path)


def test_bc_l5_arg1_equal():
    path = make_path([1, "arguments", 0], "def_argument", 3)
    check_path(bigcode, 5, 15, path)


def test_bc_l5_arg1_second_formatting():
    path = make_path([1, "arguments", 0, "second_formatting"], "def_argument", 4)
    check_path(bigcode, 5, 16, path)


def test_bc_l5_arg1_value():
    path = make_path([1, "arguments", 0, "value", "value"], "name", 1)
    check_path(bigcode, 5, 17, path)
    check_path(bigcode, 5, 18, path)
    check_path(bigcode, 5, 19, path)
    check_path(bigcode, 5, 20, path)
    check_path(bigcode, 5, 21, path)
    check_path(bigcode, 5, 22, path)
    check_path(bigcode, 5, 23, path)


def test_bc_l5_args_comma():
    path = make_path([1, "arguments", 1], "comma", 2)
    check_path(bigcode, 5, 24, path)


def test_bc_l5_args_comma_second_formatting():
    path = make_path([1, "arguments", 1, "second_formatting"], "comma", 3)
    check_path(bigcode, 5, 25, path)


def test_bc_l5_arg2_operator():
    path = make_path([1, "arguments", 2], "dict_argument", 1)
    check_path(bigcode, 5, 26, path)
    check_path(bigcode, 5, 27, path)


def test_bc_l5_arg2_name():
    path = make_path([1, "arguments", 2, "value", "value"], "name", 1)
    check_path(bigcode, 5, 28, path)
    check_path(bigcode, 5, 29, path)
    check_path(bigcode, 5, 30, path)
    check_path(bigcode, 5, 31, path)
    check_path(bigcode, 5, 32, path)
    check_path(bigcode, 5, 33, path)


def test_bc_l5_right_paren():
    path = make_path([1], "funcdef", 10)
    check_path(bigcode, 5, 34, path)


def test_bc_l5_colon():
    path = make_path([1], "funcdef", 12)
    check_path(bigcode, 5, 35, path)


def test_bc_l5_out_of_scope():
    check_path(bigcode, 5, 36, None)
    check_path(bigcode, 6, 0, None)


def test_bc_l6_endl():
    path = make_path([1, "value", 0, "indent"], "endl", 3)
    check_path(bigcode, 6, 1, path)
    check_path(bigcode, 6, 2, path)
    check_path(bigcode, 6, 3, path)
    check_path(bigcode, 6, 4, path)


def test_bc_l6_assign_var():
    path = make_path([1, "value", 1, "target", "value", 0, "value"], "name", 1)
    check_path(bigcode, 6, 5, path)
    check_path(bigcode, 6, 6, path)
    check_path(bigcode, 6, 7, path)
    check_path(bigcode, 6, 8, path)


def test_bc_l6_assign_var_dot():
    path = make_path([1, "value", 1, "target", "value", 1], "dot", 2)
    check_path(bigcode, 6, 9, path)


def test_bc_l6_assign_var_dot_name():
    path = make_path([1, "value", 1, "target", "value", 2, "value"], "name", 1)
    check_path(bigcode, 6, 10, path)
    check_path(bigcode, 6, 11, path)
    check_path(bigcode, 6, 12, path)
    check_path(bigcode, 6, 13, path)


def test_bc_l6_assign_first_formatting():
    path = make_path([1, "value", 1, "first_formatting"], "assignment", 2)
    check_path(bigcode, 6, 14, path)


def test_bc_l6_assign_equal():
    path = make_path([1, "value", 1], "assignment", 4)
    check_path(bigcode, 6, 15, path)


def test_bc_l6_assign_second_formatting():
    path = make_path([1, "value", 1, "second_formatting"], "assignment", 5)
    check_path(bigcode, 6, 16, path)


def test_bc_l6_assign_value():
    path = make_path([1, "value", 1, "value", "value"], "int", 1)
    check_path(bigcode, 6, 17, path)


def test_bc_l6_out_of_scope():
    check_path(bigcode, 6, 18, None)
    check_path(bigcode, 7, 0, None)
