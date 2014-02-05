from utils import create_node_from_token


def include_primivites(pg):
    @pg.production("print_stmt : PRINT")
    def print_stmt_empty((print_,)):
        return {
            "type": "print",
            "value": None,
            "destination": None,
            "destination_space": "",
            "space": "",
        }


    @pg.production("print_stmt : PRINT testlist")
    def print_stmt((print_, testlist)):
        return {
            "type": "print",
            "value": testlist["value"] if testlist["type"] == "tuple" else [testlist],
            "destination": None,
            "destination_space": "",
            "space": print_.after_space,
        }


    @pg.production("print_stmt : PRINT RIGHT_SHIFT test")
    def print_stmt_redirect((print_, right_shift, test)):
        return {
            "type": "print",
            "value": None,
            "destination": test,
            "destination_space": right_shift.after_space,
            "space": print_.after_space,
        }


    @pg.production("print_stmt : PRINT RIGHT_SHIFT test COMMA testlist")
    def print_stmt_redirect_testlist((print_, right_shift, test, comma, testlist)):
        value = []
        if comma.before_space:
            value += [{"type": "space", "value": comma.before_space}]
        value += [create_node_from_token(comma)]
        if comma.after_space:
            value += [{"type": "space", "value": comma.after_space}]
        #print testlist
        value += testlist["value"] if testlist["type"] == "tuple" else [testlist]
        return {
            "type": "print",
            "value": value,
            "destination": test,
            "destination_space": right_shift.after_space,
            "space": print_.after_space,
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
            "space": ""
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
            "first_space": raise_.after_space,
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
        }


    @pg.production("raise_stmt : RAISE test")
    def raise_stmt((raise_, test)):
        return {
            "type": "raise",
            "value": test,
            "instance": None,
            "traceback": None,
            "first_space": raise_.after_space,
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
        }


    @pg.production("raise_stmt : RAISE test COMMA test")
    def raise_stmt_instance((raise_, test, comma, test2)):
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": None,
            "first_space": raise_.after_space,
            "second_space": comma.before_space,
            "third_space": comma.after_space,
            "forth_space": "",
            "fith_space": ""
        }


    @pg.production("raise_stmt : RAISE test COMMA test COMMA test")
    def raise_stmt_instance_traceback((raise_, test, comma, test2, comma2, test3)):
        return {
            "type": "raise",
            "value": test,
            "instance": test2,
            "traceback": test3,
            "first_space": raise_.after_space,
            "second_space": comma.before_space,
            "third_space": comma.after_space,
            "forth_space": comma2.before_space,
            "fith_space": comma2.after_space
        }


    @pg.production("assert_stmt : EXEC expr")
    def exec_stmt((exec_, expr)):
        return {
            "type": "exec",
            "value": expr,
            "globals": None,
            "locals": None,
            "first_space": exec_.after_space,
            "second_space": "",
            "third_space": "",
            "forth_space": "",
            "fith_space": ""
        }


    @pg.production("assert_stmt : EXEC expr IN test")
    def exec_stmt_in((exec_, expr, in_, test)):
        return {
            "type": "exec",
            "value": expr,
            "globals": test,
            "locals": None,
            "first_space": exec_.after_space,
            "second_space": in_.before_space,
            "third_space": in_.after_space,
            "forth_space": "",
            "fith_space": ""
        }


    @pg.production("assert_stmt : EXEC expr IN test COMMA test")
    def exec_stmt_in_comma((exec_, expr, in_, test, comma, test2)):
        return {
            "type": "exec",
            "value": expr,
            "globals": test,
            "locals": test2,
            "first_space": exec_.after_space,
            "second_space": in_.before_space,
            "third_space": in_.after_space,
            "forth_space": comma.before_space,
            "fith_space": comma.after_space
        }


    @pg.production("assert_stmt : ASSERT test")
    def assert_stmt((assert_, test)):
        return {
            "type": "assert",
            "value": test,
            "message": None,
            "first_space": assert_.after_space,
            "second_space": "",
            "third_space": ""
        }


    @pg.production("assert_stmt : ASSERT test COMMA test")
    def assert_stmt_message((assert_, test, comma, test2)):
        return {
            "type": "assert",
            "value": test,
            "message": test2,
            "first_space": assert_.after_space,
            "second_space": comma.before_space,
            "third_space": comma.after_space
        }


    @pg.production("global_stmt : GLOBAL names")
    def global_stmt((global_, names)):
        return {
            "type": "global",
            "space": global_.after_space,
            "value": names,
        }


    @pg.production("names : NAME")
    def names_name((name,)):
        return [create_node_from_token(name)]


    @pg.production("names : names COMMA NAME")
    def names_names_name((names, comma, name,)):
        to_return = names
        if comma.before_space:
            to_return += [{"type": "space", "value": comma.before_space}]
        to_return += [create_node_from_token(comma)]
        if comma.after_space:
            to_return += [{"type": "space", "value": comma.after_space}]
        to_return += [create_node_from_token(name)]
        return to_return


    @pg.production("return_stmt : RETURN testlist")
    @pg.production("yield_expr : YIELD testlist")
    @pg.production("del_stmt : DEL exprlist")
    def return_testlist((token, testlist)):
        return {
            "type": token.name.lower(),
            "value": testlist,
            "space": token.after_space,
        }
