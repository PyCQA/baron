import sys
import json


def render(node, strict=False):
    """Recipe to render a given FST node.

    The FST is composed of branch nodes which are either lists or dicts
    and of leaf nodes which are strings. Branch nodes can have other
    list, dict or leaf nodes as childs.

    To render a string, simply output it. To render a list, render each
    of its elements in order. To render a dict, you must follow the
    node's entry in the nodes_rendering_order dictionary and its
    dependents constraints.

    This function hides all this algorithmic complexity by returning
    a structured rendering recipe, whatever the type of node. But even
    better, you should subclass the RenderWalker which simplifies
    drastically working with the rendered FST.

    The recipe is a list of steps, each step correspond to a child and is actually a 3-uple composed of the following fields:

    - `key_type` is a string determining the type of the child in the second field (`item`) of the tuple. It can be one of:

      - 'constant': the child is a string
      - 'node': the child is a dict
      - 'key': the child is an element of a dict
      - 'list': the child is a list
      - 'formatting': the child is a list specialized in formatting

    - `item` is the child itself: either a string, a dict or a list.
    - `render_key` gives the key used to access this child from the parent node. It's a string if the node is a dict or a number if its a list.

    Please note that "bool" `key_types` are never rendered, that's why
    they are not shown here.
    """
    if isinstance(node, list):
        return render_list(node)

    elif isinstance(node, dict):
        return render_node(node, strict=strict)

    else:
        raise NotImplementedError("You tried to render a %s. Only list and dicts can be rendered." % node.__class__.__name__)


def render_list(node):
    for pos, child in enumerate(node):
        yield ('node', child, pos)


def render_node(node, strict=False):
    if node["type"] not in nodes_rendering_order:
        raise Exception("There are no defined rules for rendering a node of type '%s', has it been defined in render.py?" % node["type"])

    for key_type, render_key, dependent in nodes_rendering_order[node['type']]:
        if not dependent:
            continue
        elif key_type == "bool":
            raise NotImplementedError("Bool keys are only used for dependency, they cannot be rendered. Please set the \"%s\"'s dependent key in \"%s\" node to False" % ((key_type, render_key, dependent), node['type']))
        elif isinstance(dependent, str) and not node.get(dependent):
            continue
        elif isinstance(dependent, list) and not all([node.get(x) for x in dependent]):
            continue

        if strict:
            try:
                if key_type == "key":
                    assert isinstance(node[render_key], (dict, type(None))), "Key '%s' is expected to have type of 'key' (dict/None) but has type of '%s' instead" % (render_key, type(node[render_key]))
                elif key_type == "string":
                    assert isinstance(node[render_key], str), "Key '%s' is expected to have type of 'string' but has type of '%s' instead" % (render_key, type(node[render_key]))
                elif key_type in ("list", "formatting"):
                    assert isinstance(node[render_key], list), "Key '%s' is expected to have type of 'list' but has type of '%s' instead" % (render_key, type(node[render_key]))
                elif key_type == "constant":
                    pass
                else:
                    raise Exception("Invalid key_type '%s', should be one of those: key, string, list, formatting" % key_type)

                if dependent is True:
                    pass
                elif isinstance(dependent, str):
                    assert dependent in node
                elif isinstance(dependent, list):
                    assert all([x in node for x in dependent])
            except AssertionError as e:
                sys.stdout.write("Where node.type == '%s', render_key == '%s' and node ==\n%s\n" % (node["type"], render_key, json.dumps(node, indent=4, sort_keys=True)))
                raise e

        if key_type in ['key', 'string', 'list', 'formatting']:
            yield (key_type, node[render_key], render_key)
        elif key_type in ['constant', 'string']:
            yield (key_type, render_key, render_key)
        else:
            raise NotImplementedError("Unknown key type \"%s\" in \"%s\" node" % (key_type, node['type']))


node_types = set(['node', 'list', 'key', 'formatting', 'constant', 'bool', 'string'])


def node_keys(node):
    return [key for (_, key, _) in nodes_rendering_order[node['type']]]


def child_by_key(node, key):
    if isinstance(node, list):
        return node[key]

    if key in node:
        return node[key]

    if key in node_keys(node):
        return key

    raise AttributeError("Cannot access key \"%s\" in node \"%s\"" % (key, node))


# for a surprising exception, we won't honnor pep8 here because it really increase lisibility
nodes_rendering_order = {
    "int":                       [("string", "value", True)],  # noqa
    "long":                      [("string", "value", True)],  # noqa
    "name":                      [("string", "value", True)],  # noqa
    "hexa":                      [("string", "value", True)],  # noqa
    "octa":                      [("string", "value", True)],  # noqa
    "float":                     [("string", "value", True)],  # noqa
    "space":                     [("string", "value", True)],  # noqa
    "binary":                    [("string", "value", True)],  # noqa
    "complex":                   [("string", "value", True)],  # noqa
    "float_exponant":            [("string", "value", True)],  # noqa
    "left_parenthesis":          [("string", "value", True)],  # noqa
    "right_parenthesis":         [("string", "value", True)],  # noqa
    "float_exponant_complex":    [("string", "value", True)],  # noqa

    "break":                     [("string", "type", True)],  # noqa
    "continue":                  [("string", "type", True)],  # noqa
    "pass":                      [("string", "type", True)],  # noqa

    "dotted_name":               [("list", "value", True)],  # noqa
    "ifelseblock":               [("list", "value", True)],  # noqa
    "atomtrailers":              [("list", "value", True)],  # noqa
    "string_chain":              [("list", "value", True)],  # noqa

    "endl": [
        ("formatting", "formatting",        True),  # noqa
        ("string",     "value",             True),  # noqa
        ("string",     "indent",            True),  # noqa
    ],

    "star": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],

    "star_expression": [
        ("constant",   "*",                 True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "raw_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "binary_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "unicode_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "binary_raw_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "interpolated_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "interpolated_raw_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],
    "unicode_raw_string": [
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],

    # FIXME ugly, comment can end up in formatting of another
    # node or being standalone, this is bad
    "comment": [
        ("formatting", "formatting", "formatting"),  # noqa
        ("string",     "value",             True),  # noqa
    ],

    "ternary_operator": [
        ("key",        "first",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "if",                True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "else",              True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("key",        "second",            True),  # noqa
    ],

    "ellipsis": [
        ("constant",   ".",                 True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ".",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ".",                 True),  # noqa
    ],

    "dot": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ".",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],

    "semicolon": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ";",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],

    "comma": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ",",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
    ],

    "call": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "(",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   ")",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "decorator": [
        ("constant",   "@",                 True),  # noqa
        ("key",        "value",             True),  # noqa
        ("key",        "call",              "call"),  # noqa
    ],

    "class": [
        ("list",       "decorators",        True),  # noqa
        ("constant",   "class",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "name",              True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   "(",                 "parenthesis"),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "inherit_from",      True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("constant",   ")",                 "parenthesis"),  # noqa
        ("formatting", "fifth_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "sixth_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
        ("bool",       "parenthesis",       False),  # noqa
    ],

    "repr": [
        ("constant",   "`",                 True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   "`",                 True),  # noqa
    ],

    "list": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "[",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "]",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "associative_parenthesis": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "(",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   ")",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "tuple": [
        ("formatting", "first_formatting",  "with_parenthesis"),  # noqa
        ("constant",   "(",                 "with_parenthesis"),  # noqa
        ("formatting", "second_formatting", "with_parenthesis"),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "third_formatting",  "with_parenthesis"),  # noqa
        ("constant",   ")",                 "with_parenthesis"),  # noqa
        ("formatting", "fourth_formatting", "with_parenthesis"),  # noqa
        ("bool",       "with_parenthesis",  False),  # noqa
    ],

    "await": [
        ("constant",    "await",        True),  # noqa
        ("formatting",  "formatting",   True),  # noqa
        ("key",         "value",        True),  # noqa
    ],

    "def": [
        ("list",       "decorators",        True),  # noqa
        ("bool",       "async",             False),  # noqa
        ("constant",   "async",             "async"),  # noqa
        ("formatting", "async_formatting",  "async"),  # noqa
        ("constant",   "def",               True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "name",              True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   "(",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "arguments",         True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("constant",   ")",                 True),  # noqa
        ("formatting", "return_annotation_first_formatting", "return_annotation"),  # noqa
        ("constant",   "->", "return_annotation"),  # noqa
        ("formatting", "return_annotation_second_formatting", "return_annotation"),  # noqa
        ("key",        "return_annotation", "return_annotation"),  # noqa
        ("formatting", "fifth_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "sixth_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "call_argument": [
        ("key",        "target",            "target"),  # noqa
        ("formatting", "first_formatting",  "target"),  # noqa
        ("constant",   "=",                 "target"),  # noqa
        ("formatting", "second_formatting", "target"),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "def_argument": [
        ("key",        "target",            True),  # noqa
        ("formatting", "annotation_first_formatting", "annotation"),  # noqa
        ("constant",   ":",                 "annotation"),  # noqa
        ("formatting", "annotation_second_formatting", "annotation"),  # noqa
        ("key",        "annotation",        "annotation"),  # noqa
        ("formatting", "first_formatting",  "value"),  # noqa
        ("constant",   "=",                 "value"),  # noqa
        ("formatting", "second_formatting", "value"),  # noqa
        ("key",        "value",             "value"),  # noqa
    ],

    "list_argument": [
        ("constant",   "*",                 True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "annotation_first_formatting", "annotation"),  # noqa
        ("constant",   ":",                 "annotation"),  # noqa
        ("formatting", "annotation_second_formatting", "annotation"),  # noqa
        ("key",        "annotation",        "annotation"),  # noqa
    ],

    "kwargs_only_marker": [
        ("constant",   "*",                 True),  # noqa
        ("formatting", "formatting",        True),  # noqa
    ],

    "dict_argument": [
        ("constant",   "**",                True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "annotation_first_formatting", "annotation"),  # noqa
        ("constant",   ":",                 "annotation"),  # noqa
        ("formatting", "annotation_second_formatting", "annotation"),  # noqa
        ("key",        "annotation",        "annotation"),  # noqa
    ],

    "return": [
        ("constant",   "return",            True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             "value"),  # noqa
    ],

    "raise": [
        ("constant",   "raise",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "value",             "value"),  # noqa
        ("formatting", "second_formatting", "instance"),  # noqa
        ("string",     "comma_or_from",     "instance"),  # noqa
        ("formatting", "third_formatting",  "instance"),  # noqa
        ("key",        "instance",          "instance"),  # noqa
        ("formatting", "fourth_formatting", "traceback"),  # noqa
        ("constant",   ",",                 "traceback"),  # noqa
        ("formatting", "fifth_formatting",  "traceback"),  # noqa
        ("key",        "traceback",         "traceback"),  # noqa
    ],

    "assert": [
        ("constant",   "assert",            True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "second_formatting", "message"),  # noqa
        ("constant",   ",",                 "message"),  # noqa
        ("formatting", "third_formatting",  "message"),  # noqa
        ("key",        "message",           "message"),  # noqa
    ],

    "set_comprehension": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "{",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "result",            True),  # noqa
        ("list",       "generators",        True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "}",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "dict_comprehension": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "{",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "result",            True),  # noqa
        ("list",       "generators",        True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "}",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "argument_generator_comprehension": [
        ("key",  "result",                  True),  # noqa
        ("list", "generators",              True),  # noqa
    ],

    "generator_comprehension": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "(",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "result",            True),  # noqa
        ("list",       "generators",        True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   ")",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "list_comprehension": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "[",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "result",            True),  # noqa
        ("list",       "generators",        True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "]",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "comprehension_loop": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "for",               True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "iterator",          True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "in",                True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("key",        "target",            True),  # noqa
        ("list",       "ifs",               True),  # noqa
    ],

    "comprehension_if": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "if",                True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "getitem": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "[",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "]",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "slice": [
        ("key",        "lower",             "lower"),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "upper",             "upper"),  # noqa
        ("formatting", "third_formatting",  "has_two_colons"),  # noqa
        ("constant",   ":",                 "has_two_colons"),  # noqa
        ("formatting", "fourth_formatting", "has_two_colons"),  # noqa
        ("key",        "step",              ["has_two_colons", "step"]),  # noqa
        ("bool",       "has_two_colons",    False),  # noqa
    ],

    "assignment": [
        ("key",        "target",            True),  # noqa
        ("formatting", "annotation_first_formatting",  "annotation"),  # noqa
        ("constant",   ":",                 "annotation"),  # noqa
        ("formatting", "annotation_second_formatting",  "annotation"),  # noqa
        ("key",        "annotation",        "annotation"),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        # FIXME should probably be a different node type  # noqa
        ("string",     "operator",          "operator"),  # noqa
        ("constant",   "=",                 "target"),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "standalone_annotation": [
        ("key",        "target",            True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "annotation",        True),  # noqa
    ],

    "unitary_operator": [
        ("string",     "value",             True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "target",            True),  # noqa
    ],

    "binary_operator": [
        ("key",        "first",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "second",            True),  # noqa
    ],

    "boolean_operator": [
        ("key",        "first",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("string",     "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "second",            True),  # noqa
    ],

    "comparison_operator": [
        ("string",     "first",             True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("string",     "second",            "second"),  # noqa
    ],

    "comparison": [
        ("key",        "first",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "second",            True),  # noqa
    ],

    "with": [
        ("bool",       "async",             False),  # noqa
        ("constant",   "async",             "async"),  # noqa
        ("formatting", "async_formatting",  "async"),  # noqa
        ("constant",   "with",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("list",       "contexts",          True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "with_context_item": [
        ("key",        "value",             True),  # noqa
        ("formatting", "first_formatting",  "as"),  # noqa
        ("constant",   "as",                "as"),  # noqa
        ("formatting", "second_formatting", "as"),  # noqa
        ("key",        "as",                "as"),  # noqa
    ],

    "nonlocal": [
        ("constant",    "nonlocal",         True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("list",        "value",            True),  # noqa
    ],

    "del": [
        ("constant",   "del",               True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "yield": [
        ("constant",   "yield",             True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("key",        "value",             "value"),  # noqa
    ],

    "yield_from": [
        ("constant",   "yield",             True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("constant",   "from",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "value",             "value"),  # noqa
    ],

    "yield_atom": [
        ("constant",   "(",                 True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "yield",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             "value"),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   ")",                 True),  # noqa
    ],

    "exec": [
        ("constant",   "exec",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "value",             True),  # noqa
        ("formatting", "second_formatting", "globals"),  # noqa
        ("constant",   "in",                "globals"),  # noqa
        ("formatting", "third_formatting",  "globals"),  # noqa
        ("key",        "globals",           "globals"),  # noqa
        ("formatting", "fourth_formatting", "locals"),  # noqa
        ("constant",   ",",                 "locals"),  # noqa
        ("formatting", "fifth_formatting",  "locals"),  # noqa
        ("key",        "locals",            "locals"),  # noqa
    ],

    "global": [
        ("constant",   "global",            True),  # noqa
        ("formatting", "formatting",        True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "while": [
        ("constant",   "while",             True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "test",              True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
        ("key",        "else",              "else"),  # noqa
    ],

    "for": [
        ("bool",       "async",             False),  # noqa
        ("constant",   "async",             "async"),  # noqa
        ("formatting", "async_formatting",  "async"),  # noqa
        ("constant",   "for",               True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "iterator",          True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   "in",                True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("key",        "target",            True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "fifth_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
        ("key",        "else",              "else"),  # noqa
    ],

    "if": [
        ("constant",   "if",                True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "test",              True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "elif": [
        ("constant",   "elif",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "test",              True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "else": [
        ("constant",   "else",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "lambda": [
        ("constant",   "lambda",            True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("list",       "arguments",         True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "try": [
        ("constant",   "try",               True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
        ("list",       "excepts",           True),  # noqa
        ("key",        "else",              "else"),  # noqa
        ("key",        "finally",           "finally"),  # noqa
    ],

    "except": [
        ("constant",   "except",            True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("key",        "exception",         "exception"),  # noqa
        ("formatting", "second_formatting", "delimiter"),  # noqa
        ("string",     "delimiter",         "delimiter"),  # noqa
        ("formatting", "third_formatting",  "delimiter"),  # noqa
        ("key",        "target",            "delimiter"),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "fifth_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "finally": [
        ("constant",   "finally",           True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "dict": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "{",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "}",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "set": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "{",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("constant",   "}",                 True),  # noqa
        ("formatting", "fourth_formatting", True),  # noqa
    ],

    "dictitem": [
        ("key",        "key",               True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   ":",                 True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("key",        "value",             True),  # noqa
    ],

    "import": [
        ("formatting", "first_formatting",  True),  # noqa
        ("constant",   "import",            True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("list",       "value",             True),  # noqa
    ],

    "from_import": [
        ("constant",   "from",              True),  # noqa
        ("formatting", "first_formatting",  True),  # noqa
        ("list",       "value",             True),  # noqa
        ("formatting", "second_formatting", True),  # noqa
        ("constant",   "import",            True),  # noqa
        ("formatting", "third_formatting",  True),  # noqa
        ("list",       "targets",           True),  # noqa
    ],

    "dotted_as_name": [
        ("list",       "value",             True),  # noqa
        ("formatting", "first_formatting",  "target"),  # noqa
        ("constant",   "as",                "target"),  # noqa
        ("formatting", "second_formatting", "target"),  # noqa
        ("string",     "target",            "target"),  # noqa
    ],

    "name_as_name": [
        ("string",     "value",             True),  # noqa
        ("formatting", "first_formatting",  "target"),  # noqa
        ("constant",   "as",                "target"),  # noqa
        ("formatting", "second_formatting", "target"),  # noqa
        ("string",     "target",            "target"),  # noqa
    ],

    "print": [
        ("constant",   "print",                  True),  # noqa
        ("formatting", "formatting",             True),  # noqa
        ("constant",   ">>",                     "destination"),  # noqa
        ("formatting", "destination_formatting", "destination"),  # noqa
        ("key",        "destination",            "destination"),  # noqa
        ("list",       "value",                  "value"),  # noqa
    ],
}


class RenderWalker(object):
    """Inherit me and overload the methods you want.

    When calling walk() on a FST node, this class will traverse all the
    node's subtree by following the recipe given by the `render`
    function for the node and recursively for all its childs. At each
    recipe step, it will call methods that you can override to make a
    specific process.

    For every "node", "key", "list", "formatting" and "constant" childs,
    it will call the `before` method when going down the tree and the
    `after` method when going up. There are also specific
    `before_[node,key,list,formatting,constant]` and
    `after_[node,key,list,formatting,constant]` methods provided for
    convenience.

    The latter are called on specific steps:

    * before_list: called before encountering a list of nodes
    * after_list: called after encountering a list of nodes
    * before_formatting: called before encountering a formatting list
    * after_formatting: called after encountering a formatting list
    * before_node: called before encountering a node
    * after_node: called after encountering a node
    * before_key: called before encountering a key type entry
    * after_key: called after encountering a key type entry
    * before_leaf: called before encountering a leaf of the FST (can be a constant (like "def" in a function definition) or an actual value like the value a name node)
    * after_leaf: called after encountering a leaf of the FST (can be a constant (like "def" in a function definition) or an actual value like the value a name node)

    Every method has the same signature: (self, node, render_pos, render_key).
    """
    STOP = True

    def __init__(self, strict=False):
        self.strict = strict

    def before_list(self, node, render_key):
        pass

    def after_list(self, node, render_key):
        pass

    def before_formatting(self, node, render_key):
        pass

    def after_formatting(self, node, render_key):
        pass

    def before_node(self, node, render_key):
        pass

    def after_node(self, node, render_key):
        pass

    def before_key(self, node, render_key):
        pass

    def after_key(self, node, render_key):
        pass

    def before_constant(self, node, render_key):
        pass

    def after_constant(self, node, render_key):
        pass

    def before_string(self, node, render_key):
        pass

    def after_string(self, node, render_key):
        pass

    def before(self, key_type, item, render_key):
        if key_type not in node_types:
            raise NotImplementedError("Unknown key type: %s" % key_type)

        to_call = getattr(self, 'before_' + key_type)

        return to_call(item, render_key)

    def after(self, key_type, item, render_key):
        if key_type not in node_types:
            raise NotImplementedError("Unknown key type: %s" % key_type)

        to_call = getattr(self, 'after_' + key_type)

        return to_call(item, render_key)

    def walk(self, node):
        return self._walk(node)

    def _walk(self, node):
        for key_type, item, render_key in render(node, strict=getattr(self, "strict", False)):
            stop = self._walk_on_item(key_type, item, render_key)
            if stop == self.STOP:
                return self.STOP

    def _walk_on_item(self, key_type, item, render_key):
        stop_before = self.before(key_type, item, render_key)
        if stop_before:
            return self.STOP

        stop = self._walk(item) if key_type not in ['constant', 'string'] else False

        stop_after = self.after(key_type, item, render_key)

        if stop or stop_after:
            return self.STOP
