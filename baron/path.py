from .render import RenderWalker, child_by_key
from .utils import is_newline, split_on_newlines
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

    for key in path:
        node = child_by_key(node, key)

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


def make_position(line, column):
    return Position(line, column)


class Position(object):
    """Handles a cursor's line and column

    Operations requiring another Position as argument can be given
    a tuple instead for convenience.
    """
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def advance_columns(self, columns):
        """(3, 10) -> (3, 11)"""
        self.column += columns

    def advance_line(self):
        """(3, 10) -> (4, 1)"""
        self.line += 1
        self.column = 1

    def left(self):
        """(3, 10) -> (3, 9)"""
        return Position(self.line, self.column - 1)

    def __add__(self, other):
        """(1, 1) + (1, 1) -> (2, 2)"""
        if isinstance(other, Position):
            return Position(self.line + other.line,
                    self.column + other.column)
        else:
            return Position(self.line + other[0],
                    self.column + other[1])

    def __neg__(self):
        """(1, -1) -> (-1, 1)"""
        return Position(-self.line, -self.column)

    def __sub__(self, other):
        """(1, 1) - (1, 1) -> (0, 0)"""
        if isinstance(other, Position):
            return Position(self.line - other.line,
                    self.column - other.column)
        else:
            return Position(self.line - other[0],
                    self.column - other[1])

    def __eq__(self, other):
        """Compares Positions or Position and tuple"""
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

    def to_tuple(self):
        return (self.line, self.column)

    @classmethod
    def from_tuple(class_, tup):
        return class_(tup[0], tup[1])


def make_bounding_box(top_left=None, bottom_right=None):
    return namedtuple("BoundingBox", ["top_left", "bottom_right"])._make([
            deepcopy(top_left),
            deepcopy(bottom_right)
        ])


class PathWalker(RenderWalker):
    """Gives the current path while walking the rendered tree

    It adds an attribute "current_path" which is updated each time the
    walker takes a step.
    """
    def walk(self, tree):
        self.current_path = []

        super(PathWalker, self).walk(tree)

    def before(self, key_type, item, render_key):
        if render_key is not None:
            self.current_path.append(render_key)

        return super(PathWalker, self).before(key_type, item, render_key)

    def after(self, key_type, item, render_key):
        stop = super(PathWalker, self).after(key_type, item, render_key)

        if render_key is not None:
            self.current_path.pop()

        return stop


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

    def before_leaf(self, constant, key):
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
                    self.found_path = deepcopy(self.current_path)
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
        self.found = True if self.target_path is None or len(target_path) == 0 else False

        self.walk(tree)

        if self.found and self.top_left is None and self.bottom_right is None:
            return make_bounding_box(make_position(1, 1), self.left_of_current_position)

        return make_bounding_box(self.top_left, self.bottom_right)

    def before(self, key_type, item, render_key):
        stop = super(BoundingBox, self).before(key_type, item, render_key)

        if self.current_path == self.target_path:
            self.found = True
            self.top_left = deepcopy(self.current_position)

        if key_type != 'constant':
            return stop

        newlines_split = split_on_newlines(item)

        for c in newlines_split:
            if is_newline(c):
                self.current_position.advance_line()
            elif c != "":
                self.current_position.advance_columns(len(c))
                self.left_of_current_position = self.current_position.left()

        return stop

    def after(self, key_type, item, render_key):
        if self.bottom_right is None and self.found and self.current_path == self.target_path:
            self.bottom_right = deepcopy(self.left_of_current_position)

        return super(BoundingBox, self).after(key_type, item, render_key)
