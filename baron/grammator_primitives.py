from utils import create_node_from_token


def include_primivites(pg, print_function):
    if not print_function:
        @pg.production("print_stmt : PRINT")
        def print_stmt_empty((print_,)):
            return {
                "type": "print",
                "value": None,
                "destination": None,
                "destination_formatting": [],
                "formatting": [],
            }


        @pg.production("print_stmt : PRINT testlist")
        def print_stmt((print_, testlist)):
            return {
                "type": "print",
                "value": testlist["value"] if testlist["type"] == "tuple" and testlist["with_parenthesis"] == False else [testlist],
                "destination": None,
                "destination_formatting": [],
                "formatting": print_.hidden_tokens_after,
            }


        @pg.production("print_stmt : PRINT RIGHT_SHIFT test")
        def print_stmt_redirect((print_, right_shift, test)):
            return {
                "type": "print",
                "value": None,
                "destination": test,
                "destination_formatting": right_shift.hidden_tokens_after,
                "formatting": print_.hidden_tokens_after,
            }


        @pg.production("print_stmt : PRINT RIGHT_SHIFT test COMMA testlist")
        def print_stmt_redirect_testlist((print_, right_shift, test, comma, testlist)):
            value = [{
                "type": "comma",
                "first_formatting": comma.hidden_tokens_before,
                "second_formatting": comma.hidden_tokens_after,
            }]
            #print testlist
            value += testlist["value"] if testlist["type"] == "tuple" else [testlist]
            return {
                "type": "print",
                "value": value,
                "destination": test,
                "destination_formatting": right_shift.hidden_tokens_after,
                "formatting": print_.hidden_tokens_after,
            }


    @pg.production("flow_stmt : return_stmt")
    @pg.production("flow_stmt : break_stmt")
    @pg.production("flow_stmt : continue_stmt")
    @pg.production("flow_stmt : yield_stmt")
    @pg.production("yield_stmt : yield_expr")
    def flow((flow_stmt,)):
        return flow_stmt


    @pg.production("return_stmt : RETURN")
    @pg.production("yield_expr : YIELD")
    def return_empty((token,)):
        return {
            "type": token.name.lower(),
            "value": None,
            "formatting": token.hidden_tokens_after,
        }


    @pg.production("break_stmt : BREAK")
    @pg.production("continue_stmt : CONTINUE")
    @pg.production("pass_stmt : PASS")
    def break_stmt((token,)):
        return {"type": token.name.lower()}


    @pg.production("raise_stmt : RAISE")
    def raise_stmt_empty((raise_,)):
        return {
            "type": "raise",
            "value": None,
            "instance": None,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": []
        }


    @pg.production("raise_stmt : RAISE test")
    def raise_stmt((raise_, test)):
        return {
            "type": "raise",
            "value": test,
            "instance": None,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": []
        }


    @pg.production("raise_stmt : RAISE test COMMA test")
    def raise_stmt_instance((raise_, test, comma, test2)):
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": None,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after,
            "forth_formatting": [],
            "fith_formatting": []
        }


    @pg.production("raise_stmt : RAISE test COMMA test COMMA test")
    def raise_stmt_instance_traceback((raise_, test, comma, test2, comma2, test3)):
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": test3,
            "first_formatting": raise_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after,
            "forth_formatting": comma2.hidden_tokens_before,
            "fith_formatting": comma2.hidden_tokens_after
        }


    @pg.production("assert_stmt : EXEC expr")
    def exec_stmt((exec_, expr)):
        return {
            "type": "exec",
            "value": expr,
            "globals": None,
            "locals": None,
            "first_formatting": exec_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "fith_formatting": []
        }


    @pg.production("assert_stmt : EXEC expr IN test")
    def exec_stmt_in((exec_, expr, in_, test)):
        return {
            "type": "exec",
            "value": expr,
            "globals": test,
            "locals": None,
            "first_formatting": exec_.hidden_tokens_after,
            "second_formatting": in_.hidden_tokens_before,
            "third_formatting": in_.hidden_tokens_after,
            "forth_formatting": [],
            "fith_formatting": []
        }


    @pg.production("assert_stmt : EXEC expr IN test COMMA test")
    def exec_stmt_in_comma((exec_, expr, in_, test, comma, test2)):
        return {
            "type": "exec",
            "value": expr,
            "globals": test,
            "locals": test2,
            "first_formatting": exec_.hidden_tokens_after,
            "second_formatting": in_.hidden_tokens_before,
            "third_formatting": in_.hidden_tokens_after,
            "forth_formatting": comma.hidden_tokens_before,
            "fith_formatting": comma.hidden_tokens_after
        }


    @pg.production("assert_stmt : ASSERT test")
    def assert_stmt((assert_, test)):
        return {
            "type": "assert",
            "value": test,
            "message": None,
            "first_formatting": assert_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": []
        }


    @pg.production("assert_stmt : ASSERT test COMMA test")
    def assert_stmt_message((assert_, test, comma, test2)):
        return {
            "type": "assert",
            "value": test,
            "message": test2,
            "first_formatting": assert_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after
        }


    @pg.production("global_stmt : GLOBAL names")
    def global_stmt((global_, names)):
        return {
            "type": "global",
            "formatting": global_.hidden_tokens_after,
            "value": names,
        }


    @pg.production("names : NAME")
    def names_name((name,)):
        return [create_node_from_token(name)]


    @pg.production("names : names comma name")
    def names_names_name((names, comma, name,)):
        return names + [comma, name]


    @pg.production("return_stmt : RETURN testlist")
    @pg.production("yield_expr : YIELD testlist")
    @pg.production("del_stmt : DEL exprlist")
    def return_testlist((token, testlist)):
        return {
            "type": token.name.lower(),
            "value": testlist,
            "formatting": token.hidden_tokens_after,
        }

    @pg.production("lambdef : LAMBDA COLON test")
    @pg.production("old_lambdef : LAMBDA COLON old_test")
    def lambdef((lambda_, colon, test)):
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
    def lambdef_arguments((lambda_, parameters, colon, test)):
        return {
            "type": "lambda",
            "arguments": parameters,
            "first_formatting": lambda_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "value": test
        }
