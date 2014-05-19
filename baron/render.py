def render(node):
    for pos, (key_type, render_key, dependent) in enumerate(rendering_dictionnary[node['type']]):
        if not dependent and not node.get(render_key):
            continue
        elif isinstance(dependent, str) and not node.get(dependent):
            continue
        elif isinstance(dependent, list) and not all([node.get(x) for x in dependent]):
            continue

        if key_type in ['list', 'key', 'formatting']:
            value = node[render_key]
        elif key_type == 'constant':
            value = render_key
            render_key = None
        else:
            raise NotImplemented("Unknown key type: %s" % key_type)

        yield (pos, render_key, key_type, value)


rendering_dictionnary = {
        "int":               [("key", "value", True)],
        "name":              [("key", "value", True)],
        "hexa":              [("key", "value", True)],
        "octa":              [("key", "value", True)],
        "float":             [("key", "value", True)],
        "space":             [("key", "value", True)],
        "binary":            [("key", "value", True)],
        "complex":           [("key", "value", True)],
        "float_exponant":    [("key", "value", True)],
        "left_parenthesis":  [("key", "value", True)],
        "right_parenthesis": [("key", "value", True)],

        "break":    [("key", "type", True)],
        "continue": [("key", "type", True)],
        "pass":     [("key", "type", True)],

        "dotted_name":  [("list", "value", True)],
        "ifelseblock":  [("list", "value", True)],
        "atomtrailers": [("list", "value", True)],
        "string_chain": [("list", "value", True)],

        "endl": [
            ("formatting", "formatting",  True),
            ("key",        "value",       True),
            ("key",        "indent",      True),
        ],

        "star": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "raw_string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "binary_string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "unicode_string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "binary_raw_string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "unicode_raw_string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],

        # FIXME ugly, comment can end up in formatting of another
        # node or being standalone, this is bad
        "comment": [
            ("formatting", "formatting", "formatting"),
            ("key",        "value",      True),
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
            ("key",        "value",             True),
            ("formatting", "third_formatting",  True),
            ("constant",   ")",                 True),
            ("formatting", "fourth_formatting", True),
        ],

        "decorator": [
            ("constant",   "@",     True),
            ("key",        "value", True),
            ("key",        "call",  "call"),
        ],

        "class": [
            ("list",       "decorators",        True),
            ("constant",   "class",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "name",              True),
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
            ("list",       "value",             True),
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
        ],

        "funcdef": [
            ("list",       "decorators",        True),
            ("constant",   "def",               True),
            ("formatting", "first_formatting",  True),
            ("key",        "name",              True),
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
            ("key",        "name",              "name"),
            ("formatting", "first_formatting",  "name"),
            ("constant",   "=",                 "name"),
            ("formatting", "second_formatting", "name"),
            ("key",        "value",             True),
        ],
        "def_argument": [
            ("key",        "name",              True),
            ("formatting", "first_formatting",  "value"),
            ("constant",   "=",                 "value"),
            ("formatting", "second_formatting", "value"),
            ("key",        "value",             "value"),
        ],
        "list_argument": [
            ("constant",   "*",          True),
            ("formatting", "formatting", True),
            ("key",        "value",      True),
        ],
        "dict_argument": [
            ("constant",   "**",         True),
            ("formatting", "formatting", True),
            ("key",        "value",      True),
        ],

        "return": [
            ("constant",   "return",     True),
            ("formatting", "formatting", True),
            ("key",        "value",      "value"),
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
            ("key",  "result",     True),
            ("list", "generators", True),
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
    #if isinstance(node["target"], list):
    #    yield dump_node_list(node["target"])
    #else:
    #    yield dump_node(node["target"])
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
        ],

        "assignment": [
            ("key",        "target",            True),
            ("formatting", "first_formatting",  True),
            # FIXME should probably be a different node type
            ("key",        "operator",          "operator"),
            ("constant",   "=",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",             True),
        ],

        "unitary_operator": [
            ("key",        "value",      True),
            ("formatting", "formatting", True),
            ("key",        "target",     True),
        ],
        "binary_operator": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
            ("key",        "second",            True),
        ],
        "boolean_operator": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
            ("key",        "second",            True),
        ],
        "comparison": [
            ("key",        "first",             True),
            ("formatting", "first_formatting",  True),
            ("list",       "middle_formatting", True),
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
            ("key",        "value",             True),
        ],
        "with_context_item": [
            ("key",        "value",             True),
            ("formatting", "first_formatting",  "as"),
            ("constant",   "as",                "as"),
            ("formatting", "second_formatting", "as"),
            ("key",        "as",                "as"),
        ],

        "del": [
            ("constant",   "del",        True),
            ("formatting", "formatting", True),
            ("key",        "value",      True),
        ],
        "yield": [
            ("constant",   "yield",      True),
            ("formatting", "formatting", True),
            ("key",        "value",      "value"),
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
            ("constant",   "global",     True),
            ("formatting", "formatting", True),
            ("list",       "value",      True),
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
            ("formatting", "second_formatting", "delimiteur"),
            ("key",        "delimiteur",        "delimiteur"),
            ("formatting", "third_formatting",  "delimiteur"),
            ("key",        "target",            "delimiteur"),
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
            ("key",        "value",            True),
            ("formatting", "third_formatting",  True),
            ("constant",   "}",                 True),
            ("formatting", "fourth_formatting", True),
        ],
        "set": [
            ("formatting", "first_formatting",  True),
            ("constant",   "{",                 True),
            ("formatting", "second_formatting", True),
            ("key",        "value",            True),
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
            ("key",        "value",             True),
        ],
        "from_import": [
            ("constant",   "from",              True),
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
            ("constant",   "import",            True),
            ("formatting", "third_formatting",  True),
            ("key",        "targets",           True),
        ],

        "dotted_as_name": [
            ("key",        "value",             True),
            ("formatting", "first_formatting",  "as"),
            ("constant",   "as",                "as"),
            ("formatting", "second_formatting", "as"),
            ("key",        "target",            "as"),
        ],
        "name_as_name": [
            ("key",        "value",             True),
            ("formatting", "first_formatting",  "as"),
            ("constant",   "as",                "as"),
            ("formatting", "second_formatting", "as"),
            ("key",        "target",            "as"),
        ],

        "print": [
            ("constant",   "print",                  True),
            ("formatting", "formatting",             True),
            ("constant",   ">>",                     "destination"),
            ("formatting", "destination_formatting", "destination"),
            ("key",        "destination",            "destination"),
            ("key",        "value",                  "value"),
        ],
    }


class RenderWalker:
    '''Inherit me and overload the methods you want'''
    CONTINUE = False
    STOP = True

    def before_list(self, node):
        return self.CONTINUE

    def after_list(self, node, pos):
        return self.CONTINUE

    def before_dict(self, node):
        return self.CONTINUE

    def after_dict(self, node, render_pos, render_key, key_type):
        return self.CONTINUE

    def on_constant(self, constant):
        return self.CONTINUE

    def walk(self, node):
        if isinstance(node, list):
            return self.walk_on_list(node)
        elif isinstance(node, dict):
            return self.walk_on_dict(node)
        else:
            return self.walk_on_constant(node)

    def walk_on_list(self, node):
        stop = self.before_list(node)
        if stop:
            return stop

        pos = None
        for pos, child in enumerate(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.after_list(node, pos)
        return stop


    def walk_on_dict(self, node):
        stop = self.before_dict(node)
        if stop:
            return stop

        render_pos = None
        render_key = None
        for render_pos, render_key, key_type, child in render(node):
            stop = self.walk(child)
            if stop:
                break

        stop |= self.after_dict(node, render_pos, render_key, key_type)
        return stop


    def walk_on_constant(self, node):
        return self.on_constant(node)

