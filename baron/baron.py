from rply.errors import ParsingError

from spliter import split
from grouper import group
from tokenizer import tokenize as _tokenize
from formatting_grouper import group as space_group
from grammator import generate_parse
from indentation_marker  import mark_indentation
from inner_formatting_grouper import group as inner_group


parse_tokens = generate_parse(print_function=False)

def _parse(tokens):
    try:
        return parse_tokens(tokens)
    except ParsingError:
        # sooo horrible hack to handle grammar modification to please hipsters
        # TODO launch ast.py at some point to find "from __future__ import
        # print_function" or something like that
        return generate_parse(print_function=True)(tokens)


def parse(source_code):
    if source_code and source_code[-1] != "\n":
        source_code += "\n"
    return _parse(tokenize(source_code))


def tokenize(pouet):
    return mark_indentation(inner_group(space_group(_tokenize(group(split(pouet))))))
