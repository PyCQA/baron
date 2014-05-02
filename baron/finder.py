from .walker import NodeWalker


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def advance_columns(self, columns):
        self.column += columns

    def advance_line(self):
        self.line += 1
        self.column = 1


class PathHandler:
    def __init__(self):
        self.path = []
        self.type = None
        self.position_in_rendering_list = None

    def add_list_level(self, index):
        self.path = [index] + self.path

    def add_dict_level(self, render_key, render_type, render_index):
        if render_key:
            self.path = [render_key] + self.path

        if self.leaf_node_not_specified():
            self.type = render_type
            self.position_in_rendering_list = render_index

    def leaf_node_not_specified(self):
        return self.type is None

    def get_path(self):
        return {
                "path": self.path,
                "type": self.type,
                "position_in_rendering_list": self.position_in_rendering_list
            }


class PositionFinder(NodeWalker):
    def __init__(self):
        NodeWalker.__init__(self)
        self.current = None
        self.target = None
        self.path_found = None

    def find(self, tree, line, column):
        self.current = Position(1,1)
        self.target = Position(line, column)
        self.path_found = None

        self.walk(tree)
        return self.path_found.get_path() if self.path_found else None

    def on_list(self, node, pos):
        if self.path_found:
            self.path_found.add_list_level(pos)
            return True
        return False

    def on_dict(self, item, render_pos, render_key):
        if self.path_found:
            self.path_found.add_dict_level(render_key, item["type"], render_pos)
            return self.STOP
        return self.CONTINUE

    # The constant node is not interesting for the path: every leaf node is
    # a constant. What's more interesting is the parent node, with its type
    # and position_in_rendering_list, so the function returns an empty
    # PathHandler() object that will be filled by the callee later on.
    def on_constant(self, constant):
        if constant == "\n":
            self.current.advance_line()
            if targetted_line_is_passed(self.target, self.current):
                return True
        else:
            advance_by = len(constant)
            if is_on_targetted_node(self.target, self.current, advance_by):
                self.path_found = PathHandler()
                return True
            self.current.advance_columns(advance_by)
        return False


def is_on_targetted_node(target, current, length):
    return target.line == current.line \
        and target.column >= current.column \
        and target.column < current.column + length


def targetted_line_is_passed(target, current):
    return current.line > target.line

