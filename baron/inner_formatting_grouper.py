from .utils import FlexibleIterator, BaronError


class UnExpectedFormattingToken(BaronError):
        pass

class GroupingError(BaronError):
        pass


GROUP_THOSE = (
    "ENDL",

    # TODO test those 2
    "COMMENT",
    "SPACE",
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

    # TODO test everything bellow
    "STRING",
    "RAW_STRING",
    "BINARY_STRING",
    "BINARY_RAW_STRING",
    "UNICODE_STRING",
    "UNICODE_RAW_STRING",

    "AS",
    "IMPORT",
    "DOUBLE_STAR",
    "DOT",
    "LEFT_SQUARE_BRACKET",
    "STAR",
    "SLASH",
    "PERCENT",
    "DOUBLE_SLASH",
    "PLUS",
    "MINUS",
    "LEFT_SHIFT",
    "RIGHT_SHIFT",
    "AMPER",
    "CIRCUMFLEX",
    "VBAR",
    "LESS",
    "GREATER",
    "EQUAL_EQUAL",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "NOT_EQUAL",
    "IN",
    "IS",
    "NOT",
    "AND",
    "OR",
    "IF",
    "ELSE",
    "EQUAL",
    "PLUS_EQUAL",
    "MINUS_EQUAL",
    "STAR_EQUAL",
    "SLASH_EQUAL",
    "PERCENT_EQUAL",
    "AMPER_EQUAL",
    "VBAR_EQUAL",
    "CIRCUMFLEX_EQUAL",
    "LEFT_SHIFT_EQUAL",
    "RIGHT_SHIFT_EQUAL",
    "DOUBLE_STAR_EQUAL",
    "DOUBLE_SLASH_EQUAL",
    "ENDL",
    "FOR",
    "COLON",
    "RAW_STRING",
    "UNICODE_STRING",
    "UNICODE_RAW_STRING",
) + ENTER_GROUPING_MODE + QUIT_GROUPING_MODE


def append_to_token_after(token, to_append_list):
    if len(token) == 2:
        return (token[0], token[1], [], to_append_list)
    elif len(token) == 3:
        return (token[0], token[1], token[2], to_append_list)
    elif len(token) == 4:
        return (token[0], token[1], token[2], token[3] + to_append_list)


def append_to_token_before(token, to_append_list):
    if len(token) == 2:
        return (token[0], token[1], to_append_list, [])
    elif len(token) == 3:
        return (token[0], token[1], to_append_list + token[2], [])
    elif len(token) == 4:
        return (token[0], token[1],  to_append_list + token[2], token[3])


def group(sequence):
    return list(group_generator(sequence))


def fail_on_bad_token(token, debug_file_content, in_grouping_mode):
    if token[0] in GROUP_ON:
        return

    debug_file_content += _append_to_debug_file_content(token)

    debug_file_content = debug_file_content.split("\n")
    debug_file_content = list(zip(range(1, len(debug_file_content) + 1), debug_file_content))
    debug_file_content = debug_file_content[-8:]
    debug_file_content = "\n".join(["%4s %s" % (x[0], x[1]) for x in debug_file_content])
    raise GroupingError("Fail to group formatting tokens, here:\n%s <----\n\n'%s' should have been in: %s\n\nCurrent value of 'in_grouping_mode': %s" % (debug_file_content, token, ', '.join(sorted(GROUP_ON)), in_grouping_mode))


def _append_to_debug_file_content(token):
    before_debug = "".join(map(lambda x: x[1], token[2] if len(token) >= 3 else []))
    after_debug = "".join(map(lambda x: x[1], token[3] if len(token) >= 4 else []))
    return  before_debug + token[1] + after_debug


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    in_grouping_mode = 0
    debug_file_content = ""
    while True:
        if iterator.end():
            return

        debug_previous_token = current
        current = next(iterator)
        debug_file_content += _append_to_debug_file_content(current)

        if current[0] in ENTER_GROUPING_MODE:
            in_grouping_mode += 1
        elif current[0] in QUIT_GROUPING_MODE:
            in_grouping_mode -= 1

        if in_grouping_mode:
            if current[0] in GROUP_THOSE:
                to_group = [current]
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    to_group.append(next(iterator))
                    debug_file_content += _append_to_debug_file_content(to_group[-1])

                    # XXX don't remember how (:() but I can end up finding a
                    # DEDENT/INDENT token in this situation and I don't want to
                    # group on it. Need to do test for that.
                    if iterator.show_next()[0] in ("INDENT", "DEDENT"):
                        yield next(iterator)

                fail_on_bad_token(iterator.show_next(), debug_file_content, in_grouping_mode)
                current = append_to_token_before(next(iterator), to_group)

                # TODO test
                if current[0] in QUIT_GROUPING_MODE:
                    in_grouping_mode -= 1
                    yield current
                    continue


            if current[0] in GROUP_ON:
                while iterator.show_next() and iterator.show_next()[0] in GROUP_THOSE:
                    debug_file_content += _append_to_debug_file_content(iterator.show_next())
                    current = append_to_token_after(current, [next(iterator)])


        if current[0] == "SPACE":
            debug_file_content = debug_file_content.split("\n")
            debug_file_content = list(zip(range(1, len(debug_file_content) + 1), debug_file_content))
            debug_file_content = debug_file_content[-3:]
            debug_file_content = "\n".join(["%4s %s" % (x[0], x[1]) for x in debug_file_content])
            debug_file_content += "<--- here"
            debug_text = "Unexpected '%s' token:\n\n" % current[0].lower() + debug_file_content + "\n\n"
            debug_text += "Should have been grouped on either %s (before) or %s (after) token." % (debug_previous_token, iterator.show_next())
            raise UnExpectedFormattingToken(debug_text)

        yield current
