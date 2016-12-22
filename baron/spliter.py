import string
from .utils import FlexibleIterator, BaronError


def split(sequence):
    return list(split_generator(sequence))


class UntreatedError(BaronError):
    pass


def split_generator(sequence):
    iterator = FlexibleIterator(sequence)

    # Pay attention that if a next() call fails, a StopIteration error
    # is raised. This coincidently is the same error used by python to
    # understand that a function using yield has finished processing.
    # It's not a bad thing, but it must be kept in mind.
    while not iterator.end():
        not_found = True

        if iterator.next_in("#"):
            not_found = False
            result = iterator.grab(lambda iterator: (iterator.show_next() not in "\r\n"))
            yield result

        for section in ("'", '"'):
            if iterator.next_starts_with(section * 3):
                not_found = False
                result = next(iterator)
                result += next(iterator)
                result += next(iterator)
                result += iterator.grab_string(lambda iterator: not iterator.next_starts_with(section * 3))
                # This next() call can fail if no closing quote exists. We
                # still want to yield so we catch it.
                try:
                    result += next(iterator)
                    result += next(iterator)
                    result += next(iterator)
                except StopIteration:
                    pass
                yield result
            elif iterator.next_in(section):
                not_found = False
                result = next(iterator)
                result += iterator.grab_string(lambda iterator: iterator.show_next() not in section)
                # This next() call can fail if no closing quote exists. We
                # still want to yield so we catch it.
                try:
                    result += next(iterator)
                except StopIteration:
                    pass
                yield result

        for section in (string.ascii_letters + "_" + "1234567890", " \t"):
            if iterator.next_in(section):
                not_found = False
                yield iterator.grab(lambda iterator: iterator.show_next() in section)

        for one in "@,.;()=*:+-/^%&<>|\r\n~[]{}!``\\":
            if iterator.next_in(one):
                not_found = False
                yield next(iterator)

        if iterator.show_next().__repr__().startswith("'\\x"):
            # guys, seriously, how do you manage to put this shit in your code?
            # I mean, I don't even know how this is possible!
            # example of guilty file: ve/lib/python2.7/site-packages/tests/test_oauth.py
            # example of crapy unicode stuff found in some source files: \x0c\xef\xbb\xbf
            not_found = False
            # let's drop that crap
            next(iterator)

        if not_found:
            raise UntreatedError("Untreated elements: %s" % iterator.rest_of_the_sequence().__repr__()[:50])
