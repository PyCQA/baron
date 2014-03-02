from grammator import parser, Token

def parse_simple(tokens, result):
    if not tokens or tokens[-1][0] != "ENDL":
        tokens += [('ENDL', '\n')]
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [('ENDMARKER', ''), None]))) == (result + [{"type": "endl", "value": "\n", "space": "", "indent": ""}])

def parse_multi(tokens, result):
    assert parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens + [('ENDMARKER', ''), None]))) == result

def _node(typeu, value, **kwargs):
    if kwargs is not None:
        to_return = {"type": typeu, "value": value}
        to_return.update(kwargs)
        return to_return
    return {"type": typeu, "value": value}

def space(value=" "):
    return _node("space", value)

def name(value):
    return _node("name", value)

def inteu(value):
    return _node("int", value, section="number")

def string(value):
    return _node("string", value)

def endl(value, **kwargs):
    return _node("endl", value, space="", indent="", **kwargs)

def dot():
    return _node("dot", ".")

def expression(value):
    return _node("expression", value)

def dotted_name(value):
    return _node("dotted_name", value)

def importeu(value, **kwargs):
    return _node("import", value, **kwargs)

def dotted_as_name(value, before_space="", after_space="", **kwargs):
    return _node("dotted_as_name", value, before_space=before_space, after_space=after_space, **kwargs)

def comma():
    return _node("comma", ",")

def from_import(value, targets, before_space=" ", middle_space=" ", after_space=" ", **kwargs):
    return _node("from_import", value, targets=targets, before_space=before_space, middle_space=middle_space, after_space=after_space, **kwargs)

def name_as_name(value, before_space="", after_space="", **kwargs):
    return _node("name_as_name", value, before_space=before_space, after_space=after_space, **kwargs)

def left_parenthesis():
    return _node('left_parenthesis', '(')

def right_parenthesis():
    return _node('right_parenthesis', ')')

def star():
    return _node('star', '*')

def binary_operator(operator, first, second, first_space, second_space):
    return _node('binary_operator', operator, first=first, second=second, first_space=first_space, second_space=second_space)

def unitary_operator(operator, target, space):
    return _node('unitary_operator', operator, target=target, space=space)

