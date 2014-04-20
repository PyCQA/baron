from .rendering_dictionnary import rendering_dictionnary as d
from .dumper import dumps
import json


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def advance_columns(self, columns):
        self.column += columns

    def advance_line(self):
        self.advance_lines(1)

    def advance_lines(self, lines):
        self.line += 1
        self.column = 1


def path_to_location(tree, line, column):
    current = Position(1,1)
    target = Position(line, column)

    found = path_to_location_walk(tree, current, target)
    if not found:
        return None
    else:
        return json.dumps(found)


def path_to_location_walk(node, current, target):
    if isinstance(node, list):
        for pos, child in enumerate(node):
            found = path_to_location_walk(child, current, target)
            if found is False:
                return False
            elif found is not None:
                found["path"] = [pos] + found["path"]
                return found
    elif isinstance(node, dict):
        for render_pos, key_type, render_key, value in render(node):
            if key_type == 'list':
                found = path_to_location_walk(node[render_key], current, target)
            else:
                found = path_to_location_walk(value, current, target)

            if found is False:
                return False
            elif found is not None:
                if render_key is not None:
                    found["path"] = [render_key] + found["path"]
                if found["type"] is None:
                    found["type"] = node["type"]
                    found["position_in_rendering_list"] = render_pos
                return found
    else:
        if node == "\n":
            current.advance_line()
            if targetted_line_is_passed(target, current):
                return False
        else:
            advance_by = len(node)
            if is_on_targetted_node(target, current, advance_by):
                return {"path":[], "type":None, "position_in_rendering_list":None}
            current.advance_columns(advance_by)
        
    return None


def is_on_targetted_node(target, current, length):
    return target.line == current.line \
        and target.column >= current.column \
        and target.column < current.column + length


def targetted_line_is_passed(target, current):
    return current.line > target.line


def render(node):
    for pos, (key_type, render_key, dependent) in enumerate(d[node['type']]):
        if not dependent and not node.get(render_key):
            continue
        elif isinstance(dependent, str) and not node.get(dependent):
            continue
        elif isinstance(dependent, list) and not all([node.get(x) for x in dependent]):
            continue

        if key_type == 'list':
            value = ''
        elif key_type == 'key':
            value = node[render_key]
        elif key_type == 'constant':
            value = render_key
            render_key = None
        elif key_type == 'formatting':
            #TODO do not use dumps from dumper
            value = dumps(node[render_key])
        yield (pos+1, key_type, render_key, value)

