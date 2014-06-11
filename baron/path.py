from .render import RenderWalker, render
from .utils import string_instance, is_newline, split_on_newlines
from collections import namedtuple
from copy import deepcopy


def position_to_path(tree, line, column):
    """Path to the node located at the given line and column

    This function locates a node in the rendered source code
    """
    return PositionFinder().find(tree, line, column)


def path_to_node(tree, path):
    """FST node located at the given path"""
    if path is None:
        return None
    node = tree
    for key in path.path:
        if not isinstance(node[key], string_instance):
            node = node[key]
    return node


def position_to_node(tree, line, column):
    """FST node located at the given line and column"""
    return path_to_node(tree, position_to_path(tree, line, column))


def node_to_bounding_box(node):
    """Bounding box of the given node

    The bounding box of a node represents its left most and right most
    position in the rendered source code. Its left position is here
    always (1, 1).
    """
    return BoundingBox().compute(node)


def path_to_bounding_box(tree, path):
    """Absolute bounding box of the node located at the given path"""
    return BoundingBox().compute(tree, path)


def make_path(path=None, node_type=None, position_in_rendering_list=None):
    return namedtuple('Path', ['path', 'node_type', 'position_in_rendering_list'])._make([
        [] if path is None else deepcopy(path),
        deepcopy(node_type),
        deepcopy(position_in_rendering_list)
    ])


def is_empty(path):
    return path.path == [] and path.node_type is None and path.position_in_rendering_list is None


def make_position(line, column):
    return Position(line, column)


class Position(object):
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

    def __eq__(self, other):
        if isinstance(other, tuple) or isinstance(other, list):
            try:
                return self.line == other[0] and self.column == other[1]
            except IndexError:
                return False

        try:
            return self.line == other.line and self.column == other.column
        except AttributeError:
            return False

    def __repr__(self):
        return 'Position (%s, %s)' % (str(self.line), str(self.column))


def make_bounding_box(top_left=None, bottom_right=None):
    return namedtuple("BoundingBox", ["top_left", "bottom_right"])._make([
            deepcopy(top_left),
            deepcopy(bottom_right)
        ])


class PathWalker(RenderWalker):
    def walk(self, tree):
        self.current_path = []
        self.current_node_type = None
        self.current_position_in_rendering_list = None

        super(PathWalker, self).walk(tree)

    def current_decorated_path(self):
        return make_path(self.current_path, self.current_node_type, self.current_position_in_rendering_list)

    def _walk(self, node):
        for key_type, item, render_pos, render_key in render(node):
            if render_key is not None:
                self.current_path.append(render_key)
            if key_type != 'constant':
                old_type = self.current_node_type
                self.current_node_type = item["type"] if "type" in item else key_type
            old_pos = self.current_position_in_rendering_list
            self.current_position_in_rendering_list = render_pos

            stop = self._walk_on_item(key_type, item, render_pos, render_key)

            if render_key is not None:
                self.current_path.pop()
            if key_type != 'constant':
                self.current_node_type = old_type
            self.current_position_in_rendering_list = old_pos

            if stop:
                return self.STOP


class PositionFinder(PathWalker):
    """Find a node by line and column and return the path to it.

    First, walk through all the nodes while maintaining the current line
    and column. When the targetted node is found, stop there and build
    the path while going back up the tree.
    """
    def find(self, tree, line, column):
        self.current = make_position(1, 1)
        self.target = make_position(line, column)
        self.found_path = None

        self.walk(tree)
        return self.found_path

    def on_leaf(self, constant, pos, key):
        """Determine if we're on the targetted node.

        If the targetted column is reached, `stop` and `path_found` are
        set. If the targetted line is passed, only `stop` is set. This
        prevents unnecessary tree travelling when the targetted column
        is out of bounds.
        """
        newlines_split = split_on_newlines(constant)

        for c in newlines_split:
            if is_newline(c):
                self.current.advance_line()
                # if target line is passed
                if self.current.line > self.target.line:
                    return self.STOP

            else:
                advance_by = len(c)
                if self.is_on_targetted_node(advance_by):
                    self.found_path = self.current_decorated_path()
                    return self.STOP
                self.current.advance_columns(advance_by)

    def is_on_targetted_node(self, advance_by):
        return self.target.line == self.current.line \
            and self.target.column >= self.current.column \
            and self.target.column < self.current.column + advance_by


class BoundingBox(PathWalker):
    """Compute the bounding box of the given node.

    First, walk to the target path while incrementing the position.
    When reached, the top-left position is set to the current position.
    Then walk the whole node, still incrementing the position. When
    arriving at the end of the node, store the previous position, not
    the current one, as the bottom-right position.
    If no target path is given, assume the targetted node is the whole
    tree.
    """
    def compute(self, tree, target_path=None):
        self.target_path = target_path
        self.current_position = make_position(1, 1)
        self.left_of_current_position = make_position(1, 0)
        self.top_left = None
        self.bottom_right = None
        self.found = True if self.target_path is None else False

        self.walk(tree)

        if self.found and self.top_left is None and self.bottom_right is None:
            return make_bounding_box(make_position(1, 1), self.left_of_current_position)

        return make_bounding_box(self.top_left, self.bottom_right)

    def on_leaf(self, constant, pos, key):
        if self.current_decorated_path() == self.target_path:
            self.found = True
            self.top_left = deepcopy(self.current_position)

        newlines_split = split_on_newlines(constant)

        for c in newlines_split:
            if is_newline(c):
                self.current_position.advance_line()
            elif c != "":
                self.current_position.advance_columns(len(c))
                self.left_of_current_position = self.current_position.left()

        if self.bottom_right is None and self.found and self.current_decorated_path() == self.target_path:
            self.bottom_right = deepcopy(self.left_of_current_position)
            return self.STOP

