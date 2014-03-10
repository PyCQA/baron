def dump_node(node):
    return dumpers[node["type"]](node)


def get_value(node):
    return node["value"]


dumpers = {
    "name": get_value,
    "endl": get_value,
    "int": get_value,
}


def dumps(tree):
    result = ""

    for node in tree:
        result += dump_node(node)

    return result
