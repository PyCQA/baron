from .spliter import split
from .grouper import group
from .tokenizer import tokenize as _tokenize
from .formatting_grouper import group as space_group
from .future import has_print_function, replace_print_by_name
from .grammator import generate_parse
from .indentation_marker import mark_indentation
from .inner_formatting_grouper import group as inner_group
from .parser import ParsingError


parse_tokens = generate_parse(False)
parse_tokens_print_function = generate_parse(True)


def _parse(tokens, print_function):
    parser = parse_tokens if not print_function else parse_tokens_print_function
    try:
        try:
            return parser(tokens)
        except ParsingError:
            # swap parsers for print_function situation where I failed to find it
            parser = parse_tokens if print_function else parse_tokens_print_function
            return parser(tokens)
    except ParsingError as e:
        raise e
    except Exception as e:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.stderr.write("%s\n" % e)
        sys.stderr.write("\nBaron has failed to parse this input. If this is valid python code (and by that I mean that the python binary successfully parse this code without any syntax error) (also consider that python does not yet parse python 3 code integrally) it would be kind if you can extract a snippet of your code that make Baron fails and open a bug here: https://github.com/Psycojoker/baron/issues\n\nSorry for the inconvenience.")


def parse(source_code, print_function=None):
    # Python syntax requires source code to end with an ENDL token
    # the endl token is removed afterward if and only if it's the last token of the root level
    # It is possible that this token end up in a 'suite' grammar rule
    # which means that it is 'traped' in an indented block of code
    # I don't want to recursively cross the tree to hope to find it
    # This solution behave in the expected way for 90% of the case
    newline_appended = False
    linesep = "\r\n" if source_code.endswith("\r\n") else "\n"
    if source_code and not source_code.endswith(linesep):
        source_code += linesep
        newline_appended = True

    if print_function is None:
        tokens = tokenize(source_code, False)
        print_function = has_print_function(tokens)
        if print_function:
            replace_print_by_name(tokens)
    else:
        tokens = tokenize(source_code, print_function)

    if newline_appended:
        to_return = _parse(tokens, print_function)

        if to_return[-1]["type"] == "endl" and not to_return[-1]["formatting"]:
            return to_return[:-1]
        elif to_return[-1]["type"] == "endl" and to_return[-1]["formatting"]:
            return to_return[:-1] + to_return[-1]["formatting"]
        else:
            return to_return

    return _parse(tokens, print_function)


def tokenize(pouet, print_function=False):
    return mark_indentation(inner_group(space_group(_tokenize(group(split(pouet)), print_function))))
