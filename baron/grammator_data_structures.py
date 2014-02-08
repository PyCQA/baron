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


    @pg.production("testlist_comp : test COMMA test")
    def testlist_comp_two((test, comma, test2)):
        return [test, {"type": "comma", "value": ",", "first_space": comma.before_space, "second_space": comma.after_space}, test2]


    @pg.production("testlist_comp : test COMMA testlist_comp")
    def testlist_comp_more((test, comma, testlist_comp)):
        return [test, {"type": "comma", "value": ",", "first_space": comma.before_space, "second_space": comma.after_space}] + testlist_comp


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


    @pg.production("listmaker : test COMMA listmaker")
    def listmaker_more((test, comma, listmaker)):
        return [test, {"type": "comma", "value": ",", "first_space": comma.before_space, "second_space": comma.after_space}] + listmaker


    @pg.production("atom : LEFT_BRACKET RIGHT_BRACKET")
    def dict((left_bracket, right_bracket,)):
        return {
                "type": "dict",
                "first_space": left_bracket.after_space,
                "second_space": right_bracket.before_space,
                "value": []
               }
