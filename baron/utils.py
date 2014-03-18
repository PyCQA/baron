import ast


class PrintFunctionImportFinder(ast.NodeVisitor):
    def __init__(self, *args, **kwars):
        super(ast.NodeVisitor, self).__init__(*args, **kwars)
        self.print_function = False

    def visit_ImportFrom(self, node):
        if self.print_function:
            # my job is already done
            return

        if node.module == "__future__" and filter(lambda x: x.name == "print_function", node.names):
            self.print_function = True


class FlexibleIterator():
    def __init__(self, sequence):
        self.sequence = sequence
        self.position = -1

    def __iter__(self):
        return self

    def next(self):
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
            current = self.next()
            to_return += current

        return to_return

    def grab_string(self, test):
        to_return = ""
        current = None
        escaped = False
        while self.show_next() is not None and (escaped or test(self)):
            current = self.next()
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
