from spliter import split
from grouper import group
from tokenizer import tokenize
from space_grouper import group as space_group
from grammator import parser, Token


def _parse(tokens):
    return parser.parse(iter(map(lambda x: Token(*x) if x else x, tokens)))


def parse(pouet):
    if pouet and pouet[-1] != "\n":
        pouet += "\n"
    return _parse(space_group(tokenize(group(split(pouet)))))
