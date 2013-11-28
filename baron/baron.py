from spliter import split
from grouper import group
from tokenizer import tokenize as _tokenize
from space_grouper import group as space_group
from grammator import parser, Token
from indentation_marker  import mark_indentation


def _parse(tokens):
    return parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens) + [None]))


def parse(pouet):
    if pouet and pouet[-1] != "\n":
        pouet += "\n"
    return _parse(mark_indentation(space_group(_tokenize(group(split(pouet))))))


def tokenize(pouet):
    return mark_indentation(space_group(_tokenize(group(split(pouet)))))
