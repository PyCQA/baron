from .parser import ParsingError


def include_operators(pg):
    @pg.production("old_test : or_test")
    @pg.production("old_test : old_lambdef")
    def old_test(pack):
        (level,) = pack
        return level

    @pg.production("testlist_safe : old_test comma old_test")
    def testlist_safe(pack):
        (old_test, comma, old_test2) = pack
        return [old_test, comma, old_test2]

    @pg.production("testlist_safe : old_test comma testlist_safe")
    def testlist_safe_more(pack):
        (old_test, comma, testlist_safe) = pack
        return [old_test, comma] + testlist_safe

    @pg.production("expr_stmt : test COLON test")
    def alone_annotation(pack):
        target, colon, annotation = pack
        return {
            "type": "standalone_annotation",
            "target": target,
            "annotation": annotation,  # not called "value" in case someone
                                       # wants to work on both assignment and
                                       # standalone annotations
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
        }

    @pg.production("expr_stmt : test COLON test EQUAL test")
    def augmented_assignment_node(pack):
        target, colon, annotation, equal, test = pack
        return {
            "type": "assignment",
            "first_formatting": equal.hidden_tokens_before if equal else [],
            "second_formatting": equal.hidden_tokens_after if equal else [],
            "target": target,
            "value": test,
            "operator": "",
            "annotation": annotation,
            "annotation_first_formatting": colon.hidden_tokens_before,
            "annotation_second_formatting": colon.hidden_tokens_after,
        }

    @pg.production("expr_stmt : testlist_star_expr augassign_operator testlist")
    @pg.production("expr_stmt : testlist_star_expr augassign_operator yield_expr")
    def augmented_assignment_node_2(pack):
        (target, operator, value) = pack
        return {
            "type": "assignment",
            "first_formatting": operator.hidden_tokens_before,
            "second_formatting": operator.hidden_tokens_after,
            "operator": operator.value[:-1],
            "target": target,
            "value": value,
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }

    @pg.production("test_or_star_expr : test")
    @pg.production("test_or_star_expr : star_expr")
    def test_or_star_expr(pack):
        return pack[0]

    @pg.production("star_expr : STAR expr")
    def star_expr(pack):
        star, expr = pack
        return {
            "type": "star_expression",
            "formatting": star.hidden_tokens_after,
            "value": expr,
        }

    @pg.production("augassign_operator : PLUS_EQUAL")
    @pg.production("augassign_operator : MINUS_EQUAL")
    @pg.production("augassign_operator : STAR_EQUAL")
    @pg.production("augassign_operator : SLASH_EQUAL")
    @pg.production("augassign_operator : PERCENT_EQUAL")
    @pg.production("augassign_operator : AMPER_EQUAL")
    @pg.production("augassign_operator : AT_EQUAL")
    @pg.production("augassign_operator : VBAR_EQUAL")
    @pg.production("augassign_operator : CIRCUMFLEX_EQUAL")
    @pg.production("augassign_operator : LEFT_SHIFT_EQUAL")
    @pg.production("augassign_operator : RIGHT_SHIFT_EQUAL")
    @pg.production("augassign_operator : DOUBLE_STAR_EQUAL")
    @pg.production("augassign_operator : DOUBLE_SLASH_EQUAL")
    def augassign_operator(pack):
        (operator,) = pack
        return operator

    @pg.production("expr_stmt : testlist_star_expr EQUAL yield_expr")
    @pg.production("expr_stmt : testlist_star_expr EQUAL expr_stmt")
    def assignment_node(pack):
        (target, equal, value) = pack
        return {
            "type": "assignment",
            "operator": "",
            "value": value,
            "target": target,
            "first_formatting": equal.hidden_tokens_before,
            "second_formatting": equal.hidden_tokens_after,
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }

    @pg.production("test : or_test IF or_test ELSE test")
    def ternary_operator_node(pack):
        (first, if_, second, else_, third) = pack
        return {
            "type": "ternary_operator",
            "first": first,
            "second": third,
            "value": second,
            "first_formatting": if_.hidden_tokens_before,
            "second_formatting": if_.hidden_tokens_after,
            "third_formatting": else_.hidden_tokens_before,
            "fourth_formatting": else_.hidden_tokens_after,
        }

    @pg.production("or_test : and_test OR or_test")
    @pg.production("and_test : not_test AND and_test")
    def and_or_node(pack):
        (first, operator, second) = pack
        return {
            "type": "boolean_operator",
            "value": operator.value,
            "first": first,
            "second": second,
            "first_formatting": operator.hidden_tokens_before,
            "second_formatting": operator.hidden_tokens_after,
        }

    @pg.production("not_test : NOT not_test")
    def not_node(pack):
        (not_, comparison) = pack
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
    def comparison_node(pack):
        (expr, comparison_operator, comparison_) = pack
        return {
            "type": "comparison",
            "first": expr,
            "value": {
                "type": "comparison_operator",
                "first": comparison_operator.value,
                "second": "",
                "formatting": [],
            },
            "second": comparison_,
            "first_formatting": comparison_operator.hidden_tokens_before,
            "second_formatting": comparison_operator.hidden_tokens_after
        }

    @pg.production("comparison : expr IS NOT comparison")
    @pg.production("comparison : expr NOT IN comparison")
    def comparison_advanced_node(pack):
        (expr, comparison_operator, comparison_operator2, comparison_) = pack
        return {
            "type": "comparison",
            "value": {
                "type": "comparison_operator",
                "first": comparison_operator.value,
                "second": comparison_operator2.value,
                "formatting": comparison_operator.hidden_tokens_after
            },
            "first": expr,
            "second": comparison_,
            "first_formatting": comparison_operator.hidden_tokens_before,
            "second_formatting": comparison_operator2.hidden_tokens_after,
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
    @pg.production("term : factor AT term")
    @pg.production("power : atom DOUBLE_STAR factor")
    @pg.production("power : atom DOUBLE_STAR power")
    def binary_operator_node(pack):
        (first, operator, second) = pack
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
    def factor_unitary_operator_space(pack):
        (operator, factor,) = pack
        return {
            "type": "unitary_operator",
            "value": operator.value,
            "formatting": operator.hidden_tokens_after,
            "target": factor,
        }

    @pg.production("power : atomtrailers DOUBLE_STAR factor")
    @pg.production("power : atomtrailers DOUBLE_STAR power")
    def power_atomtrailer_power(pack):
        (atomtrailers, double_star, factor) = pack
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
    def power_atomtrailers(pack):
        (atomtrailers,) = pack
        return {
            "type": "atomtrailers",
            "value": atomtrailers
        }

    @pg.production("power : NAME SPACE atomtrailers")
    def power_atomtrailers_await(pack):
        (await_, space, atomtrailers,) = pack

        if await_.value != "await":
            raise ParsingError("The only possible keyword before an atomtrailers is 'await', not '%s'" % await_.value)

        return {
            "type": "await",
            "formatting": [{'type': 'space', 'value': space.value}],
            "value": {
                "type": "atomtrailers",
                "value": atomtrailers,
            }
        }

    @pg.production("atomtrailers : atom")
    def atomtrailers_atom(pack):
        (atom,) = pack
        return [atom]

    @pg.production("atomtrailers : atom trailers")
    def atomtrailer(pack):
        (atom, trailers) = pack
        return [atom] + trailers

    @pg.production("trailers : trailer")
    def trailers(pack):
        (trailer,) = pack
        return trailer

    @pg.production("trailers : trailers trailer")
    def trailers_trailer(pack):
        (trailers, trailer) = pack
        return trailers + trailer

    @pg.production("trailer : DOT NAME")
    def trailer(pack):
        (dot, name,) = pack
        return [{
            "type": "dot",
            "first_formatting": dot.hidden_tokens_before,
            "second_formatting": dot.hidden_tokens_after,
        }, {
            "type": "name",
            "value": name.value,
        }]

    @pg.production("trailer : LEFT_PARENTHESIS argslist RIGHT_PARENTHESIS")
    def trailer_call(pack):
        (left, argslist, right) = pack
        return [{
            "type": "call",
            "value": argslist,
            "first_formatting": left.hidden_tokens_before,
            "second_formatting": left.hidden_tokens_after,
            "third_formatting": right.hidden_tokens_before,
            "fourth_formatting": right.hidden_tokens_after,
        }]

    @pg.production("trailer : LEFT_SQUARE_BRACKET subscript RIGHT_SQUARE_BRACKET")
    @pg.production("trailer : LEFT_SQUARE_BRACKET subscriptlist RIGHT_SQUARE_BRACKET")
    def trailer_getitem_ellipsis(pack):
        (left, subscript, right) = pack
        return [{
            "type": "getitem",
            "value": subscript,
            "first_formatting": left.hidden_tokens_before,
            "second_formatting": left.hidden_tokens_after,
            "third_formatting": right.hidden_tokens_before,
            "fourth_formatting": right.hidden_tokens_after,
        }]

    @pg.production("subscript : ELLIPSIS")
    @pg.production("atom : ELLIPSIS")
    def subscript_ellipsis(pack):
        ellipsis = pack[0]
        return {
            "type": "ellipsis",
            "first_formatting": ellipsis.hidden_tokens_after,
            "second_formatting": ellipsis.hidden_tokens_after,
        }

    @pg.production("subscript : test")
    @pg.production("subscript : slice")
    def subscript_test(pack):
        (test,) = pack
        return test

    @pg.production("slice : COLON")
    def slice(pack):
        (colon,) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "fourth_formatting": [],
        }

    @pg.production("slice : COLON COLON")
    def slice_colon(pack):
        (colon, colon2) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON")
    def slice_lower(pack):
        (test, colon,) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "fourth_formatting": [],
        }

    @pg.production("slice : test COLON COLON")
    def slice_lower_colon_colon(pack):
        (test, colon, colon2) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON test")
    def slice_upper(pack):
        (colon, test,) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "fourth_formatting": [],
        }

    @pg.production("slice : COLON test COLON")
    def slice_upper_colon(pack):
        (colon, test, colon2) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON COLON test")
    def slice_step(pack):
        (colon, colon2, test) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": {},
            "step": test,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON test")
    def slice_lower_upper(pack):
        (test, colon, test2,) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": {},
            "has_two_colons": False,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": [],
            "fourth_formatting": [],
        }

    @pg.production("slice : test COLON test COLON")
    def slice_lower_upper_colon(pack):
        (test, colon, test2, colon2) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": {},
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON COLON test")
    def slice_lower_step(pack):
        (test, colon, colon2, test2) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": {},
            "step": test2,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : COLON test COLON test")
    def slice_upper_step(pack):
        (colon, test, colon2, test2) = pack
        return {
            "type": "slice",
            "lower": {},
            "upper": test,
            "step": test2,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }

    @pg.production("slice : test COLON test COLON test")
    def slice_lower_upper_step(pack):
        (test, colon, test2, colon2, test3) = pack
        return {
            "type": "slice",
            "lower": test,
            "upper": test2,
            "step": test3,
            "has_two_colons": True,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "third_formatting": colon2.hidden_tokens_before,
            "fourth_formatting": colon2.hidden_tokens_after,
        }
