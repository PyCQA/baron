from .utils import FlexibleIterator
import sys

"""
Objective: add an INDENT token and a DEDENT token arround every block.

Strategy: put after every ":" that is not in a slice/dictionary declaration/lambda.

Slice and dictionary are easy: increase a number when a "[" or "{" is found,
decrease it for a "]" or "}". If the number is != 0, we are in a dictionary or
slice -> do not put a INDENT when a ":" is found.

Lambda are a bit different: increase another number when a "lambda" is found,
if the number is != 0 and a ":" is found, decrease this number, otherwise put a
INDENT.

For the DEDENT, I'm probably going to need to keep a list of indentation and
decheck the last one every time I encounter a meaningfull line. Still need to
test this idea.
"""


def mark_indentation(sequence):
    return list(mark_indentation_generator(sequence))


def transform_tabs_to_spaces(string):
    return string.replace("\t", " "*8)


def get_space(node):
    """ Return space formatting information of node.

    If the node does not have a third formatting item - like in
    a ('ENDL', '\n') node - then we return None as a flag value. This is
    maybe not the best behavior but it seems to work for now.
    """
    if len(node) < 3 or len(node[3]) == 0:
        return None
    return transform_tabs_to_spaces(node[3][0][1])


def mark_indentation_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    indentations = []
    while True:
        if iterator.end():
            return

        current = next(iterator)

        if current is None:
            return

        # end of the file, I need to pop all indentations left and put the
        # corresponding dedent token for them
        if current[0] == "ENDMARKER" and indentations:
            while len(indentations) > 0:
                yield ('DEDENT', '')
                indentations.pop()

        # if were are at ":\n" like in "if stuff:\n"
        if current[0] == "COLON" and iterator.show_next(1)[0] == "ENDL":
            # if we aren't in "if stuff:\n\n"
            if iterator.show_next(2)[0] not in ("ENDL",):
                indentations.append(get_space(iterator.show_next()))
                yield current
                yield next(iterator)
                yield ('INDENT', '')
                continue
            else:  # else, skip all "\n"
                yield current
                for i in iterator:
                    if i[0] == 'ENDL' and iterator.show_next()[0] not in ('ENDL',):
                        indentations.append(get_space(i))
                        yield ('INDENT', '')
                        yield i
                        break
                    yield i
                continue

        # if we were in an indented situation and that the next line has a lower indentation
        if indentations and current[0] == "ENDL":
            the_indentation_level_changed = get_space(current) is None or get_space(current) != indentations[-1]
            if the_indentation_level_changed and iterator.show_next()[0] not in ("ENDL", "COMMENT"):
                new_indent = get_space(current) if len(current) == 4 else ""
                yield current

                # pop until reaching the matching indentation level
                while indentations and string_is_bigger(indentations[-1], new_indent):
                    indentations.pop()
                    yield ('DEDENT', '')
                yield next(iterator)
                continue

        yield current


def string_is_bigger(s1, s2):
    """ Return s1 > s2 by taking into account None values.

    None is always smaller than any string.

    None > "string" works in python2 but not in python3. This function
    makes it work in python3 too.
    """
    if s1 is None:
        return False
    elif s2 is None:
        return True
    else:
        return s1 > s2

