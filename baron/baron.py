from ast import parse as python_ast_parse

from rply.errors import ParsingError

from utils import PrintFunctionImportFinder
from spliter import split
from grouper import group
from tokenizer import tokenize as _tokenize
from formatting_grouper import group as space_group
from grammator import generate_parse
from indentation_marker import mark_indentation
from inner_formatting_grouper import group as inner_group


parse_tokens = generate_parse(False)
parse_tokens_print_function = generate_parse(True)


def _parse(tokens, print_function):
    parser = parse_tokens if not print_function else parse_tokens_print_function
    try:
        return parser(tokens)
    except ParsingError:
        # swap parsers for print_function situation where I failed to find it
        parser = parse_tokens if print_function else parse_tokens_print_function
        return parser(tokens)


def parse(source_code, print_function=None):
    if print_function is None:
        print_function_finder = PrintFunctionImportFinder()
        print_function_finder.visit(python_ast_parse(source_code))
        print_function = print_function_finder.print_function

    if source_code and source_code[-1] != "\n":
        source_code += "\n"
    return _parse(tokenize(source_code, print_function), print_function)


def tokenize(pouet, print_function=False):
    return mark_indentation(inner_group(space_group(_tokenize(group(split(pouet)), print_function))))
