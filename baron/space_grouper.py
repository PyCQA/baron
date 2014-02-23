from utils import FlexibleIterator

class UnExpectedSpaceToken(Exception):
    pass

PRIORITY_ORDER = (
    "IMPORT",
    "ENDL",
)

BOTH = (
    "AS",
    "IMPORT",
    "DOUBLE_STAR",
    "DOT",
    "LEFT_SQUARE_BRACKET",
    "LEFT_PARENTHESIS",
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
    "LESS_GREATER",
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
    "COMMA",
    "COLON"
)

GROUP_SPACE_BEFORE = BOTH + (
    "RIGHT_PARENTHESIS",
)

GROUP_SPACE_AFTER = BOTH + (
    "FROM",
    "TILDE",
    "RETURN",
    "YIELD",
    "DEL",
    "ASSERT",
    "RAISE",
    "EXEC",
    "GLOBAL",
    "PRINT",
    "INDENT",
    "ENDL",
    "WHILE",
    "ELIF",
    "FOR",
    "EXCEPT",
    "DEF",
    "CLASS",
    "LAMBDA",
)

def less_prioritary_than(a, b):
    if b not in PRIORITY_ORDER:
        return False

    if a not in PRIORITY_ORDER:
        return True

    return PRIORITY_ORDER.index(a) < PRIORITY_ORDER.index(b)

def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    debug_file_content = ""
    debug_previous_token = None
    while True:
        if iterator.end():
            return

        debug_previous_token = current
        current = iterator.next()

        if current is None:
            return

        debug_file_content += current[1]

        if current[0] == "SPACE" and iterator.show_next()[0] in GROUP_SPACE_BEFORE:
            debug_previous_token = current
            new_current = iterator.next()
            debug_file_content += new_current[1]
            current = (new_current[0], new_current[1], current[1])

        if current[0] in GROUP_SPACE_AFTER and\
            (iterator.show_next() and iterator.show_next()[0] == "SPACE") and\
            (iterator.show_next(2) and not less_prioritary_than(current[0], iterator.show_next(2)[0])):
            debug_previous_token = current
            _, space_value = iterator.next()
            debug_file_content += space_value
            current = (current[0], current[1], current[2] if len(current) > 2 else '', space_value)

        if current[0] == "SPACE":
            debug_file_content = debug_file_content.split("\n")
            debug_file_content = zip(range(1, len(debug_file_content) + 1), debug_file_content)
            debug_file_content = debug_file_content[-3:]
            debug_file_content = "\n".join(map(lambda x: "%4s %s" % (x[0], x[1]), debug_file_content))
            debug_file_content += "<--- here"
            debug_text = "Unexpected space token:\n\n" + debug_file_content + "\n\n"
            debug_text += "Should have been grouped on either %s (before) or %s (after) token." % (debug_previous_token, iterator.show_next())
            raise UnExpectedSpaceToken(debug_text)
        yield current
