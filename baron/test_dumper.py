#!/usr/bin/python
# -*- coding:Utf-8 -*-

from test_utils import check_dumps


def test_empty():
    check_dumps("")


def test_var():
    check_dumps("hello")


def test_int():
    check_dumps("1")


def test_assign():
    check_dumps("a = 2")


def test_binary_operator():
    check_dumps("z +  42")
    check_dumps("z   -  42")


def test_while():
    check_dumps("while a  : pass")


def test_while_else():
    check_dumps("while a  : pass\nelse : pass")


def test_while_indent():
    check_dumps("while a:\n    pass")


def test_if():
    check_dumps("if a:\n    pass")


def test_if_elif():
    check_dumps("if a: \n    pass\nelif b: pass")


def test_if_elif_else():
    check_dumps("if a: \n    pass\nelif b: pass\nelse :   \n	pouet")


def test_import():
    check_dumps("import  a")


def test_import_madness():
    check_dumps("import  a.B .   c as  saucisse")


def test_from_import():
    check_dumps("from b   import  a  as   rev")


def test_print():
    check_dumps("print pouet")


def test_print_madness():
    check_dumps("print >>  qsd, pouet, zdzd,")


def test_atom_trailers_call():
    check_dumps("a.c(b)")


def test_atom_trailers_call_default():
    check_dumps("caramba(s, b=2)")


def test_string():
    check_dumps("'ama string!'")


def test_funcdef():
    check_dumps("def a  ( ) : pass")


def test_funcdef_indent():
    check_dumps("def a  ( ) : \n    pass")


def test_funcdef_parameter():
    check_dumps("def a  ( b ) : pass")


def test_funcdef_parameter_named():
    check_dumps("def a  ( b  , c = qsd ) : pass")


def test_return():
    check_dumps("return a")


def test_getitem():
    check_dumps("a[ b  ]")


def test_slice_empty():
    check_dumps("a[ :  ]")


def test_slice_classical():
    check_dumps("a[1: 42]")


def test_slice_step():
    check_dumps("a[1: 42:]")
    check_dumps("a[1: 42    :         3]")


def test_unitary_operator():
    check_dumps("- 1")


def test_unicode_string():
    check_dumps("u'pouet'")


def test_raw_string():
    check_dumps("r'pouet'")


def test_unicode_raw_string():
    check_dumps("ur'pouet'")


def test_binary_string():
    check_dumps("b'pouet'")


def test_binary_raw_string():
    check_dumps("br'pouet'")


def test_for():
    check_dumps("for i in pouet : pass")


def test_for_indent():
    check_dumps("for i in pouet : \n    pass")


def test_for_else():
    check_dumps("for i in pouet : pass\nelse: pass")


def test_lambda():
    check_dumps("lambda : x")


def test_lambda_args():
    check_dumps("lambda poeut, hompi_dompi: x")


def test_try_finally():
    check_dumps("try : pass\nfinally : pass")


def test_try_except():
    check_dumps("try : pass\nexcept Exception : pass")


def test_try_except_comma():
    check_dumps("try : pass\nexcept Exception ,   d : pass")


def test_try_except_as():
    check_dumps("try : pass\nexcept Exception     as   d : pass")


def test_try_except_finally():
    check_dumps("try : pass\nexcept Exception : pass\nfinally : pass")


def test_try_except_finally_else():
    check_dumps("try : pass\nexcept Exception : pass\nelse: pouet\nfinally : pass")


def test_comment():
    check_dumps("# pouet")


def test_boolean_operator():
    check_dumps("a and b")


def test_boolean_operator_advanced():
    check_dumps("a and b or c and d")


def test_comparison():
    check_dumps("a < b")


def test_with():
    check_dumps("with a : \n    pass")


def test_with_as():
    check_dumps("with a as b : \n    pass")


def test_dict_empty():
    check_dumps("{   }")


def test_dict_one():
    check_dumps("{ a : b  }")


def test_dict_more():
    check_dumps("{ a : b   ,\n123  :     'pouet'  }")


def test_ternary_operator():
    check_dumps("a   if        b  else      c")


def test_yield():
    check_dumps("yield a")


def test_decorator():
    check_dumps("@pouet\ndef a(): pass")


def test_decorator_call():
    check_dumps("@pouet('pouet')\ndef a(): pass")


def test_class():
    check_dumps("class A: pass")


def test_class_parenthesis():
    check_dumps("class A(): pass")


def test_class_parenthesis_inherit():
    check_dumps("class A(B): pass")


def test_class_parenthesis_inherit_decorated():
    check_dumps("@pouet\nclass A(B): pass")


def test_tuple():
    check_dumps("a  ,  b    , c")


def test_tuple_parenthesis():
    check_dumps("( a  ,  b    , c    )")


def test_return_empty():
    check_dumps("return")


def test_list_empty():
    check_dumps("[   ]")


def test_list():
    check_dumps("[ x ]")


def test_list_more():
    check_dumps("[ x, r, f, e   , e ]")
