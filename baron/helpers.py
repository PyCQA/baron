import json
import sys
from os import linesep
from . import parse


def show(source_code):
    sys.stdout.write(json.dumps(parse(source_code), indent=4) + linesep)


def show_file(target_file):
    with open(target_file, "r") as source_code:
        sys.stdout.write(json.dumps(parse(source_code.read()), indent=4) + linesep)


def show_node(node):
    sys.stdout.write(json.dumps(node, indent=4) + linesep)
