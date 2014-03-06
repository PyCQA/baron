from spliter import split
from grouper import group
from tokenizer import tokenize as _tokenize
from space_grouper import group as space_group
from grammator import parser, Token
from indentation_marker  import mark_indentation
from inner_formatting_grouper import group as inner_group


def _parse(tokens):
    return parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens) + [None]))


def parse(pouet):
    if pouet and pouet[-1] != "\n":
        pouet += "\n"
    return _parse(inner_group(mark_indentation(space_group(_tokenize(group(split(pouet)))))))


def tokenize(pouet):
    return inner_group(mark_indentation(space_group(_tokenize(group(split(pouet))))))
