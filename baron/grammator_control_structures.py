def include_control_structures(pg):
    @pg.production("try_stmt : TRY COLON suite excepts")
    def try_excepts_stmt((try_, colon, suite, excepts)):
        return [{
            "type": "try",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "else": {},
            "finally": {},
            "excepts": excepts,
        }]

    @pg.production("try_stmt : TRY COLON suite excepts else_stmt")
    def try_excepts_else_stmt((try_, colon, suite, excepts, else_stmt)):
        return [{
            "type": "try",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "else": else_stmt,
            "finally": {},
            "excepts": excepts,
        }]

    @pg.production("try_stmt : TRY COLON suite excepts finally_stmt")
    def try_excepts_finally_stmt((try_, colon, suite, excepts, finally_stmt)):
        return [{
            "type": "try",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "else": {},
            "finally": finally_stmt,
            "excepts": excepts,
        }]

    @pg.production("try_stmt : TRY COLON suite excepts else_stmt finally_stmt")
    def try_excepts_else_finally_stmt((try_, colon, suite, excepts, else_stmt, finally_stmt)):
        return [{
            "type": "try",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "else": else_stmt,
            "finally": finally_stmt,
            "excepts": excepts,
        }]

    @pg.production("try_stmt : TRY COLON suite finally_stmt")
    def try_stmt((try_, colon, suite, finally_stmt)):
        return [{
            "type": "try",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "else": {},
            "finally": finally_stmt,
            "excepts": [],
        }]

    @pg.production("excepts : excepts except_stmt")
    def excepts((excepts_, except_stmt)):
        return excepts_ + except_stmt

    @pg.production("excepts : except_stmt")
    def excepts_except_stmt((except_stmt,)):
        return except_stmt

    @pg.production("except_stmt : EXCEPT test AS test COLON suite")
    def except_as_stmt((except_, test, as_, test2, colon, suite)):
        return [{
            "type": "except",
            "first_formatting": except_.hidden_tokens_after,
            "second_formatting": as_.hidden_tokens_before,
            "third_formatting": as_.hidden_tokens_after,
            "forth_formatting": colon.hidden_tokens_before,
            "fith_formatting": colon.hidden_tokens_after,
            "delimiteur": "as",
            "target": test2,
            "exception": test,
            "value": suite
        }]

    @pg.production("except_stmt : EXCEPT test COMMA test COLON suite")
    def except_comma_stmt((except_, test, comma, test2, colon, suite)):
        return [{
            "type": "except",
            "first_formatting": except_.hidden_tokens_after,
            "second_formatting": comma.hidden_tokens_before,
            "third_formatting": comma.hidden_tokens_after,
            "forth_formatting": colon.hidden_tokens_before,
            "fith_formatting": colon.hidden_tokens_after,
            "delimiteur": ",",
            "target": test2,
            "exception": test,
            "value": suite
        }]

    @pg.production("except_stmt : EXCEPT COLON suite")
    def except_stmt_empty((except_, colon, suite)):
        return [{
            "type": "except",
            "first_formatting": except_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": colon.hidden_tokens_before,
            "fith_formatting": colon.hidden_tokens_after,
            "delimiteur": "",
            "target": {},
            "exception": {},
            "value": suite
        }]

    @pg.production("except_stmt : EXCEPT test COLON suite")
    def except_stmt((except_, test, colon, suite)):
        return [{
            "type": "except",
            "first_formatting": except_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": colon.hidden_tokens_before,
            "fith_formatting": colon.hidden_tokens_after,
            "delimiteur": "",
            "target": {},
            "exception": test,
            "value": suite
        }]

    @pg.production("finally_stmt : FINALLY COLON suite")
    def finally_stmt((finally_, colon, suite)):
        return {
            "type": "finally",
            "value": suite,
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
        }

    @pg.production("else_stmt : ELSE COLON suite")
    def else_stmt((else_, colon, suite)):
        return {
            "type": "else",
            "value": suite,
            "first_formatting": else_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_after,
        }

    @pg.production("for_stmt : FOR exprlist IN testlist COLON suite")
    def for_stmt((for_, exprlist, in_, testlist, colon, suite),):
        return [{
                 "type": "for",
                 "value": suite,
                 "iterator": exprlist,
                 "target": testlist,
                 "else": {},
                 "first_formatting": for_.hidden_tokens_after,
                 "second_formatting": in_.hidden_tokens_before,
                 "third_formatting": in_.hidden_tokens_after,
                 "forth_formatting": colon.hidden_tokens_before,
                 "fith_formatting": colon.hidden_tokens_after,
               }]

    @pg.production("for_stmt : FOR exprlist IN testlist COLON suite else_stmt")
    def for_else_stmt((for_, exprlist, in_, testlist, colon, suite, else_stmt),):
        return [{
                 "type": "for",
                 "value": suite,
                 "iterator": exprlist,
                 "target": testlist,
                 "else": else_stmt,
                 "first_formatting": for_.hidden_tokens_after,
                 "second_formatting": in_.hidden_tokens_before,
                 "third_formatting": in_.hidden_tokens_after,
                 "forth_formatting": colon.hidden_tokens_before,
                 "fith_formatting": colon.hidden_tokens_after,
               }]

    @pg.production("while_stmt : WHILE test COLON suite")
    def while_stmt((while_, test, colon, suite)):
        return [{
                 "type": "while",
                 "value": suite,
                 "test": test,
                 "else": {},
                 "first_formatting": while_.hidden_tokens_after,
                 "second_formatting": colon.hidden_tokens_before,
                 "third_formatting": colon.hidden_tokens_after,
               }]

    @pg.production("while_stmt : WHILE test COLON suite else_stmt")
    def while_stmt_else((while_, test, colon, suite, else_stmt)):
        return [{
                 "type": "while",
                 "value": suite,
                 "test": test,
                 "else": else_stmt,
                 "first_formatting": while_.hidden_tokens_after,
                 "second_formatting": colon.hidden_tokens_before,
                 "third_formatting": colon.hidden_tokens_after,
               }]

    @pg.production("if_stmt : IF test COLON suite")
    def if_stmt((if_, test, colon, suite)):
        return [{
                "type": "ifelseblock",
                "value": [{
                           "type": "if",
                           "value": suite,
                           "test": test,
                           "first_formatting": if_.hidden_tokens_after,
                           "second_formatting": colon.hidden_tokens_before,
                           "third_formatting": colon.hidden_tokens_after,
                          }]
               }]

    @pg.production("if_stmt : IF test COLON suite elifs")
    def if_elif_stmt((if_, test, colon, suite, elifs)):
        return [{
                "type": "ifelseblock",
                "value": [{
                           "type": "if",
                           "value": suite,
                           "test": test,
                           "first_formatting": if_.hidden_tokens_after,
                           "second_formatting": colon.hidden_tokens_before,
                           "third_formatting": colon.hidden_tokens_after,
                          }] + elifs
               }]

    @pg.production("elifs : elifs ELIF test COLON suite")
    def elifs_elif((elifs, elif_, test, colon, suite),):
        return elifs + [{
            "type": "elif",
            "first_formatting": elif_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "value": suite,
            "test": test,
        }]

    @pg.production("elifs : ELIF test COLON suite")
    def elif_((elif_, test, colon, suite),):
        return [{
            "type": "elif",
            "first_formatting": elif_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "value": suite,
            "test": test,
        }]

    @pg.production("if_stmt : IF test COLON suite else_stmt")
    def if_else_stmt((if_, test, colon, suite, else_stmt)):
        return [{
                "type": "ifelseblock",
                "value": [{
                           "type": "if",
                           "value": suite,
                           "test": test,
                           "first_formatting": if_.hidden_tokens_after,
                           "second_formatting": colon.hidden_tokens_before,
                           "third_formatting": colon.hidden_tokens_after,
                          }, else_stmt]
               }]

    @pg.production("if_stmt : IF test COLON suite elifs else_stmt")
    def if_elif_else_stmt((if_, test, colon, suite, elifs, else_stmt)):
        return [{
                "type": "ifelseblock",
                "value": [{
                           "type": "if",
                           "value": suite,
                           "test": test,
                           "first_formatting": if_.hidden_tokens_after,
                           "second_formatting": colon.hidden_tokens_before,
                           "third_formatting": colon.hidden_tokens_after,
                          }] + elifs + [else_stmt]
               }]
