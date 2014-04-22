from .dumper import dumps


def render(node):
    for pos, (key_type, render_key, dependent) in enumerate(rendering_dictionnary[node['type']]):
        if not dependent and not node.get(render_key):
            continue
        elif isinstance(dependent, str) and not node.get(dependent):
            continue
        elif isinstance(dependent, list) and not all([node.get(x) for x in dependent]):
            continue

        if key_type == 'list':
            value = node[render_key]
        elif key_type == 'key':
            value = node[render_key]
        elif key_type == 'constant':
            value = render_key
            render_key = None
        elif key_type == 'formatting':
            #TODO do not use dumps from dumper
            value = dumps(node[render_key])
        yield (pos+1, render_key, value)


rendering_dictionnary = {
        "assignment": [
            ("key",        "target",            True ),
            ("formatting", "first_formatting",  True ),
            ("key",        "operator",          False),
            ("constant",   "=",                 True ),
            ("formatting", "second_formatting", True ),
            ("key",        "value",             True )
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
            ("list",       "value",             True)
        ],
        "def_argument": [
            ("key",        "name",              True),
            ("formatting", "first_formatting",  "value"),
            ("constant",   "=",                 "value"),
            ("formatting", "second_formatting", "value"),
            ("key",        "value",             "value"),
        ],
        "space": [
            ("key", "value", True)
        ],
        "name": [
            ("key", "value", True)
        ],
        "int": [
            ("key", "value", True)
        ],
        "comma": [
            ("formatting", "first_formatting",  True),
            ("constant",   ",",                 True),
            ("formatting", "second_formatting", True),
        ],
        "endl": [
            ("formatting", "formatting",  True),
            ("key",        "value",       True),
            ("key",        "indent",      True),
        ],
        "decorator": [
            ("constant",   "@",     True),
            ("key",        "value", True),
            ("key",        "call",  False),
        ],
        "dotted_name": [
            ("list", "value", True),
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
        "call_argument": [
            ("key",        "name",              "name"),
            ("formatting", "first_formatting",  "name"),
            ("constant",   "=",                 "name"),
            ("formatting", "second_formatting", "name"),
            ("key",        "value",             True),
        ],
        "string": [
            ("formatting", "first_formatting",  True),
            ("key",        "value",             True),
            ("formatting", "second_formatting", True),
        ],
        "pass": [
            ("constant", "pass", True),
        ],
        "dict_argument": [
            ("constant", "**",         True),
            ("list",     "formatting", True),
            ("key",      "value",      True),
        ],
        "atomtrailers": [
            ("list", "value", True)
        ],
        "dot": [
            ("formatting", "first_formatting",  True),
            ("constant",   ".",                 True),
            ("formatting", "second_formatting", True),
        ],
    }
