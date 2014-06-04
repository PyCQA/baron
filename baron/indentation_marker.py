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


def get_space(node):
    if len(node) < 3:
        sys.stdout.write("WARNING")
        return None
    if len(node[3]) == 0:
        sys.stdout.write("WARNING")
        return None
    return node[3][0][1].replace("	", " "*8)


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

        if current[0] == "ENDMARKER" and indentations:
            while len(indentations) > 0:
                yield ('DEDENT', '')
                indentations.pop()

        #sys.stdout.write(current, iterator.show_next())
        if current[0] == "COLON" and iterator.show_next()[0] == "ENDL":
            if iterator.show_next(2)[0] not in ("ENDL",):
                indentations.append(get_space(iterator.show_next()))
                yield current
                yield next(iterator)
                yield ('INDENT', '')
                continue
            else:
                yield current
                for i in iterator:
                    if i[0] == 'ENDL' and iterator.show_next()[0] not in ('ENDL',):
                        indentations.append(get_space(i))
                        yield ('INDENT', '')
                        yield i
                        break
                    yield i
                continue

        if indentations and current[0] == "ENDL" and (len(current) != 4 or get_space(current) != indentations[-1]) and iterator.show_next()[0] != "ENDL":
            new_indent = get_space(current) if len(current) == 4 else ""
            yield current
            while indentations and indentations[-1] > new_indent:
                indentations.pop()
                yield ('DEDENT', '')
            yield next(iterator)
            continue

        yield current
