from utils import create_node_from_token

def include_imports(pg):
    @pg.production("small_stmt : import")
    @pg.production("small_stmt : from_import")
    def separator((statement,)):
        return statement

    @pg.production("import : IMPORT dotted_as_names")
    def importeu((import_, dotted_as_names)):
        return {
                "type": "import",
                "value": dotted_as_names,
                "space": import_.after_space
               }

    @pg.production("from_import : FROM dotted_name IMPORT from_import_target")
    def from_import_with_space((from_, dotted_name, import_, from_import_target)):
        return {
                "type": "from_import",
                "targets": from_import_target,
                "after_space": import_.after_space,
                "before_space": from_.after_space,
                "middle_space": import_.before_space,
                "value": {
                          "type": "dotted_name",
                          "value": dotted_name
                         }
               }

    @pg.production("from_import_target : name_as_names")
    def from_import_target_name_as_names((name_as_names,)):
        return name_as_names

    @pg.production("from_import_target : LEFT_PARENTHESIS name_as_names RIGHT_PARENTHESIS")
    def from_import_parenthesis((left_parenthesis, name_as_names, right_parenthesis)):
        to_return = [{
                 "type": "left_parenthesis",
                 "value": "("
                }] + name_as_names
        if right_parenthesis.before_space:
                to_return += [{"type": "space", "value": right_parenthesis.before_space}]

        to_return += [{"type": "right_parenthesis", "value": ")"}]
        return to_return

    @pg.production("from_import_target : STAR")
    def from_import_star((star,)):
        return [{
                 "type": "star",
                 "value": "*"
                }]

    @pg.production("name_as_names : name_as_names name_as_name")
    def name_as_names_name_as_name((name_as_names, name_as_name)):
        return name_as_names + name_as_name

    @pg.production("name_as_names : name_as_name")
    def name_as_names((name_as_name,)):
        return name_as_name

    @pg.production("name_as_name : NAME AS NAME")
    def name_as_name_name_as_name((name, as_, name2)):
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "before_space": as_.before_space,
                 "after_space": as_.after_space,
                 "as_": True,
                 "target": name2.value
                }]

    @pg.production("name_as_name : NAME")
    def name_as_name_name((name,)):
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "as_": False,
                 "target": None,
                 "before_space": "",
                 "after_space": ""
                }]

    @pg.production("name_as_name : NAME SPACE")
    def name_as_name_name_space((name, space)):
        return [{
                 "type": "name_as_name",
                 "target": None,
                 "value": name.value,
                 "before_space": "",
                 "after_space": ""
                }] + [create_node_from_token(space)]

    @pg.production("name_as_name : COMMA")
    def name_as_name_comma_space((comma,)):
        to_return = []
        if comma.before_space:
            to_return += [{"type": "space", "value": comma.before_space}]
        to_return += [create_node_from_token(comma)]
        if comma.after_space:
            to_return += [{"type": "space", "value": comma.after_space}]
        return to_return

    @pg.production("dotted_as_names : dotted_as_names COMMA dotted_as_name")
    def dotted_as_names_dotted_as_names_dotted_as_name((dotted_as_names, comma, dotted_as_names2)):
        return dotted_as_names +\
                [{
                  "type": "comma",
                  "value": ","
                 },
                 {
                  "type": "space",
                  "value": comma.after_space,
                 }]\
                 + dotted_as_names2

    @pg.production("dotted_as_names : dotted_as_name")
    def dotted_as_names_dotted_as_name((dotted_as_name,)):
        return dotted_as_name

    @pg.production("dotted_as_name : dotted_name AS NAME")
    def dotted_as_name_as((dotted_as_name, as_, name)):
        return [{
                 "type": "dotted_as_name",
                 "value": {
                           "type": "dotted_name",
                           "value": dotted_as_name
                          },
                 "before_space": as_.before_space,
                 "after_space": as_.after_space,
                 "target": name.value,
                 "as_": True
                }]

    @pg.production("dotted_as_name : dotted_name")
    def dotted_as_name((dotted_name,)):
        return [{
                 "type": "dotted_as_name",
                 "value": {
                           "type": "dotted_name",
                           "value": dotted_name
                          },
                 "before_space": "",
                 "after_space": ""
                }]

    @pg.production("dotted_name : dotted_name dotted_name_element")
    def dotted_name_elements_element((dotted_name, dotted_name_element)):
        return dotted_name + dotted_name_element

    @pg.production("dotted_name : dotted_name_element")
    def dotted_name_element((dotted_name_element,)):
        return dotted_name_element

    @pg.production("dotted_name_element : NAME")
    @pg.production("dotted_name_element : SPACE")
    def dotted_name((token,)):
        return [create_node_from_token(token)]

    @pg.production("dotted_name_element : DOT")
    def dotted_name_dot((dot,)):
        to_return = []
        if dot.before_space:
            to_return += [{"type": "space", "value": dot.before_space}]
        to_return += [create_node_from_token(dot)]
        if dot.after_space:
            to_return += [{"type": "space", "value": dot.after_space}]
        return to_return
