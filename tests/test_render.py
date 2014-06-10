import pytest
from baron import parse
from baron.render import node_types, nodes_rendering_order, RenderWalker


@pytest.fixture(params=nodes_rendering_order.keys())
def dictionnary_node(request):
    return nodes_rendering_order[request.param]


def test_dictionnary_key_validity(dictionnary_node):
    for key_type, render_key, dependent in dictionnary_node:
        assert key_type in node_types


def test_dictionnary_dependent_validity(dictionnary_node):
    keys = set([t[1] for t in dictionnary_node])
    for key_type, render_key, dependent in dictionnary_node:
        assert isinstance(dependent, bool) \
            or (isinstance(dependent, str) and dependent in keys) \
            or (isinstance(dependent, list) and all([d in keys for d in dependent]))

        if key_type == 'bool':
            assert dependent is False


class RenderWalkerTester(RenderWalker):
    def __init__(self, steps):
        self.steps = steps

    def before(self, *args):
        self.process_test('>', *args)

    def after(self, *args):
        self.process_test('<', *args)

    def on_leaf(self, node, render_pos, render_key):
        _node_type, _node, _render_pos, _render_key = self.steps.pop(0)
        assert _node_type == 'constant'
        assert _node == node
        assert _render_pos == render_pos
        assert _render_key == render_key

    def process_test(self, direction, node_type, node, render_pos, render_key):
        _direction, _node_type, _node, _render_pos, _render_key = self.steps.pop(0)
        assert _direction == direction
        assert _node_type == node_type
        if "type" in node:
            assert _node == node["type"]
        else:
            assert _node == node.__class__.__name__
        assert _render_pos == render_pos
        assert _render_key == render_key


def test_walk_assignment():
    node = parse("a = 1")
    walker = RenderWalkerTester([
    ('>', 'node', 'assignment', 0, 0),
        ('>', 'key', 'name', 0, 'target'),
            ('constant', 'a', 0, 'value'),
        ('<', 'key', 'name', 0, 'target'),
        ('>', 'formatting', 'list', 1, 'first_formatting'),
            ('>', 'node', 'space', 0, 0),
                ('constant', ' ', 0, 'value'),
            ('<', 'node', 'space', 0, 0),
        ('<', 'formatting', 'list', 1, 'first_formatting'),
        ('constant', '=', 3, None),
        ('>', 'formatting', 'list', 4, 'second_formatting'),
            ('>', 'node', 'space', 0, 0),
                ('constant', ' ', 0, 'value'),
            ('<', 'node', 'space', 0, 0),
        ('<', 'formatting', 'list', 4, 'second_formatting'),
        ('>', 'key', 'int', 5, 'value'),
            ('constant', '1', 0, 'value'),
        ('<', 'key', 'int', 5, 'value'),
    ('<', 'node', 'assignment', 0, 0),
    ])

    walker.walk(node)


def test_walk_funcdef_with_leading_space():
    node = parse("""\

@deco
def fun(arg1):
    pass
""")
    walker = RenderWalkerTester([
    ('>', 'node', 'endl', 0, 0),
        ('constant', '\n', 1, 'value'),
        ('constant', '', 2, 'indent'),
    ('<', 'node', 'endl', 0, 0),
    ('>', 'node', 'funcdef', 1, 1),
        ('>', 'list', 'list', 0, 'decorators'),
            ('>', 'node', 'decorator', 0, 0),
                ('constant', '@', 0, None),
                ('>', 'key', 'dotted_name', 1, 'value'),
                    ('>', 'list', 'list', 0, 'value'),
                        ('>', 'node', 'name', 0, 0),
                            ('constant', 'deco', 0, 'value'),
                        ('<', 'node', 'name', 0, 0),
                    ('<', 'list', 'list', 0, 'value'),
                ('<', 'key', 'dotted_name', 1, 'value'),
            ('<', 'node', 'decorator', 0, 0),
            ('>', 'node', 'endl', 1, 1),
                ('constant', '\n', 1, 'value'),
                ('constant', '', 2, 'indent'),
            ('<', 'node', 'endl', 1, 1),
        ('<', 'list', 'list', 0, 'decorators'),
        ('constant', 'def', 1, None),
        ('>', 'formatting', 'list', 2, 'first_formatting'),
            ('>', 'node', 'space', 0, 0),
                ('constant', ' ', 0, 'value'),
            ('<', 'node', 'space', 0, 0),
        ('<', 'formatting', 'list', 2, 'first_formatting'),
        ('constant', 'fun', 3, 'name'),
        ('constant', '(', 5, None),
        ('>', 'list', 'list', 7, 'arguments'),
            ('>', 'node', 'def_argument', 0, 0),
                ('constant', 'arg1', 0, 'name'),
            ('<', 'node', 'def_argument', 0, 0),
        ('<', 'list', 'list', 7, 'arguments'),
        ('constant', ')', 9, None),
        ('constant', ':', 11, None),
        ('>', 'list', 'list', 13, 'value'),
            ('>', 'node', 'endl', 0, 0),
                ('constant', '\n', 1, 'value'),
                ('constant', '    ', 2, 'indent'),
            ('<', 'node', 'endl', 0, 0),
            ('>', 'node', 'pass', 1, 1),
                ('constant', 'pass', 0, 'type'),
            ('<', 'node', 'pass', 1, 1),
            ('>', 'node', 'endl', 2, 2),
                ('constant', '\n', 1, 'value'),
                ('constant', '', 2, 'indent'),
            ('<', 'node', 'endl', 2, 2),
        ('<', 'list', 'list', 13, 'value'),
    ('<', 'node', 'funcdef', 1, 1),
    ])

    walker.walk(node)

