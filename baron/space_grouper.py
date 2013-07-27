from utils import FlexibleIterator

PRIORITY_ORDER = (
    "IMPORT",
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
    while True:
        if iterator.end():
            return

        current = iterator.next()

        if current[0] == "SPACE" and iterator.show_next()[0] in GROUP_SPACE_BEFORE:
            new_current = iterator.next()
            current = (new_current[0], new_current[1], current[1])

        if current[0] in GROUP_SPACE_AFTER and\
            (iterator.show_next() and iterator.show_next()[0] == "SPACE") and\
            (iterator.show_next(2) and not less_prioritary_than(current[0], iterator.show_next(2)[0])):
            _, space_value = iterator.next()
            current = (current[0], current[1], current[2] if len(current) > 2 else '', space_value)

        assert current[0] != "SPACE"
        yield current
