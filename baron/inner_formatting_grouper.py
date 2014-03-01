from utils import FlexibleIterator

GROUP_THOSE = (
    "ENDL",
)

ENTER_GROUPING_MODE = (
    "LEFT_PARENTHESIS",
)

QUIT_GROUPING_MODE = (
    "RIGHT_PARENTHESIS",
)

GROUP_ON = (
    "COMMA",
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
    #"FOR",
    #"COLON"
) + ENTER_GROUPING_MODE + QUIT_GROUPING_MODE


def append_to_token_after(token, to_append_list):
    if len(token) == 2:
        return (token[0], token[1], '', '', [], to_append_list)
    elif len(token) == 3:
        return (token[0], token[1], token[2], '', [], to_append_list)
    elif len(token) == 4:
        return (token[0], token[1], token[2], token[3], [], to_append_list)
    elif len(token) == 6:
        return (token[0], token[1], token[2], token[3], token[4], token[5] + to_append_list)


def append_to_token_before(token, to_append_list):
    if len(token) == 2:
        return (token[0], token[1], '', '', to_append_list, [])
    elif len(token) == 3:
        return (token[0], token[1], token[2], '', to_append_list, [])
    elif len(token) == 4:
        return (token[0], token[1], token[2], token[3], to_append_list, [])
    #elif len(token) == 5:
        #return (token[0], token[1], token[2], token[3], token[4], to_append_list)
    elif len(token) == 6:
        return (token[0], token[1], token[2], token[3], token[4] + to_append_list, token[5])


def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    in_grouping_mode = 0
    while True:
        if iterator.end():
            return

        current = iterator.next()

        if current[0] in ENTER_GROUPING_MODE:
            in_grouping_mode += 1
        elif current[0] in QUIT_GROUPING_MODE:
            in_grouping_mode -= 1

        if in_grouping_mode:
            if current[0] in GROUP_THOSE:
                to_group = [current]
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    to_group.append(iterator.next())
                current = append_to_token_before(iterator.next(), to_group)

            if current[0] in GROUP_ON:
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    current = append_to_token_after(current, [iterator.next()])


        print current
        yield current
