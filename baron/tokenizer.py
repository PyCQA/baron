import re
from .utils import BaronError


class UnknowItem(BaronError):
    pass


KEYWORDS = ("and", "as", "assert", "break", "class", "continue", "def", "del",
            "elif", "else", "except", "exec", "finally", "for", "from",
            "global", "nonlocal", "if", "import", "in", "is", "lambda", "not",
            "or", "pass", "print", "raise", "return", "try", "while", "with",
            "yield")

TOKENS = (
    (r'[a-zA-Z_]\w*', 'NAME'),
    (r'0', 'INT'),
    (r'[-+]?\d+[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'[-+]?\d+.\d?[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'[-+]?\d?.\d+[eE][-+]?\d+[jJ]', 'FLOAT_EXPONANT_COMPLEX'),
    (r'\d+[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\d+\.\d*[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\.\d+[eE][-+]?\d*', 'FLOAT_EXPONANT'),
    (r'\d*\.\d+[jJ]', 'COMPLEX'),
    (r'\d+\.[jJ]', 'COMPLEX'),
    (r'\d+[jJ]', 'COMPLEX'),
    (r'\d+\.', 'FLOAT'),
    (r'\d*[_\d]*\.[_\d]+[lL]?', 'FLOAT'),
    (r'\d+[_\d]+\.[_\d]*[lL]?', 'FLOAT'),
    (r'\.', 'DOT'),
    (r'[1-9]+[_\d]*[lL]', 'LONG'),
    (r'[1-9]+[_\d]*', 'INT'),
    (r'0[xX][\d_a-fA-F]+[lL]?', 'HEXA'),
    (r'(0[oO][0-7]+)|(0[0-7_]*)[lL]?', 'OCTA'),
    (r'0[bB][01_]+[lL]?', 'BINARY'),
    (r'\(', 'LEFT_PARENTHESIS'),
    (r'\)', 'RIGHT_PARENTHESIS'),
    (r':', 'COLON'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'@', 'AT'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'STAR'),
    (r'/', 'SLASH'),
    (r'\|', 'VBAR'),
    (r'&', 'AMPER'),
    (r'@', 'AT'),
    (r'<', 'LESS'),
    (r'>', 'GREATER'),
    (r'=', 'EQUAL'),
    (r'%', 'PERCENT'),
    (r'\[', 'LEFT_SQUARE_BRACKET'),
    (r'\]', 'RIGHT_SQUARE_BRACKET'),
    (r'\{', 'LEFT_BRACKET'),
    (r'\}', 'RIGHT_BRACKET'),
    (r'`', 'BACKQUOTE'),
    (r'==', 'EQUAL_EQUAL'),
    (r'<>', 'NOT_EQUAL'),
    (r'!=', 'NOT_EQUAL'),
    (r'<=', 'LESS_EQUAL'),
    (r'>=', 'GREATER_EQUAL'),
    (r'~', 'TILDE'),
    (r'\^', 'CIRCUMFLEX'),
    (r'<<', 'LEFT_SHIFT'),
    (r'>>', 'RIGHT_SHIFT'),
    (r'\*\*', 'DOUBLE_STAR'),
    (r'\+=', 'PLUS_EQUAL'),
    (r'-=', 'MINUS_EQUAL'),
    (r'@=', 'AT_EQUAL'),
    (r'\*=', 'STAR_EQUAL'),
    (r'/=', 'SLASH_EQUAL'),
    (r'%=', 'PERCENT_EQUAL'),
    (r'&=', 'AMPER_EQUAL'),
    (r'\|=', 'VBAR_EQUAL'),
    (r'\^=', 'CIRCUMFLEX_EQUAL'),
    (r'<<=', 'LEFT_SHIFT_EQUAL'),
    (r'>>=', 'RIGHT_SHIFT_EQUAL'),
    (r'\.\.\.', 'ELLIPSIS'),
    (r'->', 'RIGHT_ARROW'),
    (r'\*\*=', 'DOUBLE_STAR_EQUAL'),
    (r'//', 'DOUBLE_SLASH'),
    (r'//=', 'DOUBLE_SLASH_EQUAL'),
    (r'\n', 'ENDL'),
    (r'\r\n', 'ENDL'),
    (r'#.*', 'COMMENT'),
    (r'(\s|\\\n|\\\r\n)+', 'SPACE'),
    (r'["\'](.|\n|\r)*["\']', 'STRING'),
    (r'[uU]["\'](.|\n|\r)*["\']', 'UNICODE_STRING'),
    (r'[fF]["\'](.|\n|\r)*["\']', 'INTERPOLATED_STRING'),
    (r'[rR]["\'](.|\n|\r)*["\']', 'RAW_STRING'),
    (r'[bB]["\'](.|\n|\r)*["\']', 'BINARY_STRING'),
    (r'[uU][rR]["\'](.|\n|\r)*["\']', 'UNICODE_RAW_STRING'),
    (r'[bB][rR]["\'](.|\n|\r)*["\']', 'BINARY_RAW_STRING'),
    (r'[fF][rR]["\'](.|\n|\r)*["\']', 'INTERPOLATED_RAW_STRING'),
    (r'[rR][fF]["\'](.|\n|\r)*["\']', 'INTERPOLATED_RAW_STRING'),
)


TOKENS = [(re.compile('^' + x[0] + '$'), x[1]) for x in TOKENS]


def tokenize(sequence, print_function=False):
    return list(tokenize_generator(sequence, print_function))


def tokenize_current_keywords(print_function=False):
    if print_function is True:
        return [x for x in KEYWORDS if x not in ("print", "exec")]
    else:
        return KEYWORDS


def tokenize_generator(sequence, print_function=False):
    current_keywords = tokenize_current_keywords()

    for item in sequence:
        if item in current_keywords:
            yield (item.upper(), item)
            continue

        for candidate, token_name in TOKENS:
            if candidate.match(item):
                yield (token_name, item)
                break
        else:
            raise UnknowItem("Can't find a matching token for this item: '%s'" % item)
    yield ('ENDMARKER', '')
    yield
