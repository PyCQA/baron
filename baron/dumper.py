def debug(j):
    import json
    print json.dumps(j, indent=4)


def dump_node(node):
    return "".join(list(dumpers[node["type"]](node)))


def dump_node_list(node_list):
    return "".join(map(dump_node, node_list))


def endl(node):
    yield dump_node_list(node["formatting"])
    yield node["value"]
    yield node["indent"]


def get_value(node):
    yield node["value"]


def dump_node_list_value(node):
    yield dump_node_list(node["value"])


def assignment(node):
    yield dump_node(node["target"])
    yield dump_node_list(node["first_formatting"])
    yield "="
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


def binary_operator(node):
    yield dump_node(node["first"])
    yield dump_node_list(node["first_formatting"])
    yield node["value"]
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["second"])


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


def if_(node):
    yield "if"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["test"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])


def elif_(node):
    yield "elif"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["test"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])


def else_(node):
    yield "else"
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])


def import_(node):
    yield "import"
    yield dump_node_list(node["formatting"])
    yield dump_node_list(node["value"])


def from_import(node):
    yield "from"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["second_formatting"])
    yield "import"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["targets"])


def dotted_as_name(node):
    yield dump_node_list(node["value"]["value"])
    if node["as"]:
        yield dump_node_list(node["first_formatting"])
        yield "as"
        yield dump_node_list(node["second_formatting"])
        yield node["target"]


def name_as_name(node):
    yield node["value"]
    if node["as"]:
        yield dump_node_list(node["first_formatting"])
        yield "as"
        yield dump_node_list(node["second_formatting"])
        yield node["target"]
    debug(node)


dumpers = {
    "name": get_value,
    "dot": get_value,
    "endl": endl,
    "int": get_value,
    "pass": lambda x: "pass",
    "space": get_value,
    "assignment": assignment,
    "binary_operator": binary_operator,
    "while": while_,
    "ifelseblock": dump_node_list_value,
    "if": if_,
    "elif": elif_,
    "else": else_,
    "import": import_,
    "from_import": from_import,
    "dotted_as_name": dotted_as_name,
    "dotted_name": dump_node_list_value,
    "name_as_name": name_as_name,
}


def dumps(tree):
    result = ""

    for node in tree:
        result += dump_node(node)

    return result
