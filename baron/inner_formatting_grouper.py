from utils import FlexibleIterator

GROUP_THOSE = (
    "ENDL",
)

GROUP_ON = (
    "LEFT_PARENTHESIS",
    #"AS",
    #"IMPORT",
    #"DOUBLE_STAR",
    #"DOT",
    #"LEFT_SQUARE_BRACKET",
    #"STAR",
    #"SLASH",
    #"PERCENT",
    #"DOUBLE_SLASH",
    #"PLUS",
    #"MINUS",
    #"LEFT_SHIFT",
    #"RIGHT_SHIFT",
    #"AMPER",
    #"CIRCUMFLEX",
    #"VBAR",
    #"LESS",
    #"GREATER",
    #"EQUAL_EQUAL",
    #"LESS_EQUAL",
    #"GREATER_EQUAL",
    #"LESS_GREATER",
    #"NOT_EQUAL",
    #"IN",
    #"IS",
    #"NOT",
    #"AND",
    #"OR",
    #"IF",
    #"ELSE",
    #"EQUAL",
    #"PLUS_EQUAL",
    #"MINUS_EQUAL",
    #"STAR_EQUAL",
    #"SLASH_EQUAL",
    #"PERCENT_EQUAL",
    #"AMPER_EQUAL",
    #"VBAR_EQUAL",
    #"CIRCUMFLEX_EQUAL",
    #"LEFT_SHIFT_EQUAL",
    #"RIGHT_SHIFT_EQUAL",
    #"DOUBLE_STAR_EQUAL",
    #"DOUBLE_SLASH_EQUAL",
    #"ENDL",
    #"COMMA",
    #"FOR",
    #"COLON"
)


def append_to_token_after(token, to_append_list):
    if len(token) == 2:
        return (token[0], token[1], '', '', [], to_append_list)
    elif len(token) == 3:
        return (token[0], token[1], token[2], '', [], to_append_list)
    elif len(token) == 4:
        return (token[0], token[1], token[2], token[3], [], to_append_list)
    elif len(token) == 6:
        return (token[0], token[1], token[2], token[3], token[4], token[5] + to_append_list)


def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    while True:
        if iterator.end():
            return

        current = iterator.next()

        if current[0] in GROUP_ON:
            while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                current = append_to_token_after(current, [iterator.next()])

        yield current
