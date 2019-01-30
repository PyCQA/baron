from .utils import create_node_from_token


def include_primivites(pg, print_function):
    if not print_function:
        @pg.production("print_stmt : PRINT")
        def print_stmt_empty(pack):
            (print_,) = pack
            return {
                "type": "print",
                "value": [],
                "destination": None,
                "destination_formatting": [],
                "formatting": [],
            }

        @pg.production("print_stmt : PRINT testlist")
        def print_stmt(pack):
            (print_, testlist) = pack
            return {
                "type": "print",
                "value": testlist["value"] if testlist["type"] == "tuple" and testlist["with_parenthesis"] is False else [testlist],
                "destination": None,
                "destination_formatting": [],
                "formatting": print_.hidden_tokens_after,
            }

        @pg.production("print_stmt : PRINT RIGHT_SHIFT test")
        def print_stmt_redirect(pack):
            (print_, right_shift, test) = pack
            return {
                "type": "print",
                "value": [],
                "destination": test,
                "destination_formatting": right_shift.hidden_tokens_after,
                "formatting": print_.hidden_tokens_after,
            }

        @pg.production("print_stmt : PRINT RIGHT_SHIFT test COMMA testlist")
        def print_stmt_redirect_testlist(pack):
            (print_, right_shift, test, comma, testlist) = pack
            value = [{
                "type": "comma",
                "first_formatting": comma.hidden_tokens_before,
                "second_formatting": comma.hidden_tokens_after,
            }]
            value += testlist["value"] if testlist["type"] == "tuple" else [testlist]
            return {
                "type": "print",
                "value": value,
                "destination": test,
                "destination_formatting": right_shift.hidden_tokens_after,
                "formatting": print_.hidden_tokens_after,
            }

        @pg.production("assert_stmt : EXEC expr")
        def exec_stmt(pack):
            (exec_, expr) = pack
            return {
                "type": "exec",
                "value": expr,
                "globals": None,
                "locals": None,
                "first_formatting": exec_.hidden_tokens_after,
                "second_formatting": [],
                "third_formatting": [],
                "fourth_formatting": [],
                "fifth_formatting": []
            }

        @pg.production("assert_stmt : EXEC expr IN test")
        def exec_stmt_in(pack):
            (exec_, expr, in_, test) = pack
            return {
                "type": "exec",
                "value": expr,
                "globals": test,
                "locals": None,
                "first_formatting": exec_.hidden_tokens_after,
                "second_formatting": in_.hidden_tokens_before,
                "third_formatting": in_.hidden_tokens_after,
                "fourth_formatting": [],
                "fifth_formatting": []
            }

        @pg.production("assert_stmt : EXEC expr IN test COMMA test")
        def exec_stmt_in_comma(pack):
            (exec_, expr, in_, test, comma, test2) = pack
            return {
                "type": "exec",
                "value": expr,
                "globals": test,
                "locals": test2,
                "first_formatting": exec_.hidden_tokens_after,
                "second_formatting": in_.hidden_tokens_before,
                "third_formatting": in_.hidden_tokens_after,
                "fourth_formatting": comma.hidden_tokens_before,
                "fifth_formatting": comma.hidden_tokens_after
            }

    @pg.production("flow_stmt : return_stmt")
    @pg.production("flow_stmt : break_stmt")
    @pg.production("flow_stmt : continue_stmt")
    @pg.production("flow_stmt : yield_stmt")
    @pg.production("yield_stmt : yield_expr")
    def flow(pack):
        (flow_stmt,) = pack
        return flow_stmt

    @pg.production("return_stmt : RETURN")
    def return_empty(pack):
        (token,) = pack
        return {
            "type": token.name.lower(),
            "value": None,
            "formatting": token.hidden_tokens_after,
        }

    @pg.production("yield_expr : YIELD")
    def yield_expr(pack):
        (yield_,) = pack
        return {
            "type": yield_.name.lower(),
            "value": None,
            "formatting": yield_.hidden_tokens_after,
        }

    @pg.production("break_stmt : BREAK")
    @pg.production("continue_stmt : CONTINUE")
    @pg.production("pass_stmt : PASS")
    def break_stmt(pack):
        (token,) = pack
        return {"type": token.name.lower()}

    @pg.production("raise_stmt : RAISE")
    def raise_stmt_empty(pack):
        (raise_,) = pack
        return {
            "type": "raise",
            "value": None,
            "instance": None,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "comma_or_from": None,
        }

    @pg.production("raise_stmt : RAISE test")
    def raise_stmt(pack):
        (raise_, test) = pack
        return {
            "type": "raise",
            "value": test,
            "instance": None,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": [],
            "comma_or_from": None,
        }

    @pg.production("raise_stmt : RAISE test FROM test")
    def raise_stmt_from(pack):
        (raise_, test, from_, test2) = pack
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": from_.hidden_tokens_before,
            "third_formatting": from_.hidden_tokens_after,
            "fourth_formatting": [],
            "fifth_formatting": [],
            "comma_or_from": "from",
        }

    @pg.production("raise_stmt : RAISE test COMMA test")
    def raise_stmt_instance(pack):
        (raise_, test, comma, test2) = pack
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after,
            "fourth_formatting": [],
            "fifth_formatting": [],
            "comma_or_from": ",",
        }

    @pg.production("raise_stmt : RAISE test COMMA test COMMA test")
    def raise_stmt_instance_traceback(pack):
        (raise_, test, comma, test2, comma2, test3) = pack
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": test3,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after,
            "fourth_formatting": comma2.hidden_tokens_before,
            "fifth_formatting": comma2.hidden_tokens_after,
            "comma_or_from": ",",
        }

    @pg.production("assert_stmt : ASSERT test")
    def assert_stmt(pack):
        (assert_, test) = pack
        return {
            "type": "assert",
            "value": test,
            "message": None,
            "first_formatting": assert_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": []
        }

    @pg.production("assert_stmt : ASSERT test COMMA test")
    def assert_stmt_message(pack):
        (assert_, test, comma, test2) = pack
        return {
            "type": "assert",
            "value": test,
            "message": test2,
            "first_formatting": assert_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after
        }

    @pg.production("global_stmt : GLOBAL names")
    def global_stmt(pack):
        (global_, names) = pack
        return {
            "type": "global",
            "formatting": global_.hidden_tokens_after,
            "value": names,
        }

    @pg.production("nonlocal_stmt : NONLOCAL names")
    def nonlocal_stmt(pack):
        (token, names) = pack
        return {
            "type": "nonlocal",
            "formatting": token.hidden_tokens_after,
            "value": names,
        }

    @pg.production("names : NAME")
    def names_name(pack):
        (name,) = pack
        return [create_node_from_token(name)]

    @pg.production("names : names comma name")
    def names_names_name(pack):
        (names, comma, name,) = pack
        return names + [comma, name]

    @pg.production("return_stmt : RETURN testlist")
    @pg.production("yield_expr : YIELD testlist")
    @pg.production("del_stmt : DEL exprlist")
    def return_testlist(pack):
        (token, testlist) = pack
        return {
            "type": token.name.lower(),
            "value": testlist,
            "formatting": token.hidden_tokens_after,
        }

    @pg.production("yield_expr : YIELD FROM test")
    def yield_from_expr(pack):
        (yield_, from_, test) = pack
        return {
            "type": "yield_from",
            "first_formatting": from_.hidden_tokens_after,
            "value": test,
            "formatting": yield_.hidden_tokens_after,
        }

    @pg.production("lambdef : LAMBDA COLON test")
    @pg.production("old_lambdef : LAMBDA COLON old_test")
    def lambdef(pack):
        (lambda_, colon, test) = pack
        return {
            "type": "lambda",
            "arguments": [],
            "first_formatting": lambda_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "value": test
        }

    @pg.production("lambdef : LAMBDA parameters COLON test")
    @pg.production("old_lambdef : LAMBDA parameters COLON old_test")
    def lambdef_arguments(pack):
        (lambda_, parameters, colon, test) = pack
        return {
            "type": "lambda",
            "arguments": parameters,
            "first_formatting": lambda_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "value": test
        }
