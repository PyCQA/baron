from utils import create_node_from_token

def include_imports(pg):
    @pg.production("statement : import")
    @pg.production("statement : from_import")
    def separator((statement,)):
        return [statement]

    @pg.production("import : IMPORT SPACE dotted_as_names")
    def importeu((import_, space, dotted_as_names)):
        return {
                "type": "import",
                "value": dotted_as_names,
                "space": space.value
               }

    @pg.production("from_import : FROM from_import_module IMPORT SPACE? from_import_target")
    def from_import_with_space((from_, from_import_module, import_, space, from_import_target)):
        result = {
                  "type": "from_import",
                  "targets": from_import_target,
                  "after_space": space.value if space else ""
                 }
        result.update(from_import_module)
        return result

    @pg.production("from_import_module : SPACE? dotted_name SPACE?")
    def from_import_module((space, dotted_name, space2)):
        return {
                "before_space": space.value if space else "",
                "middle_space": space2.value if space2 else "",
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
        return [{
                 "type": "left_parenthesis",
                 "value": "("
                }]\
                + name_as_names +\
                [{
                  "type": "right_parenthesis",
                  "value": ")"
                 }]

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

    @pg.production("name_as_name : NAME SPACE AS SPACE NAME")
    def name_as_name_name_as_name((name, space, as_, space2, name2)):
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "before_space": space.value,
                 "after_space": space2.value,
                 "as_": True,
                 "target": name2.value
                }]

    @pg.production("name_as_name : NAME")
    def name_as_name_name((name,)):
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "before_space": "",
                 "after_space": ""
                }]

    @pg.production("name_as_name : NAME SPACE")
    def name_as_name_name_space((name, space)):
        return [{
                 "type": "name_as_name",
                 "value": name.value,
                 "before_space": "",
                 "after_space": ""
                }] + [create_node_from_token(space)]

    @pg.production("name_as_name : COMMA")
    @pg.production("name_as_name : SPACE")
    def name_as_name_comma_space((name_as_name,)):
        return [create_node_from_token(name_as_name)]

    @pg.production("dotted_as_names : dotted_as_names COMMA SPACE dotted_as_name")
    def dotted_as_names_dotted_as_names_dotted_as_name((dotted_as_names, comma, space, dotted_as_names2)):
        return dotted_as_names +\
                [{
                  "type": "comma",
                  "value": ","
                 },
                 {
                  "type": "space",
                  "value": " "
                 }]\
                 + dotted_as_names2

    @pg.production("dotted_as_names : dotted_as_name")
    def dotted_as_names_dotted_as_name((dotted_as_name,)):
        return dotted_as_name

    @pg.production("dotted_as_name : dotted_name SPACE AS SPACE NAME")
    def dotted_as_name_as((dotted_as_name, space, as_, space2, name)):
        return [{
                 "type": "dotted_as_name",
                 "value": {
                           "type": "dotted_name",
                           "value": dotted_as_name
                          },
                 "before_space": space.value,
                 "after_space": space2.value,
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
    @pg.production("dotted_name_element : DOT")
    @pg.production("dotted_name_element : SPACE")
    def dotted_name((token,)):
        return [create_node_from_token(token)]
