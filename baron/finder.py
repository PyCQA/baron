from .walker import NodeWalker


def find(tree, line, column):
    return PositionFinder().find(tree, line, column)


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
        self.reset()

    def reset(self):
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
    def find(self, tree, line, column):
        self.current = Position(1,1)
        self.target = Position(line, column)
        self.path_found = False
        self.stop = self.CONTINUE
        self.path = PathHandler()

        self.walk(tree)
        return self.path.get_path() if self.path_found else None

    def after_list(self, node, pos):
        if self.path_found:
            self.path.add_list_level(pos)

        return self.stop

    def after_dict(self, item, render_pos, render_key, key_type):
        if self.path_found:
            if key_type == 'formatting':
                self.path.reset()
            self.path.add_dict_level(render_key, item["type"], render_pos)

        return self.stop

    # The constant node is not interesting for the path: every leaf node is
    # a constant. What's more interesting is the parent node, with its type
    # and position_in_rendering_list.
    def on_constant(self, constant):
        if constant == "\n":
            self.current.advance_line()
            if targetted_line_is_passed(self.target, self.current):
                self.stop = self.STOP
            return self.stop

        advance_by = len(constant)
        if is_on_targetted_node(self.target, self.current, advance_by):
            self.path_found = True
            self.stop = self.STOP
            return self.stop

        self.current.advance_columns(advance_by)
        return self.stop


def is_on_targetted_node(target, current, length):
    return target.line == current.line \
        and target.column >= current.column \
        and target.column < current.column + length


def targetted_line_is_passed(target, current):
    return current.line > target.line

