import json
from . import parse


def show(source_code):
    print json.dumps(parse(source_code), indent=4)


def show_file(target_file):
    with open(target_file, "r") as source_code:
        print json.dumps(parse(source_code.read()), indent=4)
