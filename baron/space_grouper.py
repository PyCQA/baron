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
        if current[0] == "IMPORT" and iterator.show_next()[0] == "SPACE":
            _, space_value = iterator.next()
            current = (current[0], current[1], '', space_value)

        yield current
