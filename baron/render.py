import sys


def render(node, strict=False):
    """Recipe to render a given FST node.

    The FST is composed of branch nodes which are either lists or dicts
    and of leaf nodes which are strings. Branch nodes can have other
    list, dict or leaf nodes as childs.

    To render a string, simply output it. To render a list, render each
    of its elements in order. To render a dict, you must follow the
    node's entry in the nodes_rendering_order dictionnary and its
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
                    assert isinstance(node[render_key], (dict, type(None)))
                elif key_type == "string":
                    assert isinstance(node[render_key], str)
                elif key_type in ("list", "formatting"):
                    assert isinstance(node[render_key], list)
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
                sys.stdout.write("Where node.type == '%s', render_key == '%s' and node == %s\n" % (node["type"], render_key, node))
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


nodes_rendering_order = {
        "int":               [("string", "value", True)],
        "long":              [("string", "value", True)],
        "name":              [("string", "value", True)],
        "hexa":              [("string", "value", True)],
        "octa":              [("string", "value", True)],
        "float":             [("string", "value", True)],
        "space":             [("string", "value", True)],
        "binary":            [("string", "value", True)],
        "complex":           [("string", "value", True)],
        "float_exponant":    [("string", "value", True)],
        "left_parenthesis":  [("string", "value", True)],
        "right_parenthesis": [("string", "value", True)],
        "float_exponant_complex":    [("string", "value", True)],

        "break":             [("string", "type", True)],
        "continue":          [("string", "type", True)],
        "pass":              [("string", "type", True)],

        "dotted_name":       [("list", "value", True)],
        "ifelseblock":       [("list", "value", True)],
        "atomtrailers":      [("list", "value", True)],
        "string_chain":      [("list", "value", True)],

        "endl": [
            ("formatting", "formatting",        True),
            ("string",     "value",             True),
            ("string",     "indent",            True),
        ],

        "star": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "raw_string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "binary_string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "unicode_string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "binary_raw_string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "unicode_raw_string": [
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
        ],

        # FIXME ugly, comment can end up in formatting of another
        # node or being standalone, this is bad
        "comment": [
            ("formatting", "formatting", "formatting"),
            ("string",     "value",             True),
        ],

        "ternary_operator": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("constant",   "if",                True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   "else",              True),
            ("formatting", "fourth_formatting", True),
            ("key",        "second",            True),
        ],

        "ellipsis": [
            ("constant",   ".",                 True),
            ("formatting", "first_formatting",  True),
            ("constant",   ".",                 True),
            ("formatting", "second_formatting", True),
            ("constant",   ".",                 True),
        ],
        "dot": [
            ("formatting", "first_formatting",  True),
            ("constant",   ".",                 True),
            ("formatting", "second_formatting", True),
        ],
        "semicolon": [
            ("formatting", "first_formatting",  True),
            ("constant",   ";",                 True),
            ("formatting", "second_formatting", True),
        ],
        "comma": [
            ("formatting", "first_formatting",  True),
            ("constant",   ",",                 True),
            ("formatting", "second_formatting", True),
        ],

        "call": [
            ("formatting", "first_formatting",  True),
            ("constant",   "(",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   ")",                 True),
            ("formatting", "fourth_formatting", True),
        ],

        "decorator": [
            ("constant",   "@",                 True),
            ("key",        "value",             True),
            ("key",        "call",              "call"),
        ],

        "class": [
            ("list",       "decorators",        True),
            ("constant",   "class",             True),
            ("formatting", "first_formatting",  True),
            ("string",     "name",              True),
            ("formatting", "second_formatting", True),
            ("constant",   "(",                 "parenthesis"),
            ("formatting", "third_formatting",  True),
            ("list",       "inherit_from",      True),
            ("formatting", "fourth_formatting", True),
            ("constant",   ")",                 "parenthesis"),
            ("formatting", "fifth_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "sixth_formatting",  True),
            ("list",       "value",             True),
            ("bool",       "parenthesis",       False),
        ],

        "repr": [
            ("constant",   "`",                 True),
            ("formatting", "first_formatting",  True),
            ("list",       "value",             True),
            ("formatting", "second_formatting", True),
            ("constant",   "`",                 True),
        ],
        "list": [
            ("formatting", "first_formatting",  True),
            ("constant",   "[",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   "]",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "associative_parenthesis": [
            ("formatting", "first_formatting",  True),
            ("constant",   "(",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   ")",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "tuple": [
            ("formatting", "first_formatting",  "with_parenthesis"),
            ("constant",   "(",                 "with_parenthesis"),
            ("formatting", "second_formatting", "with_parenthesis"),
            ("list",       "value",             True),
            ("formatting", "third_formatting",  "with_parenthesis"),
            ("constant",   ")",                 "with_parenthesis"),
            ("formatting", "fourth_formatting", "with_parenthesis"),
            ("bool",       "with_parenthesis",  False),
        ],

        "def": [
            ("list",       "decorators",        True),
            ("constant",   "def",               True),
            ("formatting", "first_formatting",  True),
            ("string",     "name",              True),
            ("formatting", "second_formatting", True),
            ("constant",   "(",                 True),
            ("formatting", "third_formatting",  True),
            ("list",       "arguments",         True),
            ("formatting", "fourth_formatting", True),
            ("constant",   ")",                 True),
            ("formatting", "fifth_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "sixth_formatting",  True),
            ("list",       "value",             True),
        ],

        "call_argument": [
            ("key",        "target",            "target"),
            ("formatting", "first_formatting",  "target"),
            ("constant",   "=",                 "target"),
            ("formatting", "second_formatting", "target"),
            ("key",        "value",             True),
        ],
        "def_argument": [
            ("key",        "target",            True),
            ("formatting", "first_formatting",  "value"),
            ("constant",   "=",                 "value"),
            ("formatting", "second_formatting", "value"),
            ("key",        "value",             "value"),
        ],
        "list_argument": [
            ("constant",   "*",                 True),
            ("formatting", "formatting",        True),
            ("key",        "value",             True),
        ],
        "dict_argument": [
            ("constant",   "**",                True),
            ("formatting", "formatting",        True),
            ("key",        "value",             True),
        ],

        "return": [
            ("constant",   "return",            True),
            ("formatting", "formatting",        True),
            ("key",        "value",             "value"),
        ],

        "raise": [
            ("constant",   "raise",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             "value"),
            ("formatting", "second_formatting", "instance"),
            ("constant",   ",",                 "instance"),
            ("formatting", "third_formatting",  "instance"),
            ("key",        "instance",          "instance"),
            ("formatting", "fourth_formatting", "traceback"),
            ("constant",   ",",                 "traceback"),
            ("formatting", "fifth_formatting",  "traceback"),
            ("key",        "traceback",         "traceback"),
        ],

        "assert": [
            ("constant",   "assert",            True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", "message"),
            ("constant",   ",",                 "message"),
            ("formatting", "third_formatting",  "message"),
            ("key",        "message",           "message"),
        ],

        "set_comprehension": [
            ("formatting", "first_formatting",  True),
            ("constant",   "{",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "result",            True),
            ("list",       "generators",        True),
            ("formatting", "third_formatting",  True),
            ("constant",   "}",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "dict_comprehension": [
            ("formatting", "first_formatting",  True),
            ("constant",   "{",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "result",            True),
            ("list",       "generators",        True),
            ("formatting", "third_formatting",  True),
            ("constant",   "}",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "argument_generator_comprehension": [
            ("key",  "result",                  True),
            ("list", "generators",              True),
        ],
        "generator_comprehension": [
            ("formatting", "first_formatting",  True),
            ("constant",   "(",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "result",            True),
            ("list",       "generators",        True),
            ("formatting", "third_formatting",  True),
            ("constant",   ")",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "list_comprehension": [
            ("formatting", "first_formatting",  True),
            ("constant",   "[",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "result",            True),
            ("list",       "generators",        True),
            ("formatting", "third_formatting",  True),
            ("constant",   "]",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "comprehension_loop": [
            ("formatting", "first_formatting",  True),
            ("constant",   "for",               True),
            ("formatting", "second_formatting", True),
            ("key",        "iterator",          True),
            ("formatting", "third_formatting",  True),
            ("constant",   "in",                True),
            ("formatting", "fourth_formatting", True),
            ("key",        "target",            True),
            ("list",       "ifs",               True),
        ],
        "comprehension_if": [
            ("formatting", "first_formatting",  True),
            ("constant",   "if",                True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
        ],

        "getitem": [
            ("formatting", "first_formatting",  True),
            ("constant",   "[",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   "]",                 True),
            ("formatting", "fourth_formatting", True),
        ],

        "slice": [
            ("key",        "lower",             "lower"),
            ("formatting", "first_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "upper",             "upper"),
            ("formatting", "third_formatting",  "has_two_colons"),
            ("constant",   ":",                 "has_two_colons"),
            ("formatting", "fourth_formatting", "has_two_colons"),
            ("key",        "step",              ["has_two_colons", "step"]),
            ("bool",       "has_two_colons",    False),
        ],

        "assignment": [
            ("key",        "target",            True),
            ("formatting", "first_formatting",  True),
            # FIXME should probably be a different node type
            ("string",     "operator",          "operator"),
            ("constant",   "=",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
        ],

        "unitary_operator": [
            ("string",     "value",             True),
            ("formatting", "formatting",        True),
            ("key",        "target",            True),
        ],
        "binary_operator": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
            ("key",        "second",            True),
        ],
        "boolean_operator": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("string",     "value",             True),
            ("formatting", "second_formatting", True),
            ("key",        "second",            True),
        ],
        "comparison_operator": [
            ("string",     "first",             True),
            ("formatting", "formatting",        True),
            ("string",     "second",            "second"),
        ],
        "comparison": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
            ("key",        "second",            True),
        ],

        "with": [
            ("constant",   "with",              True),
            ("formatting", "first_formatting",  True),
            ("list",       "contexts",          True),
            ("formatting", "second_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "third_formatting",  True),
            ("list",       "value",             True),
        ],
        "with_context_item": [
            ("key",        "value",             True),
            ("formatting", "first_formatting",  "as"),
            ("constant",   "as",                "as"),
            ("formatting", "second_formatting", "as"),
            ("key",        "as",                "as"),
        ],

        "del": [
            ("constant",   "del",               True),
            ("formatting", "formatting",        True),
            ("key",        "value",             True),
        ],
        "yield": [
            ("constant",   "yield",             True),
            ("formatting", "formatting",        True),
            ("key",        "value",             "value"),
        ],
        "yield_atom": [
            ("constant",   "(",                 True),
            ("formatting", "first_formatting",  True),
            ("constant",   "yield",             True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             "value"),
            ("formatting", "third_formatting",  True),
            ("constant",   ")",                 True),
        ],

        "exec": [
            ("constant",   "exec",              True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", "globals"),
            ("constant",   "in",                "globals"),
            ("formatting", "third_formatting",  "globals"),
            ("key",        "globals",           "globals"),
            ("formatting", "fourth_formatting", "locals"),
            ("constant",   ",",                 "locals"),
            ("formatting", "fifth_formatting",  "locals"),
            ("key",        "locals",            "locals"),
        ],
        "global": [
            ("constant",   "global",            True),
            ("formatting", "formatting",        True),
            ("list",       "value",             True),
        ],

        "while": [
            ("constant",   "while",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "test",              True),
            ("formatting", "second_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "third_formatting",  True),
            ("list",       "value",             True),
            ("key",        "else",              "else"),
        ],
        "for": [
            ("constant",   "for",               True),
            ("formatting", "first_formatting",  True),
            ("key",        "iterator",          True),
            ("formatting", "second_formatting", True),
            ("constant",   "in",                True),
            ("formatting", "third_formatting",  True),
            ("key",        "target",            True),
            ("formatting", "fourth_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "fifth_formatting",  True),
            ("list",       "value",             True),
            ("key",        "else",              "else"),
        ],
        "if": [
            ("constant",   "if",                True),
            ("formatting", "first_formatting",  True),
            ("key",        "test",              True),
            ("formatting", "second_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "third_formatting",  True),
            ("list",       "value",             True),
        ],
        "elif": [
            ("constant",   "elif",              True),
            ("formatting", "first_formatting",  True),
            ("key",        "test",              True),
            ("formatting", "second_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "third_formatting",  True),
            ("list",       "value",             True),
        ],
        "else": [
            ("constant",   "else",              True),
            ("formatting", "first_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
        ],
        "lambda": [
            ("constant",   "lambda",            True),
            ("formatting", "first_formatting",  True),
            ("list",       "arguments",         True),
            ("formatting", "second_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "third_formatting",  True),
            ("key",        "value",             True),
        ],
        "try": [
            ("constant",   "try",               True),
            ("formatting", "first_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
            ("list",       "excepts",           True),
            ("key",        "else",              "else"),
            ("key",        "finally",           "finally"),
        ],
        "except": [
            ("constant",   "except",            True),
            ("formatting", "first_formatting",  True),
            ("key",        "exception",         "exception"),
            ("formatting", "second_formatting", "delimiter"),
            ("string",     "delimiter",         "delimiter"),
            ("formatting", "third_formatting",  "delimiter"),
            ("key",        "target",            "delimiter"),
            ("formatting", "fourth_formatting", True),
            ("constant",   ":",                 True),
            ("formatting", "fifth_formatting",  True),
            ("list",       "value",             True),
        ],
        "finally": [
            ("constant",   "finally",           True),
            ("formatting", "first_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
        ],

        "dict": [
            ("formatting", "first_formatting",  True),
            ("constant",   "{",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   "}",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "set": [
            ("formatting", "first_formatting",  True),
            ("constant",   "{",                 True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   "}",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "dictitem": [
            ("key",        "key",               True),
            ("formatting", "first_formatting",  True),
            ("constant",   ":",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
        ],

        "import": [
            ("formatting", "first_formatting",  True),
            ("constant",   "import",            True),
            ("formatting", "second_formatting", True),
            ("list",       "value",             True),
        ],
        "from_import": [
            ("constant",   "from",              True),
            ("formatting", "first_formatting",  True),
            ("list",       "value",             True),
            ("formatting", "second_formatting", True),
            ("constant",   "import",            True),
            ("formatting", "third_formatting",  True),
            ("list",       "targets",           True),
        ],

        "dotted_as_name": [
            ("list",       "value",             True),
            ("formatting", "first_formatting",  "target"),
            ("constant",   "as",                "target"),
            ("formatting", "second_formatting", "target"),
            ("string",     "target",            "target"),
        ],
        "name_as_name": [
            ("string",     "value",             True),
            ("formatting", "first_formatting",  "target"),
            ("constant",   "as",                "target"),
            ("formatting", "second_formatting", "target"),
            ("string",     "target",            "target"),
        ],

        "print": [
            ("constant",   "print",                  True),
            ("formatting", "formatting",             True),
            ("constant",   ">>",                     "destination"),
            ("formatting", "destination_formatting", "destination"),
            ("key",        "destination",            "destination"),
            ("list",       "value",                  "value"),
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
            raise NotImplemented("Unknown key type: %s" % key_type)

        to_call = getattr(self, 'before_' + key_type)

        return to_call(item, render_key)

    def after(self, key_type, item, render_key):
        if key_type not in node_types:
            raise NotImplemented("Unknown key type: %s" % key_type)

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
