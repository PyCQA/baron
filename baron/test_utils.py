from grammator import generate_parse
from dumper import dumps
from baron import parse as baron_parse


parse = generate_parse(False)


def parse_simple(tokens, result):
    if not tokens or tokens[-1][0] != "ENDL":
        tokens += [('ENDL', '\n')]
    assert parse(tokens + [('ENDMARKER', ''), None]) == (result + [{"type": "endl", "value": "\n", "formatting": [], "indent": ""}])


def parse_multi(tokens, result):
    assert parse(tokens + [('ENDMARKER', ''), None]) == result


def check_dumps(source_code):
    assert dumps(baron_parse(source_code)) == source_code
