import re

class UnknowItem(Exception):
    pass

KEYWORDS = ("and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "exec", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "not", "or", "pass", "print", "raise", "return", "try", "while", "with", "yield")

TOKENS = (
    (r'\.', 'DOT'),
    (r'[a-zA-Z_]\w*', 'NAME'),
    (r'[1-9]+\d*[lL]?', 'INT'),
    (r'\d*\.\d*[lL]?', 'FLOAT'),
    (r'0[xX][\da-fA-F]+[lL]?', 'HEXA'),
    (r'(0[oO][0-7]+)|(0[0-7]*)[lL]?', 'OCTA'),
    (r'\d+[eE][-+]?\d+', 'FLOAT_EXPONANT'),
    (r'\d*.\d*[eE][-+]?\d+', 'FLOAT_EXPONANT'),
    (r'\(', 'LEFT_PARENTHESIS'),
    (r'\)', 'RIGHT_PARENTHESIS'),
    (r':', 'COLON'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'STAR'),
    (r'/', 'SLASH'),
    (r'\|', 'VBAR'),
    (r'&', 'AMPER'),
    (r'<', 'LESS'),
    (r'>', 'GREATER'),
    (r'=', 'EQUAL'),
    (r'%', 'PERCENT'),
    (r'\[', 'LEFT_SQUARE_BRACKET'),
    (r'\]', 'RIGHT_SQUARE_BRACKET'),
    (r'`', 'BACKQUOTE'),
    (r'==', 'EQUAL_EQUAL'),
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
    (r'\*=', 'STAR_EQUAL'),
    (r'/=', 'SLASH_EQUAL'),
    (r'%=', 'PERCENT_EQUAL'),
    (r'&=', 'AMPER_EQUAL'),
    (r'\|=', 'VBAR_EQUAL'),
    (r'\^=', 'CIRCUMFLEX_EQUAL'),
    (r'<<=', 'LEFT_SHIFT_EQUAL'),
    (r'>>=', 'RIGHT_SHIFT_EQUAL'),
    (r'\*\*=', 'DOUBLE_STAR_EQUAL'),
    (r'//', 'DOUBLE_SLASH'),
    (r'//=', 'DOUBLE_SLASH_EQUAL'),
    (r'\n', 'ENDL'),
    (r'\r\n', 'ENDL'),
    (r'#.*', 'COMMENT'),
    (r'(\s|\\\n|\\\r\n)+', 'SPACE'),
    (r'["\'].*["\']', 'STRING'),
    (r'[uU]["\'].*["\']', 'UNICODE_STRING'),
    (r'[rR]["\'].*["\']', 'RAW_STRING'),
    (r'[bB]["\'].*["\']', 'BINARY_STRING'),
    (r'[uU][rR]["\'].*["\']', 'UNICODE_RAW_STRING'),
    (r'[bB][rR]["\'].*["\']', 'BINARY_RAW_STRING'),
)


TOKENS = map(lambda x: (re.compile('^' + x[0] + '$'), x[1]), TOKENS)


def tokenize(sequence):
    return list(tokenize_generator(sequence))


def tokenize_generator(sequence):
    for item in sequence:
        if item in KEYWORDS:
            yield (item.upper(), item)
            continue
        for candidate, token_name in TOKENS:
            if candidate.match(item):
                yield (token_name, item)
                break
        else:
            raise UnknowItem("Can't find a matching token for this item: '%s'" % item)
    yield

if __name__ == '__main__':
    from spliter import split
    from grouper import group
    import sys
    print tokenize(group(split(open(sys.argv[1]).read())))
