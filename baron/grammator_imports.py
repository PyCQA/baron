from .utils import create_node_from_token

def include_imports(pg):
    @pg.production("small_stmt : import")
    @pg.production("small_stmt : from_import")
    def separator(pack):
        (statement,) = pack
        return statement

    @pg.production("import : IMPORT dotted_as_names")
    def importeu(pack):
        (import_, dotted_as_names) = pack
        return {
                "type": "import",
                "value": dotted_as_names,
                "first_formatting": import_.hidden_tokens_before,
                "second_formatting": import_.hidden_tokens_after
               }

    @pg.production("from_import : FROM dotted_name IMPORT from_import_target")
    def from_import_with_space(pack):
        (from_, dotted_name, import_, from_import_target) = pack
        return {
                "type": "from_import",
                "targets": from_import_target,
                "first_formatting": from_.hidden_tokens_after,
                "second_formatting": import_.hidden_tokens_before,
                "third_formatting": import_.hidden_tokens_after,
                "value": dotted_name
               }

    @pg.production("from_import_target : name_as_names")
    def from_import_target_name_as_names(pack):
        (name_as_names,) = pack
        return name_as_names

    @pg.production("from_import_target : LEFT_PARENTHESIS name_as_names RIGHT_PARENTHESIS")
    def from_import_parenthesis(pack):
        (left_parenthesis, name_as_names, right_parenthesis) = pack
        return left_parenthesis.hidden_tokens_before +\
               [{"type": "left_parenthesis", "value": "("}] +\
               left_parenthesis.hidden_tokens_after +\
               name_as_names +\
               right_parenthesis.hidden_tokens_before +\
               [{"type": "right_parenthesis", "value": ")"}] +\
               right_parenthesis.hidden_tokens_after

    @pg.production("from_import_target : STAR")
    def from_import_star(pack):
        (star,) = pack
        return [{
                 "type": "star",
                 "value": "*",
                 "first_formatting": star.hidden_tokens_before,
                 "second_formatting": star.hidden_tokens_after
                }]

    @pg.production("name_as_names : name_as_names name_as_name")
    def name_as_names_name_as_name(pack):
        (name_as_names, name_as_name) = pack
        return name_as_names + name_as_name

    @pg.production("name_as_names : name_as_name")
    def name_as_names(pack):
        (name_as_name,) = pack
        return name_as_name

    @pg.production("name_as_name : NAME AS NAME")
    def name_as_name_name_as_name(pack):
        (name, as_, name2) = pack
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "first_formatting": as_.hidden_tokens_before,
                 "second_formatting": as_.hidden_tokens_after,
                 "target": name2.value
                }]

    @pg.production("name_as_name : NAME")
    def name_as_name_name(pack):
        (name,) = pack
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "target": "",
                 "first_formatting": [],
                 "second_formatting": []
                }]

    @pg.production("name_as_name : NAME SPACE")
    def name_as_name_name_space(pack):
        (name, space) = pack
        return [{
                 "type": "name_as_name",
                 "target": None,
                 "value": name.value,
                 "first_formatting": [],
                 "second_formatting": []
                }] + [create_node_from_token(space)]

    @pg.production("name_as_name : comma")
    def name_as_name_comma_space(pack):
        (comma,) = pack
        return [comma]

    @pg.production("dotted_as_names : dotted_as_names comma dotted_as_name")
    def dotted_as_names_dotted_as_names_dotted_as_name(pack):
        (dotted_as_names, comma, dotted_as_names2) = pack
        return dotted_as_names + [comma] + dotted_as_names2

    @pg.production("dotted_as_names : dotted_as_name")
    def dotted_as_names_dotted_as_name(pack):
        (dotted_as_name,) = pack
        return dotted_as_name

    @pg.production("dotted_as_name : dotted_name AS NAME")
    def dotted_as_name_as(pack):
        (dotted_name, as_, name) = pack
        return [{
                 "type": "dotted_as_name",
                 "value": dotted_name,
                 "first_formatting": as_.hidden_tokens_before,
                 "second_formatting": as_.hidden_tokens_after,
                 "target": name.value,
                }]

    @pg.production("dotted_as_name : dotted_name")
    def dotted_as_name(pack):
        (dotted_name,) = pack
        return [{
                 "type": "dotted_as_name",
                 "value": dotted_name,
                 "first_formatting": [],
                 "second_formatting": [],
                 "target": ""
                }]

    @pg.production("dotted_name : dotted_name dotted_name_element")
    def dotted_name_elements_element(pack):
        (dotted_name, dotted_name_element) = pack
        return dotted_name + dotted_name_element

    @pg.production("dotted_name : dotted_name_element")
    def dotted_name_element(pack):
        (dotted_name_element,) = pack
        return dotted_name_element

    @pg.production("dotted_name_element : NAME")
    @pg.production("dotted_name_element : SPACE")
    def dotted_name(pack):
        (token,) = pack
        return [create_node_from_token(token)]

    @pg.production("dotted_name_element : DOT")
    def dotted_name_dot(pack):
        (dot,) = pack
        return [{
            "type": "dot",
            "first_formatting": dot.hidden_tokens_before,
            "second_formatting": dot.hidden_tokens_after,
        }]
