from utils import (create_node_from_token, binary_operator, unitary_operator,
                   comparison, boolean_operator, ternary_operator, assignment,
                   augmented_assignment, tuple_)


def include_operators(pg):
    @pg.production("small_stmt : expr_stmt")
    @pg.production("expr_stmt : testlist")
    @pg.production("testlist : test")
    @pg.production("test : or_test")
    @pg.production("or_test : and_test")
    @pg.production("and_test : not_test")
    @pg.production("not_test : comparison")
    @pg.production("comparison : expr")
    @pg.production("expr : xor_expr")
    @pg.production("xor_expr : and_expr")
    @pg.production("and_expr : shift_expr")
    @pg.production("shift_expr : arith_expr")
    @pg.production("arith_expr : term")
    @pg.production("term : factor")
    @pg.production("factor : power")
    @pg.production("power : atom")
    @pg.production("exprlist : expr")
    def term_factor((level,)):
        return level


    @pg.production("testlist : test testlist_part")
    @pg.production("exprlist : expr exprlist_part")
    def implicit_tuple((test, testlist_part)):
        return tuple_([test] + testlist_part, with_parenthesis=False)


    @pg.production("testlist : test COMMA")
    @pg.production("exprlist : expr COMMA")
    def implicit_tuple_alone((test, comma)):
        tuple_content = [test]
        if comma.before_space:
            tuple_content += [{"type": "space", "value": comma.before_space}]
        tuple_content += [create_node_from_token(comma)]
        return tuple_(tuple_content, with_parenthesis=False)


    @pg.production("testlist_part : COMMA test COMMA?")
    @pg.production("exprlist_part : COMMA expr COMMA?")
    def testlist_part((comma, test, comma2)):
        to_return = []
        if comma.before_space:
            to_return += [{"type": "space", "value": comma.before_space}]
        to_return += [create_node_from_token(comma)]
        if comma.after_space:
            to_return += [{"type": "space", "value": comma.after_space}]
        to_return += [test]
        if comma2 and comma2.before_space:
            to_return += [{"type": "space", "value": comma2.before_space}]
        if comma2:
            to_return += [create_node_from_token(comma2)]
        return to_return


    @pg.production("testlist_part : COMMA test testlist_part")
    @pg.production("exprlist_part : COMMA expr exprlist_part")
    def testlist_part_next((comma, test, testlist_part)):
        to_return = []
        if comma.before_space:
            to_return += [{"type": "space", "value": comma.before_space}]
        to_return += [create_node_from_token(comma)]
        if comma.after_space:
            to_return += [{"type": "space", "value": comma.after_space}]
        to_return += [test] + testlist_part
        return to_return


    @pg.production("expr_stmt : testlist PLUS_EQUAL testlist")
    @pg.production("expr_stmt : testlist MINUS_EQUAL testlist")
    @pg.production("expr_stmt : testlist STAR_EQUAL testlist")
    @pg.production("expr_stmt : testlist SLASH_EQUAL testlist")
    @pg.production("expr_stmt : testlist PERCENT_EQUAL testlist")
    @pg.production("expr_stmt : testlist AMPER_EQUAL testlist")
    @pg.production("expr_stmt : testlist VBAR_EQUAL testlist")
    @pg.production("expr_stmt : testlist CIRCUMFLEX_EQUAL testlist")
    @pg.production("expr_stmt : testlist LEFT_SHIFT_EQUAL testlist")
    @pg.production("expr_stmt : testlist RIGHT_SHIFT_EQUAL testlist")
    @pg.production("expr_stmt : testlist DOUBLE_STAR_EQUAL testlist")
    @pg.production("expr_stmt : testlist DOUBLE_SLASH_EQUAL testlist")
    def augmented_assignment_node((target, operator, value)):
        return augmented_assignment(operator.value[:-1], value, target, operator.before_space, operator.after_space)


    @pg.production("expr_stmt : testlist EQUAL expr_stmt")
    def assignment_node((target, equal, value)):
        return assignment(value, target, equal.before_space, equal.after_space)


    @pg.production("test : or_test IF or_test ELSE test")
    def ternary_operator_node((first, if_, second, else_, third)):
        return ternary_operator(
            second,
            first=first,
            second=third,
            first_space=if_.before_space,
            second_space=if_.after_space,
            third_space=else_.before_space,
            forth_space=else_.after_space,
        )


    @pg.production("or_test : and_test OR or_test")
    @pg.production("and_test : not_test AND and_test")
    def and_or_node((first, operator, second)):
        return boolean_operator(
            operator.value,
            first=first,
            second=second,
            first_space=operator.before_space,
            second_space=operator.after_space,
        )


    @pg.production("not_test : NOT not_test")
    def not_node((not_, comparison)):
        return unitary_operator('not', target=comparison, space=not_.after_space)


    @pg.production("comparison : expr LESS comparison")
    @pg.production("comparison : expr GREATER comparison")
    @pg.production("comparison : expr EQUAL_EQUAL comparison")
    @pg.production("comparison : expr LESS_EQUAL comparison")
    @pg.production("comparison : expr GREATER_EQUAL comparison")
    @pg.production("comparison : expr LESS_GREATER comparison")
    @pg.production("comparison : expr NOT_EQUAL comparison")
    @pg.production("comparison : expr IN comparison")
    @pg.production("comparison : expr IS comparison")
    def comparison_node((expr, comparison_operator, comparison_)):
        return comparison(comparison_operator.value,
                          first=expr,
                          second=comparison_,
                          first_space=comparison_operator.before_space,
                          second_space=comparison_operator.after_space
                          )


    @pg.production("comparison : expr IS NOT comparison")
    @pg.production("comparison : expr NOT IN comparison")
    def comparison_advanced_node((expr, comparison_operator, comparison_operator2, comparison_)):
        return comparison(comparison_operator.value + " " + comparison_operator2.value,
                          first=expr,
                          second=comparison_,
                          first_space=comparison_operator.before_space,
                          second_space=comparison_operator2.after_space,
                          middle_space=comparison_operator.after_space,
                          )


    @pg.production("expr : xor_expr VBAR expr")
    @pg.production("xor_expr : and_expr CIRCUMFLEX xor_expr")
    @pg.production("and_expr : shift_expr AMPER and_expr")
    @pg.production("shift_expr : arith_expr RIGHT_SHIFT shift_expr")
    @pg.production("shift_expr : arith_expr LEFT_SHIFT shift_expr")
    @pg.production("arith_expr : term PLUS arith_expr")
    @pg.production("arith_expr : term MINUS arith_expr")
    @pg.production("term : factor STAR term")
    @pg.production("term : factor SLASH term")
    @pg.production("term : factor PERCENT term")
    @pg.production("term : factor DOUBLE_SLASH term")
    @pg.production("power : atom DOUBLE_STAR factor")
    @pg.production("power : atom DOUBLE_STAR power")
    def binary_operator_node((first, operator, second)):
        return binary_operator(
            operator.value,
            first,
            second,
            first_space=operator.before_space,
            second_space=operator.after_space
        )


    @pg.production("factor : PLUS factor")
    @pg.production("factor : MINUS factor")
    @pg.production("factor : TILDE factor")
    def factor_unitary_operator_space((operator, factor,)):
        return unitary_operator(operator.value, factor, space=operator.after_space)


    @pg.production("power : atomtrailers DOUBLE_STAR factor")
    @pg.production("power : atomtrailers DOUBLE_STAR power")
    def power_atomtrailer_power((atomtrailers, double_star, factor)):
        return binary_operator(
            double_star.value,
            {
                "type": "atomtrailers",
                "value": atomtrailers,
            },
            factor,
            first_space=double_star.before_space,
            second_space=double_star.after_space
        )


    @pg.production("power : atomtrailers")
    def power_atomtrailers((atomtrailers,)):
        return {"type": "atomtrailers", "value": atomtrailers}


    @pg.production("atomtrailers : atom")
    def atomtrailers_atom((atom,)):
        return [atom]


    @pg.production("atomtrailers : atom trailers")
    def atomtrailer((atom, trailers)):
        return [atom] + trailers


    @pg.production("trailers : trailer")
    def trailers((trailer,)):
        return trailer


    @pg.production("trailers : trailers trailer")
    def trailers_trailer((trailers, trailer)):
        return trailers + trailer


    @pg.production("trailer : DOT NAME")
    def trailer((dot, name,)):
        to_return = []
        if dot.before_space:
            to_return += [{"type": "space", "value": dot.before_space}]
        to_return += [create_node_from_token(dot)]
        if dot.after_space:
            to_return += [{"type": "space", "value": dot.after_space}]
        to_return += [create_node_from_token(name)]
        return to_return


    @pg.production("trailer : LEFT_SQUARE_BRACKET RIGHT_SQUARE_BRACKET")
    @pg.production("trailer : LEFT_PARENTHESIS RIGHT_PARENTHESIS")
    def trailer_getitem((left, right)):
        to_return = []
        if left.before_space:
            to_return += [{"type": "space", "value": left.before_space}]
        to_return += [{"type": "getitem" if left.value == "[" else "call", "value": None, "first_space": left.after_space, "second_space": ""}]
        return to_return
