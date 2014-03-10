from grammator import generate_parse


parse = generate_parse(False)


def parse_simple(tokens, result):
    if not tokens or tokens[-1][0] != "ENDL":
        tokens += [('ENDL', '\n')]
    assert parse(tokens + [('ENDMARKER', ''), None]) == (result + [{"type": "endl", "value": "\n", "formatting": [], "indent": ""}])


def parse_multi(tokens, result):
    assert parse(tokens + [('ENDMARKER', ''), None]) == result
