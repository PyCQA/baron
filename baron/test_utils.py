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
    return {
        "type": "space",
        "value": value,
    }

def name(value):
    return {
        "type": "name",
        "value": value,
    }

def endl(value, **kwargs):
    return _node("endl", value, space="", indent="", **kwargs)

def importeu(value, **kwargs):
    return _node("import", value, **kwargs)

def dotted_as_name(value, before_space="", after_space="", **kwargs):
    return _node("dotted_as_name", value, before_space=before_space, after_space=after_space, **kwargs)

def from_import(value, targets, before_space=" ", middle_space=" ", after_space=" ", **kwargs):
    return _node("from_import", value, targets=targets, before_space=before_space, middle_space=middle_space, after_space=after_space, **kwargs)

def name_as_name(value, before_space="", after_space="", **kwargs):
    return _node("name_as_name", value, before_space=before_space, after_space=after_space, **kwargs)

def binary_operator(operator, first, second, first_space, second_space):
    return {
        "type": "binary_operator",
        "value": operator,
        "first": first,
        "second": second,
        "first_space": first_space,
        "second_space": second_space
    }
