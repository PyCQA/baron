def include_operators(pg):
    @pg.production("old_test : or_test")
    @pg.production("old_test : old_lambdef")
    def old_test((level,)):
        return level

    @pg.production("testlist_safe : old_test comma old_test")
    def testlist_safe((old_test, comma, old_test2)):
        return [old_test, comma, old_test2]

    @pg.production("testlist_safe : old_test comma testlist_safe")
    def testlist_safe_more((old_test, comma, testlist_safe)):
        return [old_test, comma] + testlist_safe

    @pg.production("expr_stmt : testlist augassign_operator testlist")
    @pg.production("expr_stmt : testlist augassign_operator yield_expr")
    def augmented_assignment_node((target, operator, value)):
        return {
            "type": "assignment",
            "first_formatting": operator.hidden_tokens_before,
            "second_formatting": operator.hidden_tokens_after,
            "operator": operator.value[:-1],
            "target": target,
            "value": value
        }

    @pg.production("augassign_operator : PLUS_EQUAL")
    @pg.production("augassign_operator : MINUS_EQUAL")
    @pg.production("augassign_operator : STAR_EQUAL")
    @pg.production("augassign_operator : SLASH_EQUAL")
    @pg.production("augassign_operator : PERCENT_EQUAL")
    @pg.production("augassign_operator : AMPER_EQUAL")
    @pg.production("augassign_operator : VBAR_EQUAL")
    @pg.production("augassign_operator : CIRCUMFLEX_EQUAL")
    @pg.production("augassign_operator : LEFT_SHIFT_EQUAL")
    @pg.production("augassign_operator : RIGHT_SHIFT_EQUAL")
    @pg.production("augassign_operator : DOUBLE_STAR_EQUAL")
    @pg.production("augassign_operator : DOUBLE_SLASH_EQUAL")
    def augassign_operator((operator,)):
        return operator

    @pg.production("expr_stmt : testlist EQUAL yield_expr")
    @pg.production("expr_stmt : testlist EQUAL expr_stmt")
    def assignment_node((target, equal, value)):
        return {
            "type": "assignment",
            "value": value,
            "target": target,
            "first_formatting": equal.hidden_tokens_before,
            "second_formatting": equal.hidden_tokens_after
        }

    @pg.production("test : or_test IF or_test ELSE test")
    def ternary_operator_node((first, if_, second, else_, third)):
        return {
            "type": "ternary_operator",
            "first": first,
            "second": third,
            "value": second,
            "first_formatting": if_.hidden_tokens_before,
            "second_formatting": if_.hidden_tokens_after,
            "third_formatting": else_.hidden_tokens_before,
            "forth_formatting": else_.hidden_tokens_after,
        }

    @pg.production("or_test : and_test OR or_test")
    @pg.production("and_test : not_test AND and_test")
    def and_or_node((first, operator, second)):
        return {
            "type": "boolean_operator",
            "value": operator.value,
            "first": first,
            "second": second,
            "first_formatting": operator.hidden_tokens_before,
            "second_formatting": operator.hidden_tokens_after,
        }

    @pg.production("not_test : NOT not_test")
    def not_node((not_, comparison)):
        return {
            "type": "unitary_operator",
            "value": "not",
            "target": comparison,
            "formatting": not_.hidden_tokens_after
        }

    @pg.production("comparison : expr LESS comparison")
    @pg.production("comparison : expr GREATER comparison")
    @pg.production("comparison : expr EQUAL_EQUAL comparison")
    @pg.production("comparison : expr LESS_EQUAL comparison")
    @pg.production("comparison : expr GREATER_EQUAL comparison")
    @pg.production("comparison : expr NOT_EQUAL comparison")
    @pg.production("comparison : expr IN comparison")
    @pg.production("comparison : expr IS comparison")
    def comparison_node((expr, comparison_operator, comparison_)):
        return {
            "type": "comparison",
            "value": comparison_operator.value,
            "middle_formatting": [],
            "first": expr,
            "second": comparison_,
            "first_formatting": comparison_operator.hidden_tokens_before,
            "second_formatting": comparison_operator.hidden_tokens_after
        }

    @pg.production("comparison : expr IS NOT comparison")
    @pg.production("comparison : expr NOT IN comparison")
    def comparison_advanced_node((expr, comparison_operator, comparison_operator2, comparison_)):
        return {
            "type": "comparison",
            "value": "%s %s" % (
                comparison_operator.value,
                comparison_operator2.value
            ),
            "first": expr,
            "second": comparison_,
            "first_formatting": comparison_operator.hidden_tokens_before,
            "second_formatting": comparison_operator2.hidden_tokens_after,
            "middle_formatting": comparison_operator.hidden_tokens_after,
        }

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
        return {
            "type": "binary_operator",
            "value": operator.value,
            "first": first,
            "second": second,
            "first_formatting": operator.hidden_tokens_before,
            "second_formatting": operator.hidden_tokens_after
        }

    @pg.production("factor : PLUS factor")
    @pg.production("factor : MINUS factor")
    @pg.production("factor : TILDE factor")
    def factor_unitary_operator_space((operator, factor,)):
        return {
            "type": "unitary_operator",
            "value": operator.value,
            "formatting": operator.hidden_tokens_after,
            "target": factor,
        }

    @pg.production("power : atomtrailers DOUBLE_STAR factor")
    @pg.production("power : atomtrailers DOUBLE_STAR power")
    def power_atomtrailer_power((atomtrailers, double_star, factor)):
        return {
            "type": "binary_operator",
            "value": double_star.value,
            "first": {
                "type": "atomtrailers",
                "value": atomtrailers,
            },
            "second": factor,
            "first_formatting": double_star.hidden_tokens_before,
            "second_formatting": double_star.hidden_tokens_after
        }

    @pg.production("power : atomtrailers")
    def power_atomtrailers((atomtrailers,)):
        return {
            "type": "atomtrailers",
            "value": atomtrailers
        }

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
        return [{
            "type": "dot",
            "first_formatting": dot.hidden_tokens_before,
            "second_formatting": dot.hidden_tokens_after,
        },{
            "type": "name",
            "value": name.value,
        }]

    @pg.production("trailer : LEFT_PARENTHESIS argslist RIGHT_PARENTHESIS")
    def trailer_call((left, argslist, right)):
        return [{
            "type": "call",
            "value": argslist,
            "first_formatting": left.hidden_tokens_before,
            "second_formatting": left.hidden_tokens_after,
            "third_formatting": right.hidden_tokens_before,
            "forth_formatting": right.hidden_tokens_after,
        }]

    @pg.production("trailer : LEFT_SQUARE_BRACKET subscript RIGHT_SQUARE_BRACKET")
    @pg.production("trailer : LEFT_SQUARE_BRACKET subscriptlist RIGHT_SQUARE_BRACKET")
    def trailer_getitem_ellipsis((left, subscript, right)):
        return [{
            "type": "getitem",
            "value": subscript,
            "first_formatting": left.hidden_tokens_before,
            "second_formatting": left.hidden_tokens_after,
            "third_formatting": right.hidden_tokens_before,
            "forth_formatting": right.hidden_tokens_after,
        }]

    @pg.production("subscript : DOT DOT DOT")
    def subscript_ellipsis((dot1, dot2, dot3)):
        return {
            "type": "ellipsis",
            "first_formatting": dot1.hidden_tokens_after,
            "second_formatting": dot2.hidden_tokens_after,
        }

    @pg.production("subscript : test")
    @pg.production("subscript : slice")
    def subscript_test((test,)):
        return test

    @pg.production("slice : COLON")
    def slice((colon,)):
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "forth_formatting": [],
        }

    @pg.production("slice : COLON COLON")
    def slice_colon((colon, colon2)):
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON")
    def slice_lower((test, colon,)):
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "forth_formatting": [],
        }

    @pg.production("slice : test COLON COLON")
    def slice_lower_colon_colon((test, colon, colon2)):
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON test")
    def slice_upper((colon, test,)):
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "forth_formatting": [],
        }

    @pg.production("slice : COLON test COLON")
    def slice_upper_colon((colon, test, colon2)):
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON COLON test")
    def slice_step((colon, colon2, test)):
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": test,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON test")
    def slice_lower_upper((test, colon, test2,)):
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "forth_formatting": [],
        }

    @pg.production("slice : test COLON test COLON")
    def slice_lower_upper_colon((test, colon, test2, colon2)):
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON COLON test")
    def slice_lower_step((test, colon, colon2, test2)):
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": test2,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON test COLON test")
    def slice_upper_step((colon, test, colon2, test2)):
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": test2,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON test COLON test")
    def slice_lower_upper_step((test, colon, test2, colon2, test3)):
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": test3,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "forth_formatting": colon2.hidden_tokens_after,
        }
