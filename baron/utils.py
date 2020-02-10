import sys
import re


python_version = sys.version_info[0]
python_subversion = sys.version_info[1]
string_instance = str if python_version == 3 else basestring


class BaronError(Exception):
    pass


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
        if self.position + 1 >= len(self.sequence):
            return False
        return self.sequence[self.position + 1] in choice

    def show_next(self, at=1):
        if self.position + at >= len(self.sequence):
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


# Thanks to
# https://github.com/nvie/rq/commit/282f4be9316d608ebbacd6114aab1203591e8f95
if python_version >= 3 or python_subversion >= 7:
    from functools import total_ordering
else:
    def total_ordering(cls):
        """Class decorator that fills in missing ordering methods"""
        convert = {
            '__lt__': [('__gt__', lambda self, other: other < self),
                       ('__le__', lambda self, other: not other < self),
                       ('__ge__', lambda self, other: not self < other)],
            '__le__': [('__ge__', lambda self, other: other <= self),
                       ('__lt__', lambda self, other: not other <= self),
                       ('__gt__', lambda self, other: not self <= other)],
            '__gt__': [('__lt__', lambda self, other: other > self),
                       ('__ge__', lambda self, other: not other > self),
                       ('__le__', lambda self, other: not self > other)],
            '__ge__': [('__le__', lambda self, other: other >= self),
                       ('__gt__', lambda self, other: not other >= self),
                       ('__lt__', lambda self, other: not self >= other)]
        }
        roots = set(dir(cls)) & set(convert)
        if not roots:
            raise ValueError('must define at least one ordering operation: < > <= >=')  # noqa
        root = max(roots)       # prefer __lt__ to __le__ to __gt__ to __ge__
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = opname
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls
