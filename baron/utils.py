import sys
import re


python_version = sys.version_info[0]
string_instance = str if python_version == 3 else basestring


class FlexibleIterator():
    def __init__(self, sequence):
        self.sequence = sequence
        self.position = -1

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        self.position += 1
        if self.position == len(self.sequence):
            raise StopIteration
        return self.sequence[self.position]

    def next_starts_with(self, sentence):
        size_of_choice = len(sentence)
        return self.sequence[self.position + 1: self.position + 1 + size_of_choice] == sentence

    def next_in(self, choice):
        if self.position + 1 == len(self.sequence):
            return False
        return self.sequence[self.position + 1] in choice

    def show_next(self, at=1):
        if self.position + at == len(self.sequence):
            return None
        return self.sequence[self.position + at]

    def rest_of_the_sequence(self):
        return self.sequence[self.position + 1:]

    def end(self):
        return self.position == (len(self.sequence) - 1)

    def grab(self, test):
        to_return = ""
        current = None
        while self.show_next() is not None and test(self):
            current = next(self)
            to_return += current

        return to_return

    def grab_string(self, test):
        to_return = ""
        current = None
        escaped = False
        while self.show_next() is not None and (escaped or test(self)):
            current = next(self)
            to_return += current
            if escaped:
                escaped = False
            elif current == "\\":
                escaped = True

        return to_return


def create_node_from_token(token, **kwargs):
    result = {"type": token.name.lower(), "value": token.value}
    if kwargs:
        result.update(kwargs)
    return result


def create_node(name, value, **kwargs):
    result = {"type": name, "value": value}
    if kwargs:
        result.update(kwargs)
    return result


newline_regex = re.compile("(\r\n|\n|\r)")


def is_newline(text):
    return newline_regex.match(text)


def split_on_newlines(text):
    newlines = newline_regex.finditer(text)
    if not newlines:
        yield text
    else:
        current_position = 0
        for newline in newlines:
            yield text[current_position:newline.start(1)]
            yield text[newline.start(1):newline.end(1)]
            current_position = newline.end(1)
        yield text[current_position:]

