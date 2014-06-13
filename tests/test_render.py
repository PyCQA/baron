import pytest
from baron import parse
from baron.render import render, node_types, nodes_rendering_order, RenderWalker


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


def test_render_dictionnary_bad_type():
    nodes_rendering_order['bad_type'] = [('wtf', 'hello', True)]
    with pytest.raises(NotImplementedError) as e:
        list(render({'type': 'bad_type'}))
    assert str(e.value) == "Unknown key type \"wtf\" in \"bad_type\" node"


def test_render_dictionnary_bad_bool_dependency():
    nodes_rendering_order['bad_bool_dependency'] = [('bool', True, True)]
    with pytest.raises(NotImplementedError) as e:
        list(render({'type': 'bad_bool_dependency'}))
    assert str(e.value) == "Bool keys are only used for dependency, they cannot be rendered. Please set the \"('bool', True, True)\"'s dependent key in \"bad_bool_dependency\" node to False"


def test_render_dictionnary_bad_bool_dependency2():
    nodes_rendering_order['bad_bool_dependency2'] = [('bool', False, 'other_key')]
    with pytest.raises(NotImplementedError) as e:
        list(render({'type': 'bad_bool_dependency2'}))
    assert str(e.value) == "Bool keys are only used for dependency, they cannot be rendered. Please set the \"('bool', False, 'other_key')\"'s dependent key in \"bad_bool_dependency2\" node to False"


class RenderWalkerTester(RenderWalker):
    def __init__(self, steps):
        self.steps = steps

    def before(self, *args):
        super(RenderWalkerTester, self).before(*args)
        return self.process_test('>', *args)

    def after(self, *args):
        stop = self.process_test('<', *args)
        super(RenderWalkerTester, self).after(*args)
        return stop

    def process_test(self, direction, node_type, node, render_pos, render_key):
        _direction, _node_type, _node, _render_pos, _render_key, _stop = self.steps.pop(0)
        assert _direction == direction
        assert _node_type == node_type
        if node_type == 'constant':
            assert _node == node
        elif "type" in node:
            assert _node == node["type"]
        else:
            assert _node == node.__class__.__name__
        assert _render_pos == render_pos
        assert _render_key == render_key
        return _stop


def test_walk_stop():
    node = parse("a = 1")
    walker = RenderWalkerTester([
    ('>', 'node', 'assignment', 0, 0, False),
        ('>', 'key', 'name', 0, 'target', False),
            ('>', 'constant', 'a', 0, 'value', True),
        ('<', 'key', 'name', 0, 'target', False),
    ('<', 'node', 'assignment', 0, 0, False),
    ])

    walker.walk(node)


def test_walk_assignment():
    node = parse("a = 1")
    walker = RenderWalkerTester([
    ('>', 'node', 'assignment', 0, 0, False),
        ('>', 'key', 'name', 0, 'target', False),
            ('>', 'constant', 'a', 0, 'value', False),
            ('<', 'constant', 'a', 0, 'value', False),
        ('<', 'key', 'name', 0, 'target', False),
        ('>', 'formatting', 'list', 1, 'first_formatting', False),
            ('>', 'node', 'space', 0, 0, False),
                ('>', 'constant', ' ', 0, 'value', False),
                ('<', 'constant', ' ', 0, 'value', False),
            ('<', 'node', 'space', 0, 0, False),
        ('<', 'formatting', 'list', 1, 'first_formatting', False),
        ('>', 'constant', '=', 3, None, False),
        ('<', 'constant', '=', 3, None, False),
        ('>', 'formatting', 'list', 4, 'second_formatting', False),
            ('>', 'node', 'space', 0, 0, False),
                ('>', 'constant', ' ', 0, 'value', False),
                ('<', 'constant', ' ', 0, 'value', False),
            ('<', 'node', 'space', 0, 0, False),
        ('<', 'formatting', 'list', 4, 'second_formatting', False),
        ('>', 'key', 'int', 5, 'value', False),
            ('>', 'constant', '1', 0, 'value', False),
            ('<', 'constant', '1', 0, 'value', False),
        ('<', 'key', 'int', 5, 'value', False),
    ('<', 'node', 'assignment', 0, 0, False),
    ])

    walker.walk(node)


def test_walk_funcdef_with_leading_space():
    node = parse("""\

@deco
def fun(arg1):
    pass
""")
    walker = RenderWalkerTester([
    ('>', 'node', 'endl', 0, 0, False),
        ('>', 'constant', '\n', 1, 'value', False),
        ('<', 'constant', '\n', 1, 'value', False),
        ('>', 'constant', '', 2, 'indent', False),
        ('<', 'constant', '', 2, 'indent', False),
    ('<', 'node', 'endl', 0, 0, False),
    ('>', 'node', 'funcdef', 1, 1, False),
        ('>', 'list', 'list', 0, 'decorators', False),
            ('>', 'node', 'decorator', 0, 0, False),
                ('>', 'constant', '@', 0, None, False),
                ('<', 'constant', '@', 0, None, False),
                ('>', 'key', 'dotted_name', 1, 'value', False),
                    ('>', 'list', 'list', 0, 'value', False),
                        ('>', 'node', 'name', 0, 0, False),
                            ('>', 'constant', 'deco', 0, 'value', False),
                            ('<', 'constant', 'deco', 0, 'value', False),
                        ('<', 'node', 'name', 0, 0, False),
                    ('<', 'list', 'list', 0, 'value', False),
                ('<', 'key', 'dotted_name', 1, 'value', False),
            ('<', 'node', 'decorator', 0, 0, False),
            ('>', 'node', 'endl', 1, 1, False),
                ('>', 'constant', '\n', 1, 'value', False),
                ('<', 'constant', '\n', 1, 'value', False),
                ('>', 'constant', '', 2, 'indent', False),
                ('<', 'constant', '', 2, 'indent', False),
            ('<', 'node', 'endl', 1, 1, False),
        ('<', 'list', 'list', 0, 'decorators', False),
        ('>', 'constant', 'def', 1, None, False),
        ('<', 'constant', 'def', 1, None, False),
        ('>', 'formatting', 'list', 2, 'first_formatting', False),
            ('>', 'node', 'space', 0, 0, False),
                ('>', 'constant', ' ', 0, 'value', False),
                ('<', 'constant', ' ', 0, 'value', False),
            ('<', 'node', 'space', 0, 0, False),
        ('<', 'formatting', 'list', 2, 'first_formatting', False),
        ('>', 'constant', 'fun', 3, 'name', False),
        ('<', 'constant', 'fun', 3, 'name', False),
        ('>', 'constant', '(', 5, None, False),
        ('<', 'constant', '(', 5, None, False),
        ('>', 'list', 'list', 7, 'arguments', False),
            ('>', 'node', 'def_argument', 0, 0, False),
                ('>', 'constant', 'arg1', 0, 'name', False),
                ('<', 'constant', 'arg1', 0, 'name', False),
            ('<', 'node', 'def_argument', 0, 0, False),
        ('<', 'list', 'list', 7, 'arguments', False),
        ('>', 'constant', ')', 9, None, False),
        ('<', 'constant', ')', 9, None, False),
        ('>', 'constant', ':', 11, None, False),
        ('<', 'constant', ':', 11, None, False),
        ('>', 'list', 'list', 13, 'value', False),
            ('>', 'node', 'endl', 0, 0, False),
                ('>', 'constant', '\n', 1, 'value', False),
                ('<', 'constant', '\n', 1, 'value', False),
                ('>', 'constant', '    ', 2, 'indent', False),
                ('<', 'constant', '    ', 2, 'indent', False),
            ('<', 'node', 'endl', 0, 0, False),
            ('>', 'node', 'pass', 1, 1, False),
                ('>', 'constant', 'pass', 0, 'type', False),
                ('<', 'constant', 'pass', 0, 'type', False),
            ('<', 'node', 'pass', 1, 1, False),
            ('>', 'node', 'endl', 2, 2, False),
                ('>', 'constant', '\n', 1, 'value', False),
                ('<', 'constant', '\n', 1, 'value', False),
                ('>', 'constant', '', 2, 'indent', False),
                ('<', 'constant', '', 2, 'indent', False),
            ('<', 'node', 'endl', 2, 2, False),
        ('<', 'list', 'list', 13, 'value', False),
    ('<', 'node', 'funcdef', 1, 1, False),
    ])

    walker.walk(node)

