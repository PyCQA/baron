from grammator import parser, Token

def parse(tokens, result):
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
    return _node("endl", value, **kwargs)

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
