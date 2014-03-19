def d(j):
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


@node()
def ternary_operator(node):
    yield dump_node(node["first"])
    yield dump_node_list(node["first_formatting"])
    yield "if"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield "else"
    yield dump_node_list(node["forth_formatting"])
    yield dump_node(node["second"])


@node("int")
@node("name")
@node("hexa")
@node("octa")
@node("float")
@node("space")
@node("binary")
@node("complex")
@node("float_exponant")
@node("left_parenthesis")
@node("right_parenthesis")
def get_value(node):
    yield node["value"]


@node("break")
@node("continue")
@node("pass")
def get_type(node):
    yield node["type"]


@node("star")
@node("string")
@node("raw_string")
@node("binary_string")
@node("unicode_string")
@node("binary_raw_string")
@node("unicode_raw_string")
def generic(node):
    yield dump_node_list(node["first_formatting"])
    yield node["value"]
    yield dump_node_list(node["second_formatting"])


@node()
def comment(node):
    # FIXME ugly, comment can end up in formatting of another node or being
    # standalone, this is bad
    yield dump_node_list(node.get("formatting", []))
    yield node["value"]


@node()
def ellipsis(node):
    yield "."
    yield dump_node_list(node["first_formatting"])
    yield "."
    yield dump_node_list(node["second_formatting"])
    yield "."


@node()
def dot(node):
    yield dump_node_list(node["first_formatting"])
    yield "."
    yield dump_node_list(node["second_formatting"])


@node()
def semicolon(node):
    yield dump_node_list(node["first_formatting"])
    yield ";"
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
    yield dump_node_list(node["third_formatting"])
    yield ")"
    yield dump_node_list(node["forth_formatting"])


@node()
def decorator(node):
    yield "@"
    yield dump_node(node["value"])
    if node["call"]:
        yield dump_node(node["call"])


@node()
def class_(node):
    yield dump_node_list(node["decorators"])
    yield "class"
    yield dump_node_list(node["first_formatting"])
    yield node["name"]
    yield dump_node_list(node["second_formatting"])
    if node["parenthesis"]:
        yield "("
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["inherit_from"])
    yield dump_node_list(node["forth_formatting"])
    if node["parenthesis"]:
        yield ")"
    yield dump_node_list(node["fith_formatting"])
    yield ":"
    yield dump_node_list(node["sixth_formatting"])
    yield dump_node_list(node["value"])


@node()
def repr(node):
    yield "`"
    yield dump_node_list(node["first_formatting"])
    yield dump_node_list(node["value"])
    yield dump_node_list(node["second_formatting"])
    yield "`"


@node()
def list_(node):
    yield dump_node_list(node["first_formatting"])
    yield "["
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield "]"
    yield dump_node_list(node["forth_formatting"])


@node()
def associative_parenthesis(node):
    yield dump_node_list(node["first_formatting"])
    yield "("
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield ")"
    yield dump_node_list(node["forth_formatting"])


@node()
def tuple_(node):
    if node["with_parenthesis"]:
        yield dump_node_list(node["first_formatting"])
        yield "("
        yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])
    if node["with_parenthesis"]:
        yield dump_node_list(node["third_formatting"])
        yield ")"
        yield dump_node_list(node["forth_formatting"])


@node()
def funcdef(node):
    yield dump_node_list(node["decorators"])
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


@node("argument")
def funcdef_argument(node):
    if node["value"]:
        yield node["name"]
        yield dump_node_list(node["first_formatting"])
        yield "="
        yield dump_node_list(node["second_formatting"])
        yield dump_node(node["value"])
    elif isinstance(node["name"], basestring):
        yield node["name"]
    else:
        yield dump_node(node["name"])


@node()
def list_argument(node):
    yield "*"
    yield dump_node_list(node["formatting"])
    yield dump_node(node["value"])


@node()
def dict_argument(node):
    yield "**"
    yield dump_node_list(node["formatting"])
    yield dump_node(node["value"])


@node()
def return_(node):
    yield "return"
    yield dump_node_list(node["formatting"])
    if node["value"]:
        yield dump_node(node["value"])


@node()
def raise_(node):
    yield "raise"
    yield dump_node_list(node["first_formatting"])
    if node["value"]:
        yield dump_node(node["value"])
    if node["instance"]:
        yield dump_node_list(node["second_formatting"])
        yield ","
        yield dump_node_list(node["third_formatting"])
        yield dump_node(node["instance"])
    if node["traceback"]:
        yield dump_node_list(node["forth_formatting"])
        yield ","
        yield dump_node_list(node["fith_formatting"])
        yield dump_node(node["traceback"])


@node()
def assert_(node):
    yield "assert"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["value"])
    if node["message"]:
        yield dump_node_list(node["second_formatting"])
        yield ","
        yield dump_node_list(node["third_formatting"])
        yield dump_node(node["message"])


@node("dotted_name")
@node("ifelseblock")
@node("atomtrailers")
@node("string_chain")
def dump_node_list_value(node):
    yield dump_node_list(node["value"])


@node()
def set_comprehension(node):
    yield dump_node_list(node["first_formatting"])
    yield "{"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["result"])
    yield dump_node_list(node["generators"])
    yield dump_node_list(node["third_formatting"])
    yield "}"
    yield dump_node_list(node["forth_formatting"])


@node()
def dict_comprehension(node):
    yield dump_node_list(node["first_formatting"])
    yield "{"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["result"]["key"])
    yield dump_node_list(node["result"]["first_formatting"])
    yield ":"
    yield dump_node_list(node["result"]["second_formatting"])
    yield dump_node(node["result"]["value"])
    yield dump_node_list(node["generators"])
    yield dump_node_list(node["third_formatting"])
    yield "}"
    yield dump_node_list(node["forth_formatting"])


@node()
def argument_generator_comprehension(node):
    yield dump_node(node["result"])
    yield dump_node_list(node["generators"])


@node()
def generator_comprehension(node):
    yield dump_node_list(node["first_formatting"])
    yield "("
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["result"])
    yield dump_node_list(node["generators"])
    yield dump_node_list(node["third_formatting"])
    yield ")"
    yield dump_node_list(node["forth_formatting"])


@node()
def list_comprehension(node):
    yield dump_node_list(node["first_formatting"])
    yield "["
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["result"])
    yield dump_node_list(node["generators"])
    yield dump_node_list(node["third_formatting"])
    yield "]"
    yield dump_node_list(node["forth_formatting"])


@node()
def comprehension_loop(node):
    "for x in x"
    yield dump_node_list(node["first_formatting"])
    yield "for"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["iterator"])
    yield dump_node_list(node["third_formatting"])
    yield "in"
    yield dump_node_list(node["forth_formatting"])
    if isinstance(node["target"], list):
        yield dump_node_list(node["target"])
    else:
        yield dump_node(node["target"])
    yield dump_node_list(node["ifs"])


@node()
def comprehension_if(node):
    yield dump_node_list(node["first_formatting"])
    yield "if"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


@node()
def getitem(node):
    yield dump_node_list(node["first_formatting"])
    yield "["
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield "]"
    yield dump_node_list(node["forth_formatting"])


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
    if node.get("operator"):
        # FIXME should probably be a different node type
        yield node["operator"]
    yield "="
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


@node()
def unitary_operator(node):
    yield node["value"]
    yield dump_node_list(node["formatting"])
    yield dump_node(node["target"])


@node("binary_operator")
@node("boolean_operator")
@node("comparison")
def binary_operator(node):
    yield dump_node(node["first"])
    yield dump_node_list(node["first_formatting"])
    if node["value"] == "not in":  # FIXME ugly :(
        yield "not"
        yield dump_node_list(node["middle_formatting"])
        yield "in"
    else:
        yield node["value"]
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["second"])


@node()
def with_(node):
    yield "with"
    yield dump_node_list(node["first_formatting"])
    yield dump_node_list(node["contexts"])
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node_list(node["value"])


@node()
def with_context_item(node):
    yield dump_node(node["value"])
    if node["as"]:
        yield dump_node_list(node["first_formatting"])
        yield "as"
        yield dump_node_list(node["second_formatting"])
        yield dump_node(node["as"])


@node()
def del_(node):
    yield "del"
    yield dump_node_list(node["formatting"])
    yield dump_node(node["value"])


@node()
def yield_(node):
    yield "yield"
    yield dump_node_list(node["formatting"])
    if node["value"]:
        yield dump_node(node["value"])


@node()
def yield_atom(node):
    yield "("
    yield dump_node_list(node["first_formatting"])
    yield "yield"
    yield dump_node_list(node["second_formatting"])
    if node["value"]:
        yield dump_node(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield ")"


@node()
def exec_(node):
    yield "exec"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["value"])
    if node["globals"]:
        yield dump_node_list(node["second_formatting"])
        yield "in"
        yield dump_node_list(node["third_formatting"])
        yield dump_node(node["globals"])
    if node["locals"]:
        yield dump_node_list(node["forth_formatting"])
        yield ","
        yield dump_node_list(node["fith_formatting"])
        yield dump_node(node["locals"])


@node()
def global_(node):
    yield "global"
    yield dump_node_list(node["formatting"])
    yield dump_node_list(node["value"])


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
def for_(node):
    yield "for"
    yield dump_node_list(node["first_formatting"])
    yield dump_node(node["iterator"])
    yield dump_node_list(node["second_formatting"])
    yield "in"
    yield dump_node_list(node["third_formatting"])
    yield dump_node(node["target"])
    yield dump_node_list(node["forth_formatting"])
    yield ":"
    yield dump_node_list(node["fith_formatting"])
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
def lambda_(node):
    yield "lambda"
    yield dump_node_list(node["first_formatting"])
    for n in node["arguments"]:
        if n["type"] == "argument":
            yield "".join(list(funcdef_argument(n)))
        else:
            yield dump_node(n)
    yield dump_node_list(node["second_formatting"])
    yield ":"
    yield dump_node_list(node["third_formatting"])
    yield dump_node(node["value"])


@node()
def try_(node):
    yield "try"
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])
    yield dump_node_list(node["excepts"])
    if node["else"]:
        yield dump_node(node["else"])
    if node["finally"]:
        yield dump_node(node["finally"])


@node()
def except_(node):
    yield "except"
    yield dump_node_list(node["first_formatting"])
    if node["exception"]:
        yield dump_node(node["exception"])
    if node["delimiteur"]:
        yield dump_node_list(node["second_formatting"])
        yield node["delimiteur"]
        yield dump_node_list(node["third_formatting"])
        yield dump_node(node["target"])
    yield dump_node_list(node["forth_formatting"])
    yield ":"
    yield dump_node_list(node["fith_formatting"])
    yield dump_node_list(node["value"])


@node()
def finally_(node):
    yield "finally"
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])


@node()
def dict_(node):
    yield dump_node_list(node["first_formatting"])
    yield "{"
    yield dump_node_list(node["second_formatting"])
    yield dump_node_list(node["value"])
    yield dump_node_list(node["third_formatting"])
    yield "}"
    yield dump_node_list(node["forth_formatting"])


@node()
def dictitem(node):
    yield dump_node(node["key"])
    yield dump_node_list(node["first_formatting"])
    yield ":"
    yield dump_node_list(node["second_formatting"])
    yield dump_node(node["value"])


@node()
def import_(node):
    yield dump_node_list(node["first_formatting"])
    yield "import"
    yield dump_node_list(node["second_formatting"])
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
    if node["value"]:
        yield dump_node_list(node["value"])


def dumps(tree):
    return "".join(map(dump_node, tree))
