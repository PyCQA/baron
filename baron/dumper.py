def debug(j):
    import json
    print json.dumps(j, indent=4)


def dump_node(node):
    return "".join(list(dumpers[node["type"]](node)))


def dump_node_list(node_list):
    return "".join(map(dump_node, node_list))


def get_value(node):
    yield node["value"]


def assignment(node):
    yield dump_node(node["target"])
    yield dump_node_list(node["first_formatting"])
    yield "="
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


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
