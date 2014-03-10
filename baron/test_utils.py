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
    if not source_code.endswith("\n"):
        source_code += "\n"

    try:
        open("/tmp/c", "w").write(source_code)
        open("/tmp/d", "w").write(dumps(baron_parse(source_code)))
    except Exception as e:
        import sys
        import json
        import traceback
        traceback.print_exc(file=sys.stdout)
        print "Warning: couldn't write dumps output to debug file, exception: %s" % e
        print
        print "Tree: %s" % json.dumps(baron_parse(source_code), indent=4)

    assert dumps(baron_parse(source_code)) == source_code
