from utils import FlexibleIterator

class UnExpectedFormattingToken(Exception):
        pass


GROUP_THOSE = (
    "ENDL",
)

ENTER_GROUPING_MODE = (
    "LEFT_PARENTHESIS",
    "LEFT_BRACKET",
    "LEFT_SQUARE_BRACKET",
)

QUIT_GROUPING_MODE = (
    "RIGHT_PARENTHESIS",
    "RIGHT_BRACKET",
    "RIGHT_SQUARE_BRACKET",
)

GROUP_ON = (
    "COMMA",
    "COLON",
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


def fail_on_bad_token(token, debug_file_content):
    if token in GROUP_ON:
        return

    debug_file_content = debug_file_content.split("\n")
    debug_file_content = zip(range(1, len(debug_file_content) + 1), debug_file_content)
    debug_file_content = debug_file_content[-3:]
    debug_file_content = "\n".join(map(lambda x: "%4s %s" % (x[0], x[1]), debug_file_content))
    raise Exception("Here:\n%s <----\n\n'%s' should have been in: %s" % (debug_file_content, token, ', '.join(sorted(GROUP_ON))))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    in_grouping_mode = 0
    debug_file_content = ""
    while True:
        if iterator.end():
            return

        debug_previous_token = current
        current = iterator.next()
        debug_file_content += current[1]

        if current[0] in ENTER_GROUPING_MODE:
            in_grouping_mode += 1
        elif current[0] in QUIT_GROUPING_MODE:
            in_grouping_mode -= 1

        if in_grouping_mode:
            if current[0] in GROUP_THOSE:
                to_group = [current]
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    to_group.append(iterator.next())
                    debug_file_content += to_group[-1][1]

                fail_on_bad_token(iterator.show_next()[0], debug_file_content)
                current = append_to_token_before(iterator.next(), to_group)

            if current[0] in GROUP_ON:
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    debug_file_content += iterator.show_next()[1]
                    current = append_to_token_after(current, [iterator.next()])


        if current[0] == "SPACE":
            debug_file_content = debug_file_content.split("\n")
            debug_file_content = zip(range(1, len(debug_file_content) + 1), debug_file_content)
            debug_file_content = debug_file_content[-3:]
            debug_file_content = "\n".join(map(lambda x: "%4s %s" % (x[0], x[1]), debug_file_content))
            debug_file_content += "<--- here"
            debug_text = "Unexpected '%s' token:\n\n" % current[0].lower() + debug_file_content + "\n\n"
            debug_text += "Should have been grouped on either %s (before) or %s (after) token." % (debug_previous_token, iterator.show_next())
            raise UnExpectedFormattingToken(debug_text)

        print current
        yield current
