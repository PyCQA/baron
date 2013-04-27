# Ma grammaire en carton

# TODO/TOTEST

# dotted_name: NAME
# dotted_name: NAME.NAME
# dotted_name: NAME([NAME] -> . <- [NAME] NAME)+

# dotted_as_name: dotted_name
# dotted_as_name: dotted_name SPACE -> 'as' <- SPACE NAME

# dotted_as_names: dotted_as_name
# dotted_as_names: dotted_as_name [SPACE] -> ',' <- [SPACE] dotted_as_name
# dotted_as_names: dotted_as_name ([SPACE] -> ',' <- [SPACE] dotted_as_name)*

# import_as_name: NAME
# import_as_name: NAME SPACE -> 'as' <- SPACE NAME

# import_as_names: import_as_name
# import_as_names: import_as_name [SPACE] -> ',' <- [SPACE] import_as_name
# import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)*
# import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)* [SPACE] -> [',']

# import_name: 'import' <- SPACE dotted_as_names

# import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- SPACE import_as_names
# import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '(' <- [SPACE] import_as_names [SPACE] -> ')'
# import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '*'

# import_from: 'from' <- [SPACE] '.'* <- [SPACE] dotted_name SPACE 'import' ...........
# import_from: 'from' <- [SPACE] '.'+ <- [SPACE] 'import' ...........

# -

# global_stmt: 'global' SPACE NAME
# global_stmt: 'global' SPACE NAME ([SPACE] ',' [SPACE] NAME)*

# -

# break_stmt: 'break'
# pass_stmt: 'pass'
# continue_stmt: 'continue'

# -

# yield_stmt: yield_expr

# yield_expr: 'yield'
# yield_expr: 'yield' SPACE [testlist]

# -

# funcdef: 'def' SPACE NAME [SPACE] parameters [SPACE] ':' [SPACE] suite

# -

### should the SPACE really be there?
# parameters: '(' [SPACE] [varargslist] [SPACE] ')'

# -

# varargslist: [SPACE]

# varargslist: fpdef
# varargslist: fpdef [SPACE] '=' [SPACE] test
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ','
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test [SPACE] ','

# varargslist: '*' [SPACE] NAME
# varargslist: '**' [SPACE] NAME
# varargslist: '*' NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '**' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '**' [SPACE] NAME

# varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME
# varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME

# -

# suite: simple_stmt
# suite: [SPACE] NEWLINE INDENT stmt+ DEDENT

# -

# fpdef: NAME
# fpdef: '(' [SPACE] fplist [SPACE] ')'

# -

# fplist: fpdef
# fplist: fpdef [SPACE] ',' [SPACE] fpdef
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)*
# fplist: fpdef ([SPACE] ',' [SPACE] fpdef)* [SPACE] [',']

# -

# decorator: '@' [SPACE] dotted_name [SPACE] NEWLINE
# decorator: '@' dotted_name [ [SPACE] '(' [SPACE] [arglist] [SPACE] ')' ] [SPACE] NEWLINE

# -

# decorators: (decorator [BLANKLINE])+

# -

# decorated: decorators classdef
# decorated: decorators funcdef

# -

# stmt: simple_stmt
# stmt: compound_stmt

# -

# simple_stmt: small_stmt [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
# simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

# -

# small_stmt: expr_stmt
# small_stmt: print_stmt
# small_stmt: del_stmt
# small_stmt: pass_stmt
# small_stmt: flow_stmt
# small_stmt: import_stmt
# small_stmt: global_stmt
# small_stmt: exec_stmt
# small_stmt: assert_stmt

# -

# expr_stmt: testlist
# expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
# expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
# expr_stmt: testlist augassign yield_expr
# expr_stmt: testlist augassign testlist

# -

# augassign: '+='
# augassign: '-='
# augassign: '*='
# augassign: '/='
# augassign: '%='
# augassign: '&='
# augassign: '|='
# augassign: '^='
# augassign: '<<='
# augassign: '>>='
# augassign: '**='
# augassign: '//='

# -

# print_stmt: 'print'
# print_stmt: 'print' SPACE [ test ]
# print_stmt: 'print' SPACE [ test [SPACE] [','] ]
# print_stmt: 'print' SPACE [ test ([SPACE] ',' [SPACE] test)* [SPACE] [','] ]
# print_stmt: 'print' [SPACE] '>>' [SPACE] test
# print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ ]
# print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ [SPACE] [',']]

# -

# del_stmt: 'del' SPACE exprlist

# -

# flow_stmt: break_stmt
# flow_stmt: continue_stmt
# flow_stmt: return_stmt
# flow_stmt: raise_stmt
# flow_stmt: yield_stmt

# -

# return_stmt: 'return'
# return_stmt: 'return' SPACE [testlist]

# -

# yield_stmt: yield_expr

# -

# raise_stmt: 'raise'
# raise_stmt: 'raise' SPACE [test]
# raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test]]
# raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test [[SPACE] ',' [SPACE] test]]]

# -

# exec_stmt: 'exec' SPACE expr
# exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test]
# exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test [[SPACE] ',' [SPACE] test]]

# -

# assert_stmt: 'assert' SPACE test
# assert_stmt: 'assert' SPACE test [[SPACE] ',' [SPACE] test]

# -

# compound_stmt: if_stmt
# compound_stmt: while_stmt
# compound_stmt: for_stmt
# compound_stmt: try_stmt
# compound_stmt: with_stmt
# compound_stmt: funcdef
# compound_stmt: classdef
# compound_stmt: decorated

# -

# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)*
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ['else' SPACE ':' [SPACE] suite]
# if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)* ['else' SPACE ':' [SPACE] suite]

# -

# while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite
# while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

# for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite
# for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

# try_stmt: 'try' [SPACE] ':' [SPACE] suite 'finally' [SPACE] ':' suite
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite]
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['finally' [SPACE] ':' suite]
# try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite] ['finally' [SPACE] ':' suite]

# -

# with_stmt: 'with' SPACE with_item [SPACE] ':' [SPACE] suite
# with_stmt: 'with' SPACE with_item ([SPACE] ',' [SPACE] with_item)* [SPACE] ':' [SPACE] suite

# -

# with_item: test
# with_item: test [SPACE 'as' SPACE expr]

# -

# except_clause: 'except' [SPACE test [(SPACE 'as' SPACE | [SPACE] ',' [SPACE]) test]]

# -

# testlist_safe: old_test
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+]
# testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+ [SPACE] [',']]

# -

# old_test: or_test
# old_test: old_lambdef

# -

# old_lambdef: 'lambda' [SPACE] ':' [SPACE] old_test
# old_lambdef: 'lambda' SPACE [varargslist] [SPACE] ':' [SPACE] old_test

# -

# test: lambdef
# test: or_test
# test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]

# -

# or_test: and_test
# or_test: and_test (SPACE 'or' SPACE and_test)*

# -

# and_test: not_test
# and_test: not_test (SPACE 'and' SPACE not_test)*

# -

# not_test: 'not' SPACE not_test
# not_test: comparison

# -

# comparison: expr
# comparison: expr (comp_op expr)*

# -

# comp_op: '<'
# comp_op: '>'
# comp_op: '=='
# comp_op: '>='
# comp_op: '<='
# comp_op: '<>'
# comp_op: '!='
# comp_op: 'in'
# comp_op: 'not' SPACE 'in'
# comp_op: 'is'
# comp_op: 'is' SPACE 'not'

# -

# expr: xor_expr
# expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*

# -

# xor_expr: and_expr
# xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*

# -

# and_expr: shift_expr
# and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*

# -

# shift_expr: arith_expr
# shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*

# -

# arith_expr: term
# arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*

# -

# term: factor
# term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*

# -

# factor: ('+'|'-'|'~') [SPACE] factor
# factor: power

# -

# power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

# -

# atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
# atom: '(' [SPACE] [yield_expr] [SPACE] ')'
# atom: '[' [SPACE] [listmaker] [SPACE] ']'
# atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
# atom: '`' [SPACE] testlist1 [SPACE] '`'
# atom: NAME
# atom: NUMBER
# atom: STRING+

# -

# listmaker: test
# listmaker: test [SPACE] list_for
# listmaker: test ([SPACE] ',' [SPACE] test)*
# listmaker: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# testlist_comp: test
# testlist_comp: test [SPACE] comp_for
# testlist_comp: test ([SPACE] ',' [SPACE] test)*
# testlist_comp: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# lambdef: 'lambda' [SPACE] ':' [SPACE] test
# lambdef: 'lambda' [SPACE] [varargslist] [SPACE] ':' [SPACE] test

# -

# trailer: '.' [SPACE] NAME
# trailer: '[' [SPACE] subscriptlist [SPACE] ']'
# trailer: '(' [SPACE] [arglist] [SPACE] ')'

# -

# subscriptlist: subscript
# subscriptlist: subscript [SPACE] [',']
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)*
# subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)* [SPACE] [',']

# -

# subscript: test
# subscript: '.' [SPACE] '.' [SPACE] '.'
# subscript: [test] [SPACE] ':' [SPACE] [test] [SPACE] [sliceop]

# -

# sliceop: ':' [SPACE] [test]

# -

# exprlist: expr
# exprlist: expr [SPACE] [',']
# exprlist: expr ([SPACE] ',' [SPACE] expr)*
# exprlist: expr ([SPACE] ',' [SPACE] expr)* [SPACE] [',']

# -

# testlist: test
# testlist: test [SPACE] [',']
# testlist: test ([SPACE] ',' [SPACE] test)*
# testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE]
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)*)
# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)* [SPACE] [','])

# dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] comp_for

# dictorsetmaker: test [SPACE] comp_for

# dictorsetmaker: test [SPACE]
# dictorsetmaker: test [SPACE] [SPACE] [',']
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)*
# dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

# classdef: 'class' SPACE NAME [SPACE] ['(' [SPACE] [testlist] [SPACE] ')'] [SPACE] ':' [SPACE] suite

# -

# for reference
# arglist: (argument [SPACE] ',' [SPACE])* (argument [SPACE] [','] |'*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test] |'**' [SPACE] test)


# arglist: (argument [SPACE] ',' [SPACE])*
# arglist: argument [SPACE] [',']
# arglist: (argument [SPACE] ',' [SPACE])* argument [SPACE] [',']
# arglist: '**' [SPACE] test
# arglist: (argument [SPACE] ',' [SPACE])* '**' [SPACE] test

# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]
# arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]

# -

# argument: test
# argument: test [SPACE comp_for]
# argument: test [SPACE] '=' [SPACE] test

# -

# list_iter: list_if
# list_iter: list_for

# -

# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe
# list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe [SPACE list_iter]

# -

# list_if: 'if' SPACE old_test
# list_if: 'if' SPACE old_test [SPACE list_iter]

# -

# comp_iter: comp_if
# comp_iter: comp_for

# -

# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
# comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# -

# comp_if: 'if' SPACE old_test
# comp_if: 'if' SPACE old_test [SPACE comp_iter]

# -

# testlist1: test
# testlist1: test ([SPACE] ',' [SPACE] test)*

# -

# yield_expr: 'yield'
# yield_expr: 'yield' [SPACE testlist]

# -

# single_input: NEWLINE
# single_input: simple_stmt
# single_input: compound_stmt [SPACE] NEWLINE

# -

# file_input: ([SPACE] NEWLINE | stmt)* [SPACE] ENDMARKER

# -

# eval_input: testlist ([SPACE] NEWLINE)* [SPACE] ENDMARKER

# ---

# KEYWORDS: "and as assert break class continue def del elif else except exec finally for from global if import in is lambda not or pass print raise return try while with yield"

from rply.token import Token
from rply import ParserGenerator

from tokenizer import TOKENS, KEYWORDS, tokenize
from utils import create_node_from_token, binary_operator, unitary_operator
from grammator_imports import include_imports


pg = ParserGenerator(tuple(map(lambda x: x.upper(), KEYWORDS)) + zip(*TOKENS)[1] + ("ENDMARKER",), cache_id="baron")
        #precedence=[("left", ['PLUS', 'MINUS'])], cache_id="baron")


@pg.production("main : statements")
def main((statements,)):
    return filter(None, statements) if statements else []

@pg.production("statements : statements statement")
def statements_statement((statements, statement)):
    return statements + statement

@pg.production("statements : statement")
def statement((statement,)):
    return statement

@pg.production("statement : SPACE? ENDMARKER")
def end((space, endmarker)):
    if space:
        return [create_node_from_token(space)]
    return [None]

@pg.production("statement : separator")
@pg.production("statement : small_stmt")
def separator((statement,)):
    return [statement]

include_imports(pg)

@pg.production("small_stmt : expr_stmt")
@pg.production("expr_stmt : testlist")
@pg.production("testlist : test")
@pg.production("test : or_test")
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
def term_factor((level,)):
    return level

@pg.production("separator : SPACE? ENDL")
def space_endl((space, endl,)):
    return {
            "type": endl.name.lower(),
            "value": endl.value,
            "before_space": space.value if space else ""
           }

@pg.production("term : factor STAR factor")
@pg.production("term : factor SLASH factor")
@pg.production("term : factor PERCENT factor")
@pg.production("term : factor DOUBLE_SLASH factor")
def term_binary_operator((factor, operator, factor2)):
    return binary_operator(
                           operator.value,
                           first=factor,
                           second=factor2,
                           first_space=operator.before_space,
                           second_space=operator.after_space,
                          )

@pg.production("factor : PLUS factor")
@pg.production("factor : MINUS factor")
@pg.production("factor : TILDE factor")
def factor_unitary_operator_space((operator, factor,)):
    return unitary_operator(operator.value, factor, space=operator.after_space)

@pg.production("power : atom DOUBLE_STAR factor")
@pg.production("power : atom DOUBLE_STAR power")
def power((atom, double_star, factor)):
    return binary_operator(
                           double_star.value,
                           atom,
                           factor,
                           first_space=double_star.before_space,
                           second_space=double_star.after_space
                          )

@pg.production("power : atomtrailers DOUBLE_STAR factor")
@pg.production("power : atomtrailers DOUBLE_STAR power")
def power_atomtrailer_power((atomtrailers, double_star, factor)):
    return binary_operator(
                           double_star.value,
                           {
                            "type": "atomtrailers",
                            "value": atomtrailers,
                           },
                           factor,
                           first_space=double_star.before_space,
                           second_space=double_star.after_space
                          )

@pg.production("power : atomtrailers")
def power_atomtrailers((atomtrailers,)):
    return {"type": "atomtrailers", "value": atomtrailers}

@pg.production("atomtrailers : atom")
def atomtrailers_atom((atom,)):
    return [atom]

@pg.production("atomtrailers : atom trailers")
def atomtrailer((atom, trailers)):
    return [atom] + trailers

@pg.production("trailers : trailer")
def trailers((trailer,)):
    return trailer

@pg.production("trailers : trailers trailer")
def trailers_trailer((trailers, trailer)):
    return trailers + trailer

@pg.production("trailer : DOT NAME")
def trailer((dot, name,)):
    to_return = []
    if dot.before_space:
        to_return += [{"type": "space", "value": dot.before_space}]
    to_return += [create_node_from_token(dot)]
    if dot.after_space:
        to_return += [{"type": "space", "value": dot.after_space}]
    to_return += [create_node_from_token(name)]
    return to_return

@pg.production("trailer : LEFT_SQUARE_BRACKET RIGHT_SQUARE_BRACKET")
@pg.production("trailer : LEFT_PARENTHESIS RIGHT_PARENTHESIS")
def trailer_getitem((left, right)):
    to_return = []
    if left.before_space:
        to_return += [{"type": "space", "value": left.before_space}]
    to_return += [{"type": "getitem" if left.value == "[" else "call", "value": None, "first_space": left.after_space, "second_space": ""}]
    return to_return

@pg.production("atom : INT")
def int((int_,)):
    return create_node_from_token(int_, section="number")

@pg.production("atom : NAME")
def name((name,)):
    return create_node_from_token(name)

@pg.production("atom : STRING")
def string((string_,)):
    return create_node_from_token(string_)

parser = pg.build()

def fake_lexer(sequence):
    for i in tokenize(sequence):
        if i is None:
            yield None
        yield Token(*i)

def parse(sequence):
    return parser.parse(fake_lexer(sequence))

if __name__ == '__main__':
    import json
    from grouper import group
    from spliter import split
    def pouet(sequence):
        return tokenize(group(split(sequence)))

    def pouetpouet(sequence):
        return group(split(sequence))

    def pouetpouetpouet(sequence):
        for i in sequence:
            if i is None:
                yield None
            yield Token(*i)

    #print pouet('1')
    print json.dumps(parse(pouetpouet('a.B * c')), indent=4)
    #print json.dumps(parser.parse(pouetpouetpouet([('ENDMARKER', ''), None])), indent=4)
