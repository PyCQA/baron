import string
from utils import FlexibleIterator


def split(sequence):
    return list(split_generator(sequence))


def split_generator(sequence):
    iterator = FlexibleIterator(sequence)
    while True:
        if iterator.end():
            return

        not_found = True

        if iterator.next_in("#"):
            not_found = False
            result = iterator.grab(lambda iterator: (iterator.show_next() not in "\r\n"))
            yield result

        for section in ("'", '"'):
            if iterator.next_starts_with(section * 3):
                not_found = False
                result = iterator.next()
                result += iterator.next()
                result += iterator.next()
                result += iterator.grab_string(lambda iterator: not iterator.next_starts_with(section * 3))
                result += iterator.next()
                result += iterator.next()
                result += iterator.next()
                yield result
            elif iterator.next_in(section):
                not_found = False
                result = iterator.next()
                result += iterator.grab_string(lambda iterator: iterator.show_next() not in section)
                result += iterator.next()
                yield result

        for section in (string.ascii_letters + "_" + "1234567890", " \t"):
            if iterator.next_in(section):
                not_found = False
                yield iterator.grab(lambda iterator: iterator.show_next() in section)

        for one in "@,.;()=*:+-/^%&<>|\r\n~[]{}!``\\":
            if iterator.next_in(one):
                not_found = False
                yield iterator.next()

        if iterator.show_next().__repr__().startswith("'\\x"):
            # guys, seriously, how do you manage to put this shit in your code?
            # I mean, I don't even know how this is possible!
            # example of guitly file: ve/lib/python2.7/site-packages/tests/test_oauth.py
            # example of crapy unicode stuff found in some source files: \x0c\xef\xbb\xbf
            not_found = False
            # let's drop that crap
            iterator.next()

        if not_found:
            raise Exception("Untreaded elements: %s" % iterator.rest_of_the_sequence().__repr__()[:50])
