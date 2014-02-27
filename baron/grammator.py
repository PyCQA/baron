# Ma grammaire en carton

# TODO/TOTEST

### dotted_name: NAME
### dotted_name: NAME.NAME
### dotted_name: NAME([NAME] -> . <- [NAME] NAME)+

### dotted_as_name: dotted_name
### dotted_as_name: dotted_name SPACE -> 'as' <- SPACE NAME

### dotted_as_names: dotted_as_name
### dotted_as_names: dotted_as_name [SPACE] -> ',' <- [SPACE] dotted_as_name
### dotted_as_names: dotted_as_name ([SPACE] -> ',' <- [SPACE] dotted_as_name)*

### import_as_name: NAME
### import_as_name: NAME SPACE -> 'as' <- SPACE NAME

### import_as_names: import_as_name
### import_as_names: import_as_name [SPACE] -> ',' <- [SPACE] import_as_name
### import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)*
### import_as_names: import_as_name ([SPACE] -> ',' <- [SPACE] import_as_name)* [SPACE] -> [',']

### import_name: 'import' <- SPACE dotted_as_names

### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- SPACE import_as_names
### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '(' <- [SPACE] import_as_names [SPACE] -> ')'
### import_from: 'from' <- SPACE dotted_name SPACE -> 'import' <- [SPACE] '*'

### import_from: 'from' <- [SPACE] '.'* <- [SPACE] dotted_name SPACE 'import' ...........
### import_from: 'from' <- [SPACE] '.'+ <- [SPACE] 'import' ...........

# -

### global_stmt: 'global' SPACE NAME
### global_stmt: 'global' SPACE NAME ([SPACE] ',' [SPACE] NAME)*

# -

### break_stmt: 'break'
### pass_stmt: 'pass'
### continue_stmt: 'continue'

# -

### yield_stmt: yield_expr

### yield_expr: 'yield'
### yield_expr: 'yield' SPACE [testlist]

# -

### funcdef: 'def' SPACE NAME [SPACE] parameters [SPACE] ':' [SPACE] suite

# -

### should the SPACE really be there?
### parameters: '(' [SPACE] [varargslist] [SPACE] ')'

# -

### varargslist: [SPACE]

### varargslist: fpdef
### varargslist: fpdef [SPACE] '=' [SPACE] test
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ','
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] fpdef [SPACE] '=' [SPACE] test [SPACE] ','
##
### varargslist: '*' [SPACE] NAME
### varargslist: '**' [SPACE] NAME
### varargslist: '*' NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME
##
### varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME
##
### varargslist: fpdef [SPACE] ',' [SPACE] '**' [SPACE] NAME
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '**' [SPACE] NAME
##
### varargslist: fpdef [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME
### varargslist: fpdef [SPACE] '=' [SPACE] test [SPACE] ',' [SPACE] '*' [SPACE] NAME [SPACE] ',' [SPACE] '**' [SPACE] NAME

# -

### suite: simple_stmt
### suite: [SPACE] NEWLINE INDENT stmt+ DEDENT

# -

### fpdef: NAME
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

### stmt: simple_stmt
### stmt: compound_stmt

# -

### simple_stmt: small_stmt [SPACE] NEWLINE
### simple_stmt: small_stmt [SPACE] ';' [SPACE] NEWLINE
### simple_stmt: small_stmt [SPACE] ';' small_stmt [SPACE] ';' [SPACE] NEWLINE
### simple_stmt: small_stmt ([SPACE] ';' small_stmt [SPACE] ';') [SPACE] NEWLINE

# -

### small_stmt: expr_stmt
### small_stmt: print_stmt
### small_stmt: del_stmt
### small_stmt: pass_stmt
### small_stmt: flow_stmt
### small_stmt: import_stmt
### small_stmt: global_stmt
### small_stmt: exec_stmt
### small_stmt: assert_stmt

# -

### expr_stmt: testlist
### expr_stmt: testlist ([SPACE] '=' [SPACE] testlist)*
### expr_stmt: testlist ([SPACE] '=' [SPACE] yield_expr)*
### expr_stmt: testlist augassign yield_expr
### expr_stmt: testlist augassign testlist

# -

### augassign: '+='
### augassign: '-='
### augassign: '*='
### augassign: '/='
### augassign: '%='
### augassign: '&='
### augassign: '|='
### augassign: '^='
### augassign: '<<='
### augassign: '>>='
### augassign: '**='
### augassign: '//='

# -

### print_stmt: 'print'
### print_stmt: 'print' SPACE [ test ]
### print_stmt: 'print' SPACE [ test [SPACE] [','] ]
### print_stmt: 'print' SPACE [ test ([SPACE] ',' [SPACE] test)* [SPACE] [','] ]
### print_stmt: 'print' [SPACE] '>>' [SPACE] test
### print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ ]
### print_stmt: 'print' [SPACE] '>>' [SPACE] test [ ([SPACE] ',' [SPACE] test)+ [SPACE] [',']]

# -

### del_stmt: 'del' SPACE exprlist

# -

### flow_stmt: break_stmt
### flow_stmt: continue_stmt
### flow_stmt: return_stmt
### flow_stmt: raise_stmt
### flow_stmt: yield_stmt

# -

### return_stmt: 'return'
### return_stmt: 'return' SPACE [testlist]

# -

### yield_stmt: yield_expr

# -

### raise_stmt: 'raise'
### raise_stmt: 'raise' SPACE [test]
### raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test]]
### raise_stmt: 'raise' [SPACE test [[SPACE] ',' [SPACE] test [[SPACE] ',' [SPACE] test]]]

# -

### exec_stmt: 'exec' SPACE expr
### exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test]
### exec_stmt: 'exec' SPACE expr [SPACE 'in' SPACE test [[SPACE] ',' [SPACE] test]]

# -

### assert_stmt: 'assert' SPACE test
### assert_stmt: 'assert' SPACE test [[SPACE] ',' [SPACE] test]

# -

### compound_stmt: if_stmt
### compound_stmt: while_stmt
### compound_stmt: for_stmt
### compound_stmt: try_stmt
### compound_stmt: with_stmt
### compound_stmt: funcdef
### compound_stmt: classdef
# compound_stmt: decorated

# -

### if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite
### if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)*
### if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ['else' SPACE ':' [SPACE] suite]
### if_stmt: 'if' SPACE test [SPACE] ':' [SPACE] suite ('elif' SPACE test [SPACE] ':' [SPACE] suite)* ['else' SPACE ':' [SPACE] suite]

# -

### while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite
### while_stmt: 'while' SPACE test [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

### for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite
### for_stmt: 'for' SPACE exprlist SPACE 'in' SPACE testlist [SPACE] ':' [SPACE] suite ['else' [SPACE] ':' [SPACE] suite]

# -

### try_stmt: 'try' [SPACE] ':' [SPACE] suite 'finally' [SPACE] ':' suite
### try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+
### try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite]
### try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['finally' [SPACE] ':' suite]
### try_stmt: 'try' [SPACE] ':' [SPACE] suite (except_clause [SPACE] ':' [SPACE] suite)+ ['else' [SPACE] ':' [SPACE] suite] ['finally' [SPACE] ':' suite]

# -

### with_stmt: 'with' SPACE with_item [SPACE] ':' [SPACE] suite
### with_stmt: 'with' SPACE with_item ([SPACE] ',' [SPACE] with_item)* [SPACE] ':' [SPACE] suite

# -

### with_item: test
### with_item: test [SPACE 'as' SPACE expr]

# -

### except_clause: 'except' [SPACE test [(SPACE 'as' SPACE | [SPACE] ',' [SPACE]) test]]

# -

### testlist_safe: old_test
### testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+]
### testlist_safe: old_test [([SPACE] ',' [SPACE] old_test)+ [SPACE] [',']]

# -

### old_test: or_test
### old_test: old_lambdef

# -

### old_lambdef: 'lambda' [space] ':' [space] old_test
### old_lambdef: 'lambda' space [varargslist] [space] ':' [space] old_test

# -

### test: lambdef
### test: or_test
### test: or_test [SPACE 'if' SPACE or_test SPACE 'else' SPACE test]

# -

### or_test: and_test
### or_test: and_test (SPACE 'or' SPACE and_test)*

# -

### and_test: not_test
### and_test: not_test (SPACE 'and' SPACE not_test)*

# -

### not_test: 'not' SPACE not_test
### not_test: comparison

# -

### comparison: expr
### comparison: expr (comp_op expr)*

# -

### comp_op: '<'
### comp_op: '>'
### comp_op: '=='
### comp_op: '>='
### comp_op: '<='
### comp_op: '<>'
### comp_op: '!='
### comp_op: 'in'
### comp_op: 'not' SPACE 'in'
### comp_op: 'is'
### comp_op: 'is' SPACE 'not'

# -

### expr: xor_expr
### expr: xor_expr ([SPACE] '|' [SPACE] xor_expr)*

# -

### xor_expr: and_expr
### xor_expr: and_expr ([SPACE] '^' [SPACE] and_expr)*

# -

### and_expr: shift_expr
### and_expr: shift_expr ([SPACE] '&' [SPACE] shift_expr)*

# -

### shift_expr: arith_expr
### shift_expr: arith_expr ([SPACE] ('<<'|'>>') [SPACE] arith_expr)*

# -

### arith_expr: term
### arith_expr: term ([SPACE] ('+'|'-') [SPACE] term)*

# -

### term: factor
### term: factor ([SPACE] ('*'|'/'|'%'|'//') [SPACE] factor)*

# -

### factor: ('+'|'-'|'~') [SPACE] factor
### factor: power

# -

### power: atom [SPACE] trailer* [[SPACE] '**' [SPACE] factor]

# -

### atom: '(' [SPACE] [testlist_comp] [SPACE] ')'
### atom: '(' [SPACE] [yield_expr] [SPACE] ')'
### atom: '[' [SPACE] [listmaker] [SPACE] ']'
### atom: '{' [SPACE] [dictorsetmaker] [SPACE] '}'
### atom: '`' [SPACE] testlist1 [SPACE] '`'
### atom: NAME
### atom: NUMBER
### atom: STRING+

# -

### listmaker: test
### listmaker: test [SPACE] list_for
### listmaker: test ([SPACE] ',' [SPACE] test)*
### listmaker: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

### testlist_comp: test
### testlist_comp: test [SPACE] comp_for
### testlist_comp: test ([SPACE] ',' [SPACE] test)*
### testlist_comp: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

### lambdef: 'lambda' [SPACE] ':' [SPACE] test
### lambdef: 'lambda' [SPACE] [varargslist] [SPACE] ':' [SPACE] test

# -

### trailer: '.' [SPACE] NAME
### trailer: '[' [SPACE] ']'
### trailer: '[' [SPACE] subscriptlist [SPACE] ']'
### trailer: '(' [SPACE] ')'
### trailer: '(' [SPACE] [arglist] [SPACE] ')'

# -

### subscriptlist: subscript
### subscriptlist: subscript [SPACE] [',']
### subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)*
### subscriptlist: subscript ([SPACE] ',' [SPACE] subscript)* [SPACE] [',']

# -

### subscript: test
### subscript: '.' [SPACE] '.' [SPACE] '.'
### subscript: [test] [SPACE] ':' [SPACE] [test] [SPACE] [sliceop]

# -

### sliceop: ':' [SPACE] [test]

# -

### exprlist: expr
### exprlist: expr [SPACE] [',']
### exprlist: expr ([SPACE] ',' [SPACE] expr)*
### exprlist: expr ([SPACE] ',' [SPACE] expr)* [SPACE] [',']

# -

### testlist: test
### testlist: test [SPACE] [',']
### testlist: test ([SPACE] ',' [SPACE] test)*
### testlist: test ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

### dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE]
### dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] [SPACE] [',']
### dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)*)
### dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] ([SPACE] ',' [SPACE] test [SPACE] ':' [SPACE] test)* [SPACE] [','])

### dictorsetmaker: test [SPACE] ':' [SPACE] test [SPACE] comp_for

### dictorsetmaker: test [SPACE] comp_for

### dictorsetmaker: test [SPACE]
### dictorsetmaker: test [SPACE] [SPACE] [',']
### dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)*
### dictorsetmaker: test [SPACE] ([SPACE] ',' [SPACE] test)* [SPACE] [',']

# -

### classdef: 'class' SPACE NAME [SPACE] ['(' [SPACE] [testlist] [SPACE] ')'] [SPACE] ':' [SPACE] suite

# -

### for reference
### arglist: (argument [SPACE] ',' [SPACE])* (argument [SPACE] [','] |'*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test] |'**' [SPACE] test)


### arglist: (argument [SPACE] ',' [SPACE])*
### arglist: argument [SPACE] [',']
### arglist: (argument [SPACE] ',' [SPACE])* argument [SPACE] [',']
### arglist: '**' [SPACE] test
### arglist: (argument [SPACE] ',' [SPACE])* '**' [SPACE] test

### arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]
### arglist: '*' [SPACE] test ([SPACE] ',' [SPACE] argument)* [[SPACE] ',' [SPACE] '**' [SPACE] test]

# -

### argument: test
### argument: test [SPACE comp_for]
### argument: test [SPACE] '=' [SPACE] test

# -

### list_iter: list_if
### list_iter: list_for

# -

### list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe
### list_for: 'for' SPACE exprlist SPACE 'in' SPACE testlist_safe [SPACE list_iter]

# -

### list_if: 'if' SPACE old_test
### list_if: 'if' SPACE old_test [SPACE list_iter]

# -

### comp_iter: comp_if
### comp_iter: comp_for

# -

### comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test
### comp_for: 'for' SPACE exprlist SPACE 'in' SPACE or_test [SPACE comp_iter]

# -

### comp_if: 'if' SPACE old_test
### comp_if: 'if' SPACE old_test [SPACE comp_iter]

# -

### testlist1: test
### testlist1: test ([SPACE] ',' [SPACE] test)*

# -

### yield_expr: 'yield'
### yield_expr: 'yield' [SPACE testlist]

# -

# don't think I'm going to do this one
# single_input: NEWLINE
# single_input: simple_stmt
# single_input: compound_stmt [SPACE] NEWLINE

# -

### file_input: ([SPACE] NEWLINE | stmt)* [SPACE] ENDMARKER

# -

# don't think I'm going to do this one
# eval_input: testlist ([SPACE] NEWLINE)* [SPACE] ENDMARKER

# ---

# KEYWORDS: "and as assert break class continue def del elif else except exec finally for from global if import in is lambda not or pass print raise return try while with yield"

from rply.token import Token
from rply import ParserGenerator

from tokenizer import TOKENS, KEYWORDS, tokenize
from utils import create_node_from_token
from grammator_imports import include_imports
from grammator_control_structures import include_control_structures
from grammator_primitives import include_primivites
from grammator_operators import include_operators
from grammator_data_structures import include_data_structures


pg = ParserGenerator(tuple(map(lambda x: x.upper(), KEYWORDS)) + zip(*TOKENS)[1] + ("ENDMARKER", "INDENT", "DEDENT"), cache_id="baron")
        # precedence=[("left", ['PLUS', 'MINUS'])], cache_id="baron")


@pg.production("main : statements")
def main((statements,)):
    return filter(None, statements) if statements else []


@pg.production("statements : statements statement")
def statements_statement((statements, statement)):
    return statements + statement


@pg.production("statements : statement SEMICOLON?")
def statement((statement, semicolon)):
    if semicolon:
        return statement + [{"type": "semicolon", "value": ";"}]
    return statement


@pg.production("statement : ENDL")
def endl((endl,)):
    return [{"type": "endl", "value": endl.value}]


@pg.production("statement : ENDMARKER")
def end((endmarker)):
    return [None]


@pg.production("statement : simple_stmt")
@pg.production("statement : compound_stmt")
def statement_simple_statement((stmt,)):
    return stmt

@pg.production("statement : COMMENT ENDL")
def comment((comment_, endl)):
    return [{
        "type": "comment",
        "value": comment_.value,
        "space": comment_.before_space,
    }, {
        "type": "endl",
        "value": endl.value
    }]

@pg.production("simple_stmt : small_stmt SEMICOLON? ENDL")
def simple_stmt((small_stmt, semicolon, endl_)):
    if semicolon:
        return [small_stmt, {"type": "semicolon", "value": ";", "before_space": semicolon.before_space, "after_space": semicolon.after_space}] + endl((endl_,))
    return [small_stmt] + endl((endl_,))


@pg.production("simple_stmt : small_stmt SEMICOLON simple_stmt")
def simple_stmt_semicolon((small_stmt, semicolon, simple_stmt)):
    return [small_stmt, {"type": "semicolon", "value": ";", "before_space": semicolon.before_space, "after_space": semicolon.after_space}] + simple_stmt


@pg.production("small_stmt : flow_stmt")
@pg.production("small_stmt : del_stmt")
@pg.production("small_stmt : pass_stmt")
@pg.production("small_stmt : assert_stmt")
@pg.production("small_stmt : raise_stmt")
@pg.production("small_stmt : global_stmt")
@pg.production("small_stmt : print_stmt")
@pg.production("compound_stmt : if_stmt")
@pg.production("compound_stmt : while_stmt")
@pg.production("compound_stmt : for_stmt")
@pg.production("compound_stmt : try_stmt")
@pg.production("compound_stmt : funcdef")
@pg.production("compound_stmt : classdef")
@pg.production("compound_stmt : with_stmt")
@pg.production("compound_stmt : decorated")
def small_and_compound_stmt((statement,)):
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
def term_factor((level,)):
    return level


@pg.production("with_stmt : WITH with_items COLON suite")
def with_stmt((with_, with_items, colon, suite)):
    return [{
        "type": "with",
        "value": suite,
        "first_space": with_.after_space,
        "second_space": colon.before_space,
        "third_space": colon.after_space,
        "contexts": with_items
    }]


@pg.production("with_items : with_items comma with_item")
def with_items_with_item((with_items, comma, with_item,)):
    return with_items + [comma, with_item]


@pg.production("with_items : with_item")
def with_items((with_item,)):
    return [with_item]


@pg.production("with_item : test")
def with_item((test,)):
    return {
        "type": "with_context_item",
        "as": {},
        "first_space": "",
        "second_space": "",
        "value": test
    }


@pg.production("with_item : test AS expr")
def with_item_as((test, as_, expr)):
    return {
        "type": "with_context_item",
        "as": expr,
        "first_space": as_.before_space,
        "second_space": as_.after_space,
        "value": test
    }


@pg.production("classdef : CLASS NAME COLON suite")
def class_stmt((class_, name, colon, suite),):
    return [{
        "type": "class",
        "name": name.value,
        "parenthesis": False,
        "first_space": class_.after_space,
        "second_space": "",
        "third_space": "",
        "forth_space": "",
        "fith_space": "",
        "inherit_from": [],
        "value": suite,
    }]


@pg.production("classdef : CLASS NAME LEFT_PARENTHESIS RIGHT_PARENTHESIS COLON suite")
def class_stmt_parenthesis((class_, name, left_parenthesis, right_parenthesis, colon, suite),):
    return [{
        "type": "class",
        "name": name.value,
        "parenthesis": True,
        "first_space": class_.after_space,
        "second_space": left_parenthesis.before_space,
        "third_space": left_parenthesis.after_space,
        "forth_space": right_parenthesis.before_space,
        "fith_space": right_parenthesis.after_space,
        "inherit_from": [],
        "value": suite,
    }]


@pg.production("classdef : CLASS NAME LEFT_PARENTHESIS testlist RIGHT_PARENTHESIS COLON suite")
def class_stmt_inherit((class_, name, left_parenthesis, testlist, right_parenthesis, colon, suite),):
    return [{
        "type": "class",
        "name": name.value,
        "parenthesis": True,
        "first_space": class_.after_space,
        "second_space": left_parenthesis.before_space,
        "third_space": left_parenthesis.after_space,
        "forth_space": right_parenthesis.before_space,
        "fith_space": right_parenthesis.after_space,
        "inherit_from": [testlist],
        "value": suite,
    }]


@pg.production("decorated : AT dotted_name ENDL funcdef")
def decorated((at, dotted_name, endl, funcdef)):
    decorator = [{
        "type": "decorator",
        "value": {
            "value": dotted_name,
            "type": "dotted_name",
        },
        "space": "",
    }, {"type": "endl", "value": "\n"}]
    funcdef[0]["decorators"] += decorator
    return funcdef


@pg.production("funcdef : DEF NAME LEFT_PARENTHESIS parameters RIGHT_PARENTHESIS COLON suite")
def function_definition((def_, name, left_parenthesis, parameters, right_parenthesis, colon, suite)):
    return [{
        "type": "funcdef",
        "decorators": [],
        "name": name.value,
        "first_space": def_.after_space,
        "second_space": left_parenthesis.before_space,
        "third_space": left_parenthesis.after_space,
        "forth_space": right_parenthesis.before_space,
        "fith_space": colon.before_space,
        "arguments": parameters,
        "value": suite,
    }]

@pg.production("argslist : argslist argument")
@pg.production("parameters : parameters parameter")
def parameters_parameters_parameter((parameters, parameter,),):
    return parameters + parameter

@pg.production("argslist : argument")
@pg.production("parameters : parameter")
def parameters_parameter((parameter,),):
    return parameter

@pg.production("argument :")
@pg.production("parameter : ")
def parameter_empty(p):
    return []

@pg.production("name : NAME")
def name((name_,)):
    return {
        "type": "name",
        "value": name_.value,
    }

@pg.production("argument : test")
@pg.production("parameter : name")
def parameter_one((name,)):
    return [{
        "type": "argument",
        "first_space": "",
        "second_space": "",
        "default": {},
        "value": name
    }]

# really strange that left part of argument grammar can be a test
# I guess it's yet another legacy mistake
# python give me 'SyntaxError: keyword can't be an expression' when I try to
# put something else than a name (looks like a custom SyntaxError)
@pg.production("argument : test EQUAL test")
def named_argument((name, equal, test)):
    return [{
        "type": "argument",
        "first_space": equal.before_space,
        "second_space": equal.after_space,
        "value": test,
        "name": name
    }]

@pg.production("parameter : name EQUAL test")
def parameter_with_default((name, equal, test)):
    return [{
        "type": "argument",
        "first_space": equal.before_space,
        "second_space": equal.after_space,
        "default": test,
        "value": name
    }]

@pg.production("argument : test comp_for")
def generator_comprehension((test, comp_for,)):
    return [{
        "type": "argument_generator_comprehension",
        "result": test,
        "generators": comp_for,
    }]

@pg.production("argument : STAR test")
def argument_star((star, test,)):
    return [{
        "type": "list_argument",
        "space": star.after_space,
        "value": test,
    }]

@pg.production("argument : DOUBLE_STAR test")
def argument_star_star((double_star, test,)):
    return [{
        "type": "dict_argument",
        "first_space": double_star.after_space,
        "second_space": double_star.after_space,
        "value": test,
    }]

# TODO refactor those 2 to uniformise with argument_star and argument_star_star
@pg.production("parameter : STAR NAME")
def parameter_star((star, name,)):
    return [{
        "type": "list_argument",
        "first_space": star.after_space,
        "name": name.value,
    }]

@pg.production("parameter : DOUBLE_STAR NAME")
def parameter_star_star((double_star, name,)):
    return [{
        "type": "dict_argument",
        "first_space": double_star.after_space,
        "second_space": double_star.after_space,
        "name": name.value,
    }]

@pg.production("argument : comma")
@pg.production("parameter : comma")
def parameter_comma((comma,)):
    return [comma]

@pg.production("suite : simple_stmt")
def suite((simple_stmt,)):
    return simple_stmt


@pg.production("suite : endls INDENT statements DEDENT")
def suite_indent((endls, indent, statements, dedent,)):
    return endls + statements


@pg.production("endls : endls ENDL")
@pg.production("endls : ENDL")
def endls(p):
    if len(p) == 1:
        return [{"type": "endl", "value": "\n", "indent": p[0].after_space}]
    return p[0] + [{"type": "endl", "value": "\n", "indent": p[1].after_space}]

include_imports(pg)
include_control_structures(pg)
include_primivites(pg)
include_operators(pg)
include_data_structures(pg)

@pg.production("atom : LEFT_PARENTHESIS yield_expr RIGHT_PARENTHESIS")
def yield_atom((left_parenthesis, yield_expr, right_parenthesis)):
    return {
        "type": "yield_atom",
        "value": yield_expr["value"],
        "first_space": left_parenthesis.after_space,
        "second_space": right_parenthesis.before_space,
        "third_space": yield_expr["space"]
    }

@pg.production("atom : BACKQUOTE testlist1 BACKQUOTE")
def repr_atom((backquote, testlist1, backquote2)):
    return {
        "type": "repr",
        "value": testlist1,
        "first_space": backquote.after_space,
        "second_space": backquote2.before_space,
    }

@pg.production("testlist1 : test comma testlist1")
def testlist1_double((test, comma, test2,)):
    return [test, comma] + test2

@pg.production("testlist1 : test")
def testlist1((test,)):
    return [test]

@pg.production("atom : INT")
def int((int_,)):
    return create_node_from_token(int_, section="number")


@pg.production("atom : NAME")
def name((name,)):
    return create_node_from_token(name)


@pg.production("atom : STRING")
def string((string_,)):
    return create_node_from_token(string_)


@pg.production("comma : COMMA")
def comma((comma,)):
    return {
        "type": "comma",
        "first_space": comma.before_space,
        "second_space": comma.after_space,
    }

parser = pg.build()


def fake_lexer(sequence):
    for i in tokenize(sequence):
        if i is None:
            yield None
        yield Token(*i)


def parse(sequence):
    return parser.parse(fake_lexer(sequence))
