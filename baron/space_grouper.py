from utils import FlexibleIterator

BOTH = (
    "AS",
    "IMPORT",
    "DOUBLE_STAR"
)

GROUP_SPACE_BEFORE = BOTH + (
    "DOT",
    "RIGHT_PARENTHESIS",
)

GROUP_SPACE_AFTER = BOTH + (
    "COMMA",
    "FROM",
)

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

        if current[0] in GROUP_SPACE_AFTER and iterator.show_next()[0] == "SPACE":
            _, space_value = iterator.next()
            current = (current[0], current[1], current[2] if len(current) > 2 else '', space_value)

        yield current
