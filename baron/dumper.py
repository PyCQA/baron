def dump_node(node):
    return dumpers[node["type"]](node)


def dump_node_list(node_list):
    return "".join(map(dump_node, node_list))


def get_value(node):
    return node["value"]


def assignment(node):
    to_return = ""
    to_return += dump_node(node["target"])
    to_return += dump_node_list(node["first_formatting"])
    to_return += "="
    to_return += dump_node_list(node["second_formatting"])
    to_return += dump_node(node["value"])
    return to_return


dumpers = {
    "name": get_value,
    "endl": get_value,
    "int": get_value,
    "space": get_value,
    "assignment": assignment,
}


def dumps(tree):
    result = ""

    for node in tree:
        result += dump_node(node)

    return result
