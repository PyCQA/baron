from .render import RenderWalker


def find(tree, line, column):
    return PositionFinder().find(tree, line, column)


def get_node_at_end_of_path(tree, path):
    node = tree
    for key in path['path']:
        node = node[key]
    return node


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


class PositionFinder(RenderWalker):
    """Find a node by line and column and return the path to it.

    First, walk through all the nodes while maintaining the current line
    and column. When the targetted node is found, stop there and build
    the path while going back up the tree.
    """
    def find(self, tree, line, column):
        self.current = Position(1,1)
        self.target = Position(line, column)
        self.path_found = False
        self.stop = self.CONTINUE
        self.path = PathHandler()

        self.walk(tree)
        return self.path.get_path() if self.path_found else None

    def after_list(self, node, pos, key):
        if self.path_found:
            self.path.push(key)

        return self.stop

    def after_key(self, node, pos, key):
        if self.path_found:
            self.path.push(key)
            if 'type' in node:
                self.path.setTypeIfNotSet(node['type'])

        return self.stop

    def after_formatting(self, node, pos, key):
        if self.path_found:
            self.path.push(key)

        return self.stop

    def after_node(self, node, pos, key):
        if self.path_found:
            self.path.push(key)
            self.path.setPositionIfNotSet(pos)
            self.path.setTypeIfNotSet(node['type'])

        return self.stop

    def on_constant(self, constant, pos, key):
        """Determine if we're on the targetted node.
        
        If the targetted column is reached, `stop` and `path_found` are
        set. If the targetted line is passed, only `stop` is set. This
        prevents unnecessary tree travelling when the targetted column
        is out of bounds.
        """
        if constant == "\n":
            self.current.advance_line()
            if self.targetted_line_is_passed():
                self.stop = self.STOP
            return self.stop

        advance_by = len(constant)
        if self.is_on_targetted_node(advance_by):
            self.path.setPositionIfNotSet(pos)
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

