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
        result += dumpers[node["type"]](node)

    return result
