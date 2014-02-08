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
