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
        self.node_type = None
        self.position_in_rendering_list = None

    def push(self, elem):
        self.path = [elem] + self.path

    def setTypeIfNotSet(self, type):
        if self.node_type is None:
            self.node_type = type

    def setPositionIfNotSet(self, pos):
        if self.position_in_rendering_list is None:
            self.position_in_rendering_list = pos

    def get_path(self):
        return {
                "path": self.path,
                "type": self.node_type,
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
            self.path.push(pos)

        return self.stop

    def after_dict(self, item, render_pos, render_key, key_type):
        if self.path_found:
            if key_type == 'formatting':
                self.path.reset()
            if render_key:
                self.path.push(render_key)
            self.path.setTypeIfNotSet(item["type"])
            self.path.setPositionIfNotSet(render_pos)

        return self.stop

    # The constant node is not interesting for the path: every leaf node is
    # a constant. What's more interesting is the parent node, with its type
    # and position_in_rendering_list.
    def on_constant(self, constant):
        if constant == "\n":
            self.current.advance_line()
            if self.targetted_line_is_passed():
                self.stop = self.STOP
            return self.stop

        advance_by = len(constant)
        if self.is_on_targetted_node(advance_by):
            self.path_found = True
            self.stop = self.STOP
            return self.stop

        self.current.advance_columns(advance_by)
        return self.stop

    def is_on_targetted_node(self, advance_by):
        return self.target.line == self.current.line \
            and self.target.column >= self.current.column \
            and self.target.column <  self.current.column + advance_by

    def targetted_line_is_passed(self):
        return self.current.line > self.target.line

