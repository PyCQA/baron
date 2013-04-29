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

    def show_next(self):
        if self.position + 1 == len(self.sequence):
            return None
        return self.sequence[self.position + 1]

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

def comparison(operator, first, second, first_space="", second_space="", middle_space=""):
    return {
        "type": "comparison",
        "value": operator,
        "first": first,
        "second": second,
        "first_space": first_space,
        "second_space": second_space,
        "middle_space": middle_space,
    }

def boolean_operator(operator, first, second, first_space="", second_space=""):
    return {
        "type": "boolean_operator",
        "value": operator,
        "first": first,
        "second": second,
        "first_space": first_space,
        "second_space": second_space,
    }

def binary_operator(operator, first, second, first_space="", second_space=""):
    return {
        "type": "binary_operator",
        "value": operator,
        "first": first,
        "second": second,
        "first_space": first_space,
        "second_space": second_space,
    }

def assignment(value, target, first_space="", second_space=""):
    return {
        "type": "assign",
        "value": value,
        "target": target,
        "first_space": first_space,
        "second_space": second_space,
    }

def augmented_assignment(operator, value, target, first_space="", second_space=""):
    return {
        "type": "assign",
        "operator": operator,
        "value": value,
        "target": target,
        "first_space": first_space,
        "second_space": second_space,
    }

def unitary_operator(operator, target, space=""):
    return {
        "type": "unitary_operator",
        "value": operator,
        "target": target,
        "space": space,
    }

def ternary_operator(test, first, second, first_space, second_space, third_space, forth_space):
    return {
        "type": "ternary_operator",
        "value": test,
        "first": first,
        "second": second,
        "first_space": first_space,
        "second_space": second_space,
        "third_space": third_space,
        "forth_space": forth_space,
    }

def tuple_(value, with_parenthesis):
    return {
        "type": "tuple",
        "value": value,
        "with_parenthesis": with_parenthesis,
    }

def yield_(value=None, space=""):
    return {
        "type": "yield",
        "value": value,
        "space": space,
    }

def return_(value=None, space=""):
    return {
        "type": "return",
        "value": value,
        "space": space,
    }
