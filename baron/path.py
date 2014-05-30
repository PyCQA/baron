from .render import RenderWalker


def path(path = None, node_type = None, position_in_rendering_list = None):
    return {
        "path": [] if path is None else path,
        "type": node_type,
        "position_in_rendering_list": position_in_rendering_list
    }


def position_to_path(tree, line, column):
    return PositionFinder().find(tree, line, column)


def path_to_node(tree, path):
    if path is None:
        return None
    node = tree
    for key in path['path']:
        node = node[key]
    return node


def position_to_node(tree, line, column):
    return path_to_node(tree, position_to_path(tree, line, column))


def node_to_bounding_box(node):
    return BoundingBox().compute(node)


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
        self.path = path()

        self.walk(tree)
        return self.path if self.path_found else None

    def after_list(self, node, pos, key):
        if self.path_found:
            self.path['path'].insert(0, key)

        return self.stop

    def after_key(self, node, pos, key):
        if self.path_found:
            self.path['path'].insert(0, key)
            if self.path['type'] is None and 'type' in node:
                self.path['type'] = node['type']

        return self.stop

    def after_formatting(self, node, pos, key):
        if self.path_found:
            self.path['path'].insert(0, key)

        return self.stop

    def after_node(self, node, pos, key):
        if self.path_found:
            self.path['path'].insert(0, key)
            if self.path['position_in_rendering_list'] is None:
                self.path['position_in_rendering_list'] = pos
            if self.path['type'] is None:
                self.path['type'] = node['type']

        return self.stop

    def on_leaf(self, constant, pos, key):
        """Determine if we're on the targetted node.

        If the targetted column is reached, `stop` and `path_found` are
        set. If the targetted line is passed, only `stop` is set. This
        prevents unnecessary tree travelling when the targetted column
        is out of bounds.
        """
        newlines_split = split_on_newlines(constant)

        for c in newlines_split:
            if c == "\n":
                self.current.advance_line()
                # if target lined is passed
                if self.current.line > self.target.line:
                    self.stop = self.STOP
                    break

            else:
                advance_by = len(c)
                if self.is_on_targetted_node(advance_by):
                    if self.path['position_in_rendering_list'] is None:
                        self.path['position_in_rendering_list'] = pos
                    self.path_found = True
                    self.stop = self.STOP
                    break
                self.current.advance_columns(advance_by)

        return self.stop

    def is_on_targetted_node(self, advance_by):
        return self.target.line == self.current.line \
            and self.target.column >= self.current.column \
            and self.target.column <  self.current.column + advance_by


class BoundingBox(RenderWalker):
    """Compute the bounding box of the given node.

    Top-left position is always (1,1). Walk the whole node while
    incrementing the position and at the end store previous position as
    the bottom-right position.
    """
    def compute(self, tree, target_path = None):
        self.current_position = Position(1, 1)
        self.left_of_current_position = Position(1, 0)
        self.stop = self.CONTINUE

        left = Position(1,1)
        self.walk(tree)
        right = self.left_of_current_position
        return ((left.line, left.column), (right.line, right.column))

    def on_leaf(self, constant, pos, key):
        newlines_split = split_on_newlines(constant)

        for c in newlines_split:
            if c == "\n":
                self.current_position.advance_line()
            elif c != "":
                self.current_position.advance_columns(len(c))
                self.left_of_current_position = self.current_position.left()

        return self.stop


def split_on_newlines(constant):
    return ["\n"] if constant == "\n" else intersperce(constant.split("\n"), "\n")


# Stolen shamelessly from http://stackoverflow.com/a/5656097/1013628
def intersperce(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def advance_columns(self, columns):
        self.column += columns

    def advance_line(self):
        self.line += 1
        self.column = 1

    def left(self):
        return Position(self.line, self.column - 1)

