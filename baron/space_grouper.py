from utils import FlexibleIterator


def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    while True:
        if iterator.end():
            return

        current = iterator.next()

        if current[0] == "SPACE" and iterator.show_next()[0] in ("DOT", "AS", "IMPORT", "RIGHT_PARENTHESIS"):
            new_current = iterator.next()
            current = (new_current[0], new_current[1], current[1])

        if current[0] in ("IMPORT", "AS", "COMMA", "FROM", ) and iterator.show_next()[0] == "SPACE":
            _, space_value = iterator.next()
            current = (current[0], current[1], current[2] if len(current) > 2 else '', space_value)

        yield current
