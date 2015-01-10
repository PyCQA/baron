from .token import BaronToken
from .parser import BaronParserGenerator

from .tokenizer import TOKENS, tokenize, tokenize_current_keywords
from .utils import create_node_from_token
from .grammator_imports import include_imports
from .grammator_control_structures import include_control_structures
from .grammator_primitives import include_primivites
from .grammator_operators import include_operators
from .grammator_data_structures import include_data_structures


def generate_parse(print_function):
    pg = BaronParserGenerator(tuple([x.upper() for x in tokenize_current_keywords(print_function)] + [x[1] for x in TOKENS] + ["ENDMARKER", "INDENT", "DEDENT"]), cache_id="baron")

    @pg.production("main : statements")
    def main(pack):
        (statements,) = pack
        return [x for x in statements if x] if statements else []


    @pg.production("statements : statements statement")
    def statements_statement(pack):
        (statements, statement) = pack
        return statements + statement


    @pg.production("statements : statement SEMICOLON")
    def statement_semicolon(pack):
        (statement, semicolon) = pack
        return statement +\
                [{
                  "type": "semicolon",
                  "first_formatting": semicolon.hidden_tokens_before,
                  "second_formatting": semicolon.hidden_tokens_after,
                  "value": ";"
                 }]


    @pg.production("statements : statement")
    def statement(pack):
        (statement,) = pack
        return statement


    @pg.production("statement : endl")
    def statement_endl(pack):
        (endl,) = pack
        return endl


    @pg.production("endl : ENDL")
    def endl(pack):
        (endl,) = pack
        indent = ""
        if endl.hidden_tokens_after and endl.hidden_tokens_after[0]["type"] == "space":
            indent = endl.hidden_tokens_after[0]["value"]
            endl.hidden_tokens_after = endl.hidden_tokens_after[1:]
        return [{
            "type": "endl",
            "value": endl.value,
            "formatting": endl.hidden_tokens_before,
            "indent": indent,
        }] + endl.hidden_tokens_after


    @pg.production("left_parenthesis : LEFT_PARENTHESIS")
    def left_parenthesis(pack):
        (lp,) = pack
        return lp


    @pg.production("endl : COMMENT ENDL")
    def comment(pack):
        (comment_, endl) = pack
        return [{
            "type": "comment",
            "value": comment_.value,
            "formatting": comment_.hidden_tokens_before,
        }, {
            "type": "endl",
            "formatting": endl.hidden_tokens_before,
            "indent": endl.hidden_tokens_after[0]["value"] if endl.hidden_tokens_after else "",
            "value": endl.value
        }]


    @pg.production("statement : ENDMARKER")
    def end(_):
        return [None]


    @pg.production("statement : simple_stmt")
    @pg.production("statement : compound_stmt")
    def statement_simple_statement(pack):
        (stmt,) = pack
        return stmt

    @pg.production("simple_stmt : small_stmt SEMICOLON endl")
    def simple_stmt_semicolon_endl(pack):
        (small_stmt, semicolon, endl) = pack
        return [small_stmt,
                {
                 "type": "semicolon",
                 "value": ";",
                 "first_formatting": semicolon.hidden_tokens_before,
                 "second_formatting": semicolon.hidden_tokens_after
                }] + endl


    @pg.production("simple_stmt : small_stmt endl")
    def simple_stmt(pack):
        (small_stmt, endl) = pack
        return [small_stmt] + endl


    @pg.production("simple_stmt : small_stmt SEMICOLON simple_stmt")
    def simple_stmt_semicolon(pack):
        (small_stmt, semicolon, simple_stmt) = pack
        return [small_stmt,
                {
                 "type": "semicolon",
                 "value": ";",
                 "first_formatting": semicolon.hidden_tokens_before,
                 "second_formatting": semicolon.hidden_tokens_after
                }] + simple_stmt


    @pg.production("small_stmt : flow_stmt")
    @pg.production("small_stmt : del_stmt")
    @pg.production("small_stmt : pass_stmt")
    @pg.production("small_stmt : assert_stmt")
    @pg.production("small_stmt : raise_stmt")
    @pg.production("small_stmt : global_stmt")
    @pg.production("compound_stmt : if_stmt")
    @pg.production("compound_stmt : while_stmt")
    @pg.production("compound_stmt : for_stmt")
    @pg.production("compound_stmt : try_stmt")
    @pg.production("compound_stmt : funcdef")
    @pg.production("compound_stmt : classdef")
    @pg.production("compound_stmt : with_stmt")
    @pg.production("compound_stmt : decorated")
    def small_and_compound_stmt(pack):
        (statement,) = pack
        return statement

    if not print_function:
        @pg.production("small_stmt : print_stmt")
        def print_statement(pack):
            (statement,) = pack
            return statement


    @pg.production("small_stmt : expr_stmt")
    @pg.production("expr_stmt : testlist")
    @pg.production("testlist : test")
    @pg.production("test : or_test")
    @pg.production("test : lambdef")
    @pg.production("or_test : and_test")
    @pg.production("and_test : not_test")
    @pg.production("not_test : comparison")
    @pg.production("comparison : expr")
    @pg.production("expr : xor_expr")
    @pg.production("xor_expr : and_expr")
    @pg.production("and_expr : shift_expr")
    @pg.production("shift_expr : arith_expr")
    @pg.production("arith_expr : term")
    @pg.production("term : factor")
    @pg.production("factor : power")
    @pg.production("power : atom")
    @pg.production("exprlist : expr")
    def term_factor(pack):
        (level,) = pack
        return level


    @pg.production("with_stmt : WITH with_items COLON suite")
    def with_stmt(pack):
        (with_, with_items, colon, suite) = pack
        return [{
            "type": "with",
            "value": suite,
            "first_formatting": with_.hidden_tokens_after,
            "second_formatting": colon.hidden_tokens_before,
            "third_formatting": colon.hidden_tokens_after,
            "contexts": with_items
        }]


    @pg.production("with_items : with_items comma with_item")
    def with_items_with_item(pack):
        (with_items, comma, with_item,) = pack
        return with_items + [comma, with_item]


    @pg.production("with_items : with_item")
    def with_items(pack):
        (with_item,) = pack
        return [with_item]


    @pg.production("with_item : test")
    def with_item(pack):
        (test,) = pack
        return {
            "type": "with_context_item",
            "as": {},
            "first_formatting": [],
            "second_formatting": [],
            "value": test
        }


    @pg.production("with_item : test AS expr")
    def with_item_as(pack):
        (test, as_, expr) = pack
        return {
            "type": "with_context_item",
            "as": expr,
            "first_formatting": as_.hidden_tokens_before,
            "second_formatting": as_.hidden_tokens_after,
            "value": test
        }


    @pg.production("classdef : CLASS NAME COLON suite")
    def class_stmt(pack,):
        (class_, name, colon, suite) = pack
        return [{
            "type": "class",
            "name": name.value,
            "parenthesis": False,
            "first_formatting": class_.hidden_tokens_after,
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "fifth_formatting": colon.hidden_tokens_before,
            "sixth_formatting": colon.hidden_tokens_after,
            "inherit_from": [],
            "decorators": [],
            "value": suite,
        }]


    @pg.production("classdef : CLASS NAME LEFT_PARENTHESIS RIGHT_PARENTHESIS COLON suite")
    def class_stmt_parenthesis(pack,):
        (class_, name, left_parenthesis, right_parenthesis, colon, suite) = pack
        return [{
            "type": "class",
            "name": name.value,
            "parenthesis": True,
            "first_formatting": class_.hidden_tokens_after,
            "second_formatting": left_parenthesis.hidden_tokens_before,
            "third_formatting": left_parenthesis.hidden_tokens_after,
            "fourth_formatting": right_parenthesis.hidden_tokens_before,
            "fifth_formatting": right_parenthesis.hidden_tokens_after + colon.hidden_tokens_before,
            "sixth_formatting": colon.hidden_tokens_after,
            "inherit_from": [],
            "decorators": [],
            "value": suite,
        }]


    @pg.production("classdef : CLASS NAME LEFT_PARENTHESIS testlist RIGHT_PARENTHESIS COLON suite")
    def class_stmt_inherit(pack,):
        (class_, name, left_parenthesis, testlist, right_parenthesis, colon, suite) = pack
        return [{
            "type": "class",
            "name": name.value,
            "parenthesis": True,
            "first_formatting": class_.hidden_tokens_after,
            "second_formatting": left_parenthesis.hidden_tokens_before,
            "third_formatting": left_parenthesis.hidden_tokens_after,
            "fourth_formatting": right_parenthesis.hidden_tokens_before,
            "fifth_formatting": right_parenthesis.hidden_tokens_after + colon.hidden_tokens_before,
            "sixth_formatting": colon.hidden_tokens_after,
            "inherit_from": [testlist],
            "decorators": [],
            "value": suite,
        }]


    @pg.production("decorated : decorators funcdef")
    @pg.production("decorated : decorators classdef")
    def decorated(pack):
        (decorators, funcdef) = pack
        funcdef[0]["decorators"] = decorators
        return funcdef


    @pg.production("decorators : decorators decorator")
    def decorators_decorator(pack):
        (decorators, decorator,) = pack
        return decorators + decorator


    @pg.production("decorators : decorator")
    def decorators(pack):
        (decorator,) = pack
        return decorator


    # TODO tests
    @pg.production("decorator : endl")
    def decorator_endl(pack):
        # thanks iPython devs, you appear to be the only one in the world that
        # split decorators with empty lines... like seriously.
        (endl,) = pack
        return endl


    @pg.production("decorator : AT dotted_name endl")
    def decorator(pack):
        (at, dotted_name, endl) = pack
        return [{
            "type": "decorator",
            "value": {
                "value": dotted_name,
                "type": "dotted_name",
            },
            "call": {},
            "formatting": at.hidden_tokens_after,
        }] + endl


    @pg.production("decorator : AT dotted_name LEFT_PARENTHESIS RIGHT_PARENTHESIS endl")
    def decorator_empty_call(pack):
        (at, dotted_name, left_parenthesis, right_parenthesis, endl) = pack
        return [{
            "type": "decorator",
            "value": {
                "value": dotted_name,
                "type": "dotted_name",
            },
            "call": {
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "fourth_formatting": right_parenthesis.hidden_tokens_after,
                "type": "call",
                "first_formatting": left_parenthesis.hidden_tokens_before,
                "value": [],
                "second_formatting": left_parenthesis.hidden_tokens_after
            },
            "formatting": at.hidden_tokens_after,
        }] + endl


    @pg.production("decorator : AT dotted_name LEFT_PARENTHESIS argslist RIGHT_PARENTHESIS endl")
    def decorator_call(pack):
        (at, dotted_name, left_parenthesis, argslist, right_parenthesis, endl) = pack
        return [{
            "type": "decorator",
            "value": {
                "value": dotted_name,
                "type": "dotted_name",
            },
            "call": {
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "fourth_formatting": right_parenthesis.hidden_tokens_after,
                "type": "call",
                "first_formatting": left_parenthesis.hidden_tokens_before,
                "value": argslist,
                "second_formatting": left_parenthesis.hidden_tokens_after
            },
            "formatting": at.hidden_tokens_after,
        }] + endl


    @pg.production("funcdef : DEF NAME LEFT_PARENTHESIS parameters RIGHT_PARENTHESIS COLON suite")
    def function_definition(pack):
        (def_, name, left_parenthesis, parameters, right_parenthesis, colon, suite) = pack
        return [{
            "type": "def",
            "decorators": [],
            "name": name.value,
            "first_formatting": def_.hidden_tokens_after,
            "second_formatting": left_parenthesis.hidden_tokens_before,
            "third_formatting": left_parenthesis.hidden_tokens_after,
            "fourth_formatting": right_parenthesis.hidden_tokens_before,
            "fifth_formatting": colon.hidden_tokens_before,
            "sixth_formatting": colon.hidden_tokens_after,
            "arguments": parameters,
            "value": suite,
        }]

    @pg.production("argslist : argslist argument")
    @pg.production("parameters : parameters parameter")
    def parameters_parameters_parameter(pack,):
        (parameters, parameter,) = pack
        return parameters + parameter

    @pg.production("argslist : argument")
    @pg.production("parameters : parameter")
    def parameters_parameter(pack,):
        (parameter,) = pack
        return parameter

    @pg.production("argument :")
    @pg.production("parameter : ")
    def parameter_empty(p):
        return []

    @pg.production("name : NAME")
    def name(pack):
        (name_,) = pack
        return {
            "type": "name",
            "value": name_.value,
        }

    @pg.production("parameter : LEFT_PARENTHESIS name RIGHT_PARENTHESIS maybe_test")
    def parameter_fpdef(pack):
        (left_parenthesis, name, right_parenthesis, (equal, test)) = pack
        return [{
            "type": "def_argument",
            "first_formatting": equal.hidden_tokens_before if equal else [],
            "second_formatting": equal.hidden_tokens_after if equal else [],
            "value": test,
            "target": {
                "type": "associative_parenthesis",
                "first_formatting": left_parenthesis.hidden_tokens_before,
                "second_formatting": left_parenthesis.hidden_tokens_after,
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "fourth_formatting": right_parenthesis.hidden_tokens_after,
                "value": name
            }
        }]


    @pg.production("parameter : LEFT_PARENTHESIS fplist RIGHT_PARENTHESIS maybe_test")
    def parameter_fplist(pack):
        (left_parenthesis, fplist, right_parenthesis, (equal, test)) = pack
        return [{
            "type": "def_argument",
            "first_formatting": equal.hidden_tokens_before if equal else [],
            "second_formatting": equal.hidden_tokens_after if equal else [],
            "value": test,
            "target": {
                "type": "tuple",
                "with_parenthesis": True,
                "first_formatting": left_parenthesis.hidden_tokens_after,
                "second_formatting": left_parenthesis.hidden_tokens_before,
                "third_formatting": right_parenthesis.hidden_tokens_before,
                "fourth_formatting": right_parenthesis.hidden_tokens_after,
                "value": fplist,
            },
        }]


    @pg.production("fplist : fplist parameter")
    def fplist_recur(pack):
        (fplist, name) = pack
        if name[0]["type"] == "def_argument":
            name = [name[0]["target"]]
        return fplist + name


    @pg.production("fplist : parameter comma")
    def fplist(pack):
        (name, comma) = pack
        if name[0]["type"] == "def_argument":
            name = [name[0]["target"]]
        return name + [comma]


    # really strange that left part of argument grammar can be a test
    # I guess it's yet another legacy mistake
    # python give me 'SyntaxError: keyword can't be an expression' when I try to
    # put something else than a name (looks like a custom SyntaxError)
    @pg.production("argument : test maybe_test")
    def named_argument(pack):
        (name, (equal, test)) = pack
        return [{
            "type": "call_argument",
            "first_formatting": equal.hidden_tokens_before if equal else [],
            "second_formatting": equal.hidden_tokens_after if equal else [],
            "value": test if equal else name,
            "target": name if equal else {}
        }]

    @pg.production("parameter : name maybe_test")
    def parameter_with_default(pack):
        (name, (equal, test)) = pack
        return [{
            "type": "def_argument",
            "first_formatting": equal.hidden_tokens_before if equal else [],
            "second_formatting": equal.hidden_tokens_after if equal else [],
            "value": test,
            "target": name
        }]

    @pg.production("maybe_test : EQUAL test")
    def maybe_test(pack):
        return pack

    @pg.production("maybe_test : ")
    def maybe_test_empty(pack):
        return (None, {})

    @pg.production("argument : test comp_for")
    def generator_comprehension(pack):
        (test, comp_for,) = pack
        return [{
            "type": "argument_generator_comprehension",
            "result": test,
            "generators": comp_for,
        }]

    @pg.production("argument : STAR test")
    def argument_star(pack):
        (star, test,) = pack
        return [{
            "type": "list_argument",
            "formatting": star.hidden_tokens_after,
            "value": test,
        }]

    @pg.production("argument : DOUBLE_STAR test")
    def argument_star_star(pack):
        (double_star, test,) = pack
        return [{
            "type": "dict_argument",
            "formatting": double_star.hidden_tokens_after,
            "value": test,
        }]

    # TODO refactor those 2 to standardize with argument_star and argument_star_star
    @pg.production("parameter : STAR NAME")
    def parameter_star(pack):
        (star, name,) = pack
        return [{
            "type": "list_argument",
            "formatting": star.hidden_tokens_after,
            "value": {
                "type": "name",
                "value": name.value,
            }
        }]

    @pg.production("parameter : DOUBLE_STAR NAME")
    def parameter_star_star(pack):
        (double_star, name,) = pack
        return [{
            "type": "dict_argument",
            "formatting": double_star.hidden_tokens_after,
            "value": {
                "type": "name",
                "value": name.value,
            },
        }]

    @pg.production("argument : comma")
    @pg.production("parameter : comma")
    def parameter_comma(pack):
        (comma,) = pack
        return [comma]

    @pg.production("suite : simple_stmt")
    def suite(pack):
        (simple_stmt,) = pack
        return simple_stmt


    @pg.production("suite : endls INDENT statements DEDENT")
    def suite_indent(pack):
        (endls, indent, statements, dedent,) = pack
        return endls + statements


    @pg.production("endls : endls endl")
    @pg.production("endls : endl")
    def endls(p):
        if len(p) == 1:
            return p[0]
        return p[0] + p[1]


    include_imports(pg)
    include_control_structures(pg)
    include_primivites(pg, print_function)
    include_operators(pg)
    include_data_structures(pg)

    @pg.production("atom : LEFT_PARENTHESIS yield_expr RIGHT_PARENTHESIS")
    def yield_atom(pack):
        (left_parenthesis, yield_expr, right_parenthesis) = pack
        return {
            "type": "yield_atom",
            "value": yield_expr["value"],
            "first_formatting": left_parenthesis.hidden_tokens_after,
            "second_formatting": yield_expr["formatting"],
            "third_formatting": right_parenthesis.hidden_tokens_before
        }

    @pg.production("atom : BACKQUOTE testlist1 BACKQUOTE")
    def repr_atom(pack):
        (backquote, testlist1, backquote2) = pack
        return {
            "type": "repr",
            "value": testlist1,
            "first_formatting": backquote.hidden_tokens_after,
            "second_formatting": backquote2.hidden_tokens_before,
        }

    @pg.production("testlist1 : test comma testlist1")
    def testlist1_double(pack):
        (test, comma, test2,) = pack
        return [test, comma] + test2

    @pg.production("testlist1 : test")
    def testlist1(pack):
        (test,) = pack
        return [test]

    # TODO test all the things (except INT)
    @pg.production("atom : INT")
    @pg.production("atom : LONG")
    @pg.production("atom : OCTA")
    @pg.production("atom : HEXA")
    @pg.production("atom : BINARY")
    @pg.production("atom : FLOAT")
    @pg.production("atom : FLOAT_EXPONANT")
    @pg.production("atom : FLOAT_EXPONANT_COMPLEX")
    @pg.production("atom : COMPLEX")
    def int(pack):
        (int_,) = pack
        return create_node_from_token(int_, section="number")


    @pg.production("atom : name")
    def atom_name(pack):
        (name,) = pack
        return name


    @pg.production("atom : strings")
    def strings(pack):
        (string_chain,) = pack
        if len(string_chain) == 1:
            return string_chain[0]
        return {
            "type": "string_chain",
            "value": string_chain
        }

    @pg.production("strings : string strings")
    def strings_string_strings(pack):
        (string_, strings_) = pack
        return string_ + strings_

    @pg.production("strings : string")
    def strings_string(pack):
        (string_,) = pack
        return string_

    # TODO tests those other kind of strings
    @pg.production("string : STRING")
    @pg.production("string : RAW_STRING")
    @pg.production("string : UNICODE_STRING")
    @pg.production("string : BINARY_STRING")
    @pg.production("string : UNICODE_RAW_STRING")
    @pg.production("string : BINARY_RAW_STRING")
    def string(pack):
        (string_,) = pack
        return [{
            "type": string_.name.lower(),
            "value": string_.value,
            "first_formatting": string_.hidden_tokens_before,
            "second_formatting": string_.hidden_tokens_after,
        }]


    @pg.production("comma : COMMA")
    def comma(pack):
        (comma,) = pack
        return {
            "type": "comma",
            "first_formatting": comma.hidden_tokens_before,
            "second_formatting": comma.hidden_tokens_after,
        }

    def parse(tokens):
        if print_function:
            new_tokens = []
            for token in tokens:
                if token[0] == "PRINT":
                    token = list(token)
                    token[0] = "NAME"
                    token = tuple(token)
                new_tokens.append(token)

            tokens = [BaronToken(*x) if x else x for x in new_tokens] + [None]
        else:
            tokens = [BaronToken(*x) if x else x for x in tokens] + [None]

        return parser.parse(iter(tokens))

    parser = pg.build()
    return parse


def fake_lexer(sequence):
    for i in tokenize(sequence):
        if i is None:
            yield None
        yield BaronToken(*i)


def parse(sequence):
    parser = generate_parse(print_function=False)
    return parser.parse(fake_lexer(sequence))
