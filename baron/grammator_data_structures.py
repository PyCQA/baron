def include_data_structures(pg):
    @pg.production("atom : LEFT_PARENTHESIS testlist_comp RIGHT_PARENTHESIS")
    def tuple((left_parenthesis, testlist_comp, right_parenthesis,)):
        return {
                "type": "tuple",
                "first_space": left_parenthesis.after_space,
                "second_space": right_parenthesis.before_space,
                "value": testlist_comp
               }


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
                "first_space": left_bracket.after_space,
                "second_space": right_bracket.before_space,
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
                "first_space": left_bracket.after_space,
                "second_space": right_bracket.before_space,
                "value": dictmaker
               }


    @pg.production("dictmaker : ")
    def dict_empty(empty):
        return []


    @pg.production("dictmaker : test COLON test")
    def dict_one((test, colon, test2)):
        return [{
            "first_space": colon.before_space,
            "second_space": colon.after_space,
            "key": test,
            "value": test2,
            "type": "dictitem"
        }]


    @pg.production("dictmaker : test COLON test comma dictmaker")
    def dict_more((test, colon, test2, comma, dictmaker)):
        return [{
            "first_space": colon.before_space,
            "second_space": colon.after_space,
            "key": test,
            "value": test2,
            "type": "dictitem"
        }, comma] + dictmaker


    @pg.production("atom : LEFT_BRACKET setmaker RIGHT_BRACKET")
    def set((left_bracket, setmaker, right_bracket,)):
        return {
                "type": "set",
                "first_space": left_bracket.after_space,
                "second_space": right_bracket.before_space,
                "value": setmaker
               }


    @pg.production("setmaker : test comma setmaker")
    def set_more((test, comma, setmaker)):
        return [test, comma] + setmaker


    @pg.production("setmaker : test")
    def set_one((test,)):
        return [test]


    @pg.production("atom : LEFT_PARENTHESIS test comp_for RIGHT_PARENTHESIS")
    def generator_comprehension((left_parenthesis, test, comp_for, right_parenthesis,)):
        return {
            "type": "generator_comprehension",
            "first_space": left_parenthesis.after_space,
            "second_space": right_parenthesis.before_space,
            "result": test,
            "generators": comp_for,
          }

    @pg.production("atom : LEFT_SQUARE_BRACKET test list_for RIGHT_SQUARE_BRACKET")
    def list_comprehension((left_square_bracket, test, list_for, right_square_bracket)):
        return {
            "type": "list_comprehension",
            "first_space": left_square_bracket.after_space,
            "second_space": right_square_bracket.before_space,
            "result": test,
            "generators": list_for,
          }

    @pg.production("atom : LEFT_BRACKET test comp_for RIGHT_BRACKET")
    def set_comprehension((left_bracket, test, list_for, right_bracket)):
        return {
            "type": "set_comprehension",
            "first_space": left_bracket.after_space,
            "second_space": right_bracket.before_space,
            "result": test,
            "generators": list_for,
          }

    @pg.production("list_for : FOR exprlist IN testlist_safe")
    @pg.production("comp_for : FOR exprlist IN or_test")
    def comp_for((for_, exprlist, in_, or_test)):
        return [{
            "type": "comprehension_loop",
            "first_space": for_.before_space,
            "second_space": for_.after_space,
            "third_space": in_.before_space,
            "forth_space": in_.after_space,
            "target": or_test,
            "iterator": exprlist,
            "ifs": [],
        }]

    @pg.production("comp_for : FOR exprlist IN or_test comp_iter")
    @pg.production("list_for : FOR exprlist IN or_test list_iter")
    def comp_for_iter((for_, exprlist, in_, or_test, comp_iter)):
        my_ifs = []
        for i in comp_iter:
            print i
            if i["type"] != "comprehension_if":
                break
            my_ifs.append(i)
            comp_iter = comp_iter[1:]

        return [{
            "type": "comprehension_loop",
            "first_space": for_.before_space,
            "second_space": for_.after_space,
            "third_space": in_.before_space,
            "forth_space": in_.after_space,
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
            "first_space": if_.before_space,
            "second_space": if_.after_space,
            "value": old_test
        }]

    @pg.production("comp_iter : IF old_test comp_iter")
    def comp_iter_if_comp_iter((if_, old_test, comp_iter)):
        return [{
            "type": "comprehension_if",
            "first_space": if_.before_space,
            "second_space": if_.after_space,
            "value": old_test
        }] + comp_iter
