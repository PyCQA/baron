def include_data_structures(pg):
    # TODO remove left_parenthesis and use LEFT_PARENTHESIS instead
    @pg.production("atom : left_parenthesis testlist_comp RIGHT_PARENTHESIS")
    def tuple((left_parenthesis, testlist_comp, right_parenthesis,)):
        return {
                "type": "tuple",
                "value": testlist_comp,
                "first_formatting": left_parenthesis.hidden_tokens_before,
                "second_formatting": left_parenthesis.hidden_tokens_after,
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "forth_formatting": right_parenthesis.hidden_tokens_after,
                "with_parenthesis": True,
               }


    @pg.production("atom : left_parenthesis test RIGHT_PARENTHESIS")
    def associative_parenthesis((left_parenthesis, test, right_parenthesis,)):
        return {
                "type": "associative_parenthesis",
                "first_formatting": left_parenthesis.hidden_tokens_before,
                "second_formatting": left_parenthesis.hidden_tokens_after,
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "forth_formatting": right_parenthesis.hidden_tokens_after,
                "value": test
               }


    @pg.production("testlist : test comma")
    @pg.production("exprlist : expr comma")
    @pg.production("subscriptlist : subscript comma")
    def implicit_tuple_alone((test, comma)):
        return {
            "type": "tuple",
            "value": [test, comma],
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "with_parenthesis": False,
        }


    @pg.production("testlist : test testlist_part")
    @pg.production("exprlist : expr exprlist_part")
    @pg.production("subscriptlist : subscript subscriptlist_part")
    def implicit_tuple((test, testlist_part)):
        return {
            "type": "tuple",
            "value": [test] + testlist_part,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "forth_formatting": [],
            "with_parenthesis": False,
        }


    @pg.production("testlist_part : COMMA test")
    @pg.production("exprlist_part : COMMA expr")
    @pg.production("subscriptlist_part : COMMA subscript")
    def testlist_part((comma, test)):
        return [{
            "type": "comma",
            "first_formatting": comma.hidden_tokens_before,
            "second_formatting": comma.hidden_tokens_after,
        }, test]

    @pg.production("testlist_part : COMMA test COMMA")
    @pg.production("exprlist_part : COMMA expr COMMA")
    @pg.production("subscriptlist_part : COMMA subscript COMMA")
    def testlist_part_comma((comma, test, comma2)):
        return [{
            "type": "comma",
            "first_formatting": comma.hidden_tokens_before,
            "second_formatting": comma.hidden_tokens_after,
        }, test, {
            "type": "comma",
            "first_formatting": comma2.hidden_tokens_before,
            "second_formatting": comma2.hidden_tokens_after,
        }]


    @pg.production("testlist_part : COMMA test testlist_part")
    @pg.production("exprlist_part : COMMA expr exprlist_part")
    @pg.production("subscriptlist_part : COMMA subscript subscriptlist_part")
    def testlist_part_next((comma, test, testlist_part)):
        return [{
            "type": "comma",
            "first_formatting": comma.hidden_tokens_before,
            "second_formatting": comma.hidden_tokens_after,
        }, test] + testlist_part


    @pg.production("testlist_comp :")
    def testlist_comp_empty(empty):
        return []


    @pg.production("testlist_comp : test comma test")
    def testlist_comp_two((test, comma, test2)):
        return [test, comma, test2]


    @pg.production("testlist_comp : test comma testlist_comp")
    def testlist_comp_more((test, comma, testlist_comp)):
        return [test, comma] + testlist_comp


    @pg.production("atom : LEFT_SQUARE_BRACKET listmaker RIGHT_SQUARE_BRACKET")
    def list((left_bracket, listmaker, right_bracket,)):
        return {
                "type": "list",
                "first_formatting": left_bracket.hidden_tokens_before,
                "second_formatting": left_bracket.hidden_tokens_after,
                "third_formatting": right_bracket.hidden_tokens_before,
                "forth_formatting": right_bracket.hidden_tokens_after,
                "value": listmaker
               }


    @pg.production("listmaker :")
    def listmaker_empty(empty):
        return []


    @pg.production("listmaker : test")
    def listmaker_one((test,)):
        return [test]


    @pg.production("listmaker : test comma listmaker")
    def listmaker_more((test, comma, listmaker)):
        return [test, comma] + listmaker


    @pg.production("atom : LEFT_BRACKET dictmaker RIGHT_BRACKET")
    def dict((left_bracket, dictmaker, right_bracket,)):
        return {
                "type": "dict",
                "first_formatting": left_bracket.hidden_tokens_before,
                "second_formatting": left_bracket.hidden_tokens_after,
                "third_formatting": right_bracket.hidden_tokens_before,
                "forth_formatting": right_bracket.hidden_tokens_after,
                "value": dictmaker
               }


    @pg.production("dictmaker : ")
    def dict_empty(empty):
        return []


    @pg.production("dictmaker : test COLON test")
    def dict_one((test, colon, test2)):
        return [{
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "key": test,
            "value": test2,
            "type": "dictitem"
        }]


    @pg.production("dictmaker : test COLON test comma dictmaker")
    def dict_more((test, colon, test2, comma, dictmaker)):
        return [{
            "first_formatting": colon.hidden_tokens_before,
            "second_formatting": colon.hidden_tokens_after,
            "key": test,
            "value": test2,
            "type": "dictitem"
        }, comma] + dictmaker


    @pg.production("atom : LEFT_BRACKET setmaker RIGHT_BRACKET")
    def set((left_bracket, setmaker, right_bracket,)):
        return {
                "type": "set",
                "first_formatting": left_bracket.hidden_tokens_before,
                "second_formatting": left_bracket.hidden_tokens_after,
                "third_formatting": right_bracket.hidden_tokens_before,
                "forth_formatting": right_bracket.hidden_tokens_after,
                "value": setmaker
               }


    @pg.production("setmaker : test comma setmaker")
    def set_more((test, comma, setmaker)):
        return [test, comma] + setmaker


    @pg.production("setmaker : test")
    def set_one((test,)):
        return [test]


    @pg.production("atom : left_parenthesis test comp_for RIGHT_PARENTHESIS")
    def generator_comprehension((left_parenthesis, test, comp_for, right_parenthesis,)):
        return {
            "type": "generator_comprehension",
            "first_formatting": left_parenthesis.hidden_tokens_before,
            "second_formatting": left_parenthesis.hidden_tokens_after,
            "third_formatting": right_parenthesis.hidden_tokens_before,
            "forth_formatting": right_parenthesis.hidden_tokens_after,
            "result": test,
            "generators": comp_for,
          }

    @pg.production("atom : LEFT_SQUARE_BRACKET test list_for RIGHT_SQUARE_BRACKET")
    def list_comprehension((left_square_bracket, test, list_for, right_square_bracket)):
        return {
            "type": "list_comprehension",
            "first_formatting": left_square_bracket.hidden_tokens_before,
            "second_formatting": left_square_bracket.hidden_tokens_after,
            "third_formatting": right_square_bracket.hidden_tokens_before,
            "forth_formatting": right_square_bracket.hidden_tokens_after,
            "result": test,
            "generators": list_for,
          }

    @pg.production("atom : LEFT_BRACKET test COLON test comp_for RIGHT_BRACKET")
    def dict_comprehension((left_bracket, test, colon, test2, list_for, right_bracket)):
        return {
            "type": "dict_comprehension",
            "first_formatting": left_bracket.hidden_tokens_before,
            "second_formatting": left_bracket.hidden_tokens_after,
            "third_formatting": right_bracket.hidden_tokens_before,
            "forth_formatting": right_bracket.hidden_tokens_after,
            "result": {
                "key": test,
                "value": test2,
                "first_formatting": colon.hidden_tokens_before,
                "second_formatting": colon.hidden_tokens_after,
            },
            "generators": list_for,
          }

    @pg.production("atom : LEFT_BRACKET test comp_for RIGHT_BRACKET")
    def set_comprehension((left_bracket, test, list_for, right_bracket)):
        return {
            "type": "set_comprehension",
            "first_formatting": left_bracket.hidden_tokens_before,
            "second_formatting": left_bracket.hidden_tokens_after,
            "third_formatting": right_bracket.hidden_tokens_before,
            "forth_formatting": right_bracket.hidden_tokens_after,
            "result": test,
            "generators": list_for,
          }

    @pg.production("list_for : FOR exprlist IN old_test")
    @pg.production("comp_for : FOR exprlist IN or_test")
    def comp_for((for_, exprlist, in_, or_test)):
        return [{
            "type": "comprehension_loop",
            "first_formatting": for_.hidden_tokens_before,
            "second_formatting": for_.hidden_tokens_after,
            "third_formatting": in_.hidden_tokens_before,
            "forth_formatting": in_.hidden_tokens_after,
            "target": or_test,
            "iterator": exprlist,
            "ifs": [],
        }]

    @pg.production("list_for : FOR exprlist IN old_test")
    @pg.production("list_for : FOR exprlist IN testlist_safe")
    def comp_for_implicite_tuple((for_, exprlist, in_, testlist_safe)):
        return [{
            "type": "comprehension_loop",
            "first_formatting": for_.hidden_tokens_before,
            "second_formatting": for_.hidden_tokens_after,
            "third_formatting": in_.hidden_tokens_before,
            "forth_formatting": in_.hidden_tokens_after,
            "target": {
                "type": "tuple",
                "value": testlist_safe,
                "with_parenthesis": False,
                "first_formatting": [],
                "second_formatting": [],
                "third_formatting": [],
                "forth_formatting": [],
            },
            "iterator": exprlist,
            "ifs": [],
        }]

    @pg.production("comp_for : FOR exprlist IN or_test comp_iter")
    @pg.production("list_for : FOR exprlist IN old_test list_iter")
    @pg.production("list_for : FOR exprlist IN testlist_safe list_iter")
    def comp_for_iter((for_, exprlist, in_, or_test, comp_iter)):
        my_ifs = []
        for i in comp_iter:
            if i["type"] != "comprehension_if":
                break
            my_ifs.append(i)
            comp_iter = comp_iter[1:]

        return [{
            "type": "comprehension_loop",
            "first_formatting": for_.hidden_tokens_before,
            "second_formatting": for_.hidden_tokens_after,
            "third_formatting": in_.hidden_tokens_before,
            "forth_formatting": in_.hidden_tokens_after,
            "target": or_test,
            "iterator": exprlist,
            "ifs": my_ifs,
        }] + comp_iter

    @pg.production("list_iter : list_for")
    @pg.production("comp_iter : comp_for")
    def comp_iter_comp_for((comp_for,)):
        return comp_for

    @pg.production("list_iter : IF old_test")
    @pg.production("comp_iter : IF old_test")
    def comp_iter_if((if_, old_test)):
        return [{
            "type": "comprehension_if",
            "first_formatting": if_.hidden_tokens_before,
            "second_formatting": if_.hidden_tokens_after,
            "value": old_test
        }]

    @pg.production("list_iter : IF old_test list_iter")
    @pg.production("comp_iter : IF old_test comp_iter")
    def comp_iter_if_comp_iter((if_, old_test, comp_iter)):
        return [{
            "type": "comprehension_if",
            "first_formatting": if_.hidden_tokens_before,
            "second_formatting": if_.hidden_tokens_after,
            "value": old_test
        }] + comp_iter
