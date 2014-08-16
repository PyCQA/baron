import sys

from baron.grammator import generate_parse
from baron.dumper import dumps
from baron.baron import parse as baron_parse
from baron.utils import python_version

if python_version == 3:
    from itertools import zip_longest
else:
    from itertools import izip_longest
    zip_longest = izip_longest

parse = generate_parse(False)


def parse_simple(tokens, result):
    if not tokens or tokens[-1][0] != "ENDL":
        tokens += [('ENDL', '\n')]
    assert parse(tokens + [('ENDMARKER', ''), None]) == (result + [{"type": "endl", "value": "\n", "formatting": [], "indent": ""}])


def parse_multi(tokens, result):
    assert parse(tokens + [('ENDMARKER', ''), None]) == result


def check_dumps(source_code):
    try:
        open("/tmp/c", "w").write(source_code)
        open("/tmp/d", "w").write(dumps(baron_parse(source_code)))
    except Exception as e:
        import json
        import traceback
        traceback.print_exc(file=sys.stdout)
        sys.stdout.write("Warning: couldn't write dumps output to debug file, exception: %s\n\n" % e)
        sys.stdout.write("Tree: %s" % json.dumps(baron_parse(source_code), indent=4) + "\n")

    assert dumps(baron_parse(source_code), strict=True) == source_code
