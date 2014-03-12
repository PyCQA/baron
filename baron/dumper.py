def debug(j):
    import json
    print json.dumps(j, indent=4)


dumpers = {}


def node(key=""):
    def wrap(func):
        if not key:
            dumpers[func.__name__ if not func.__name__.endswith("_") else func.__name__[:-1]] = func

        dumpers[key] = func
        return func
    return wrap


def dump_node(node):
    return "".join(list(dumpers[node["type"]](node)))


def dump_node_list(node_list):
    return "".join(map(dump_node, node_list))


@node()
def endl(node):
    yield dump_node_list(node["formatting"])
    yield node["value"]
    yield node["indent"]


@node("int")
@node("name")
@node("space")
@node("string")
@node("raw_string")
@node("binary_string")
@node("unicode_string")
@node("binary_raw_string")
@node("unicode_raw_string")
def get_value(node):
    yield node["value"]


@node()
def dot(node):
    yield dump_node_list(node["first_formatting"])
    yield "."
    yield dump_node_list(node["second_formatting"])


@node()
def comma(node):
    yield dump_node_list(node["first_formatting"])
    yield ","
    yield dump_node_list(node["second_formatting"])


@node()
def call(node):
    yield dump_node_list(node["first_formatting"])
    yield "("
    yield dump_node_list(node["second_formatting"])
    for n in node["value"]:
        if n["type"] == "argument":
            yield "".join(list(call_argument(n)))
        else:
            yield dump_node(n)
    yield ")"
    yield dump_node_list(node["third_formatting"])


@node()
def funcdef(node):
    yield "def"
    yield dump_node_list(node["first_formatting"])
    yield node["name"]
    yield dump_node_list(node["second_formatting"])
    yield "("
    yield dump_node_list(node["third_formatting"])
    for n in node["arguments"]:
        if n["type"] == "argument":
            yield "".join(list(funcdef_argument(n)))
        else:
            yield dump_node(n)
    yield dump_node_list(node["forth_formatting"])
    yield ")"
    yield dump_node_list(node["fith_formatting"])
    yield ":"
    yield dump_node_list(node["sixth_formatting"])
    yield dump_node_list(node["value"])


def call_argument(node):
    if node["name"]:
        yield node["name"]
        yield dump_node_list(node["first_formatting"])
        yield "="
        yield dump_node_list(node["second_formatting"])
        yield dump_node(node["value"])
    else:
        yield dump_node(node["value"])


def funcdef_argument(node):
    if node["value"]:
        yield node["name"]
        yield dump_node_list(node["first_formatting"])
        yield "="
        yield dump_node_list(node["second_formatting"])
        yield dump_node(node["value"])
    else:
        yield node["name"]


@node()
def pass_(node):
    yield "pass"


@node()
def return_(node):
    yield "return"
    yield dump_node_list(node["formatting"])
    yield dump_node(node["value"])


@node("dotted_name")
@node("ifelseblock")
@node("atomtrailers")
def dump_node_list_value(node):
    yield dump_node_list(node["value"])


@node()
def getitem(node):
    yield "["
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["second_formatting"])
    yield "]"


@node()
def slice(node):
    if node["lower"]:
        yield dump_node(node["lower"])
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    if node["upper"]:
        yield dump_node(node["upper"])

    if node["has_two_colons"]:
        yield dump_node_list(node["third_formatting"])
        yield ":"
        yield dump_node_list(node["forth_formatting"])
        if node["step"]:
            yield dump_node(node["step"])


@node()
def assignment(node):
    yield dump_node(node["target"])
    yield dump_node_list(node["first_formatting"])
    yield "="
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


@node()
def unitary_operator(node):
    yield node["value"]
    yield dump_node_list(node["formatting"])
    yield dump_node(node["target"])


@node()
def binary_operator(node):
    yield dump_node(node["first"])
    yield dump_node_list(node["first_formatting"])
    yield node["value"]
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["second"])


@node()
def while_(node):
    yield "while"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["test"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])
    if node["else"]:
        yield dump_node(node["else"])


@node()
def if_(node):
    yield "if"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["test"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])


@node()
def elif_(node):
    yield "elif"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["test"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])


@node()
def else_(node):
    yield "else"
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])


@node()
def import_(node):
    yield "import"
    yield dump_node_list(node["formatting"])
    yield dump_node_list(node["value"])


@node()
def from_import(node):
    yield "from"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["second_formatting"])
    yield "import"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["targets"])


@node()
def dotted_as_name(node):
    yield dump_node_list(node["value"]["value"])
    if node["as"]:
        yield dump_node_list(node["first_formatting"])
        yield "as"
        yield dump_node_list(node["second_formatting"])
        yield node["target"]


@node()
def name_as_name(node):
    yield node["value"]
    if node["as"]:
        yield dump_node_list(node["first_formatting"])
        yield "as"
        yield dump_node_list(node["second_formatting"])
        yield node["target"]


@node()
def print_(node):
    yield "print"
    yield dump_node_list(node["formatting"])
    if node["destination"]:
        yield ">>"
        yield dump_node_list(node["destination_formatting"])
        yield dump_node(node["destination"])
    yield dump_node_list(node["value"])


def dumps(tree):
    return "".join(map(dump_node, tree))
