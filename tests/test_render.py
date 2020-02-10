import pytest
from baron import parse
from baron.render import render, node_types, nodes_rendering_order, RenderWalker


@pytest.fixture(params=nodes_rendering_order.keys())
def dictionnary_node(request):
    return nodes_rendering_order[request.param]


def test_render_crap():
    with pytest.raises(NotImplementedError):
        render("crap")


def test_dictionnary_key_validity(dictionnary_node):
    for key_type, _, _ in dictionnary_node:
        assert key_type in node_types


def test_dictionnary_dependent_validity(dictionnary_node):
    keys = set([t[1] for t in dictionnary_node])
    for key_type, _, dependent in dictionnary_node:
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
        super(RenderWalkerTester, self).__init__(strict=True)
        self.steps = steps

    def before(self, *args):
        super(RenderWalkerTester, self).before(*args)
        return self.process_test('>', *args)

    def after(self, *args):
        stop = self.process_test('<', *args)
        super(RenderWalkerTester, self).after(*args)
        return stop

    def process_test(self, direction, node_type, node, render_key):
        _direction, _node_type, _node, _render_key, _stop = self.steps.pop(0)
        target = (_direction, _node_type, _node, _render_key)
        if node_type in ['constant', 'string']:
            assert target == (direction, node_type, node, render_key)
        elif "type" in node:
            assert target == (direction, node_type, node["type"], render_key)
        else:
            assert target == (direction, node_type, node.__class__.__name__, render_key)
        return _stop


# flake8: noqa
def test_walk_stop():
    node = parse("a = 1")
    walker = RenderWalkerTester([
    ('>', 'node', 'assignment', 0, False),
        ('>', 'key', 'name', 'target', False),
            ('>', 'string', 'a', 'value', True),
        ('<', 'key', 'name', 'target', False),
    ('<', 'node', 'assignment', 0, False),
    ])

    walker.walk(node)


def test_walk_assignment():
    node = parse("a = 1")
    walker = RenderWalkerTester([
    ('>', 'node', 'assignment', 0, False),
        ('>', 'key', 'name', 'target', False),
            ('>', 'string', 'a', 'value', False),
            ('<', 'string', 'a', 'value', False),
        ('<', 'key', 'name', 'target', False),
        ('>', 'formatting', 'list', 'first_formatting', False),
            ('>', 'node', 'space', 0, False),
                ('>', 'string', ' ', 'value', False),
                ('<', 'string', ' ', 'value', False),
            ('<', 'node', 'space', 0, False),
        ('<', 'formatting', 'list', 'first_formatting', False),
        ('>', 'constant', '=', '=', False),
        ('<', 'constant', '=', '=', False),
        ('>', 'formatting', 'list', 'second_formatting', False),
            ('>', 'node', 'space', 0, False),
                ('>', 'string', ' ', 'value', False),
                ('<', 'string', ' ', 'value', False),
            ('<', 'node', 'space', 0, False),
        ('<', 'formatting', 'list', 'second_formatting', False),
        ('>', 'key', 'int', 'value', False),
            ('>', 'string', '1', 'value', False),
            ('<', 'string', '1', 'value', False),
        ('<', 'key', 'int', 'value', False),
    ('<', 'node', 'assignment', 0, False),
    ])

    walker.walk(node)


def test_walk_funcdef_with_leading_space():
    node = parse("""\

@deco
def fun(arg1):
    pass
""")
    walker = RenderWalkerTester([
    ('>', 'node', 'endl', 0, False),
        ('>', 'formatting', 'list', 'formatting', False),
        ('<', 'formatting', 'list', 'formatting', False),
        ('>', 'string', '\n', 'value', False),
        ('<', 'string', '\n', 'value', False),
        ('>', 'string', '', 'indent', False),
        ('<', 'string', '', 'indent', False),
    ('<', 'node', 'endl', 0, False),
    ('>', 'node', 'def', 1, False),
        ('>', 'list', 'list', 'decorators', False),
            ('>', 'node', 'decorator', 0, False),
                ('>', 'constant', '@', '@', False),
                ('<', 'constant', '@', '@', False),
                ('>', 'key', 'dotted_name', 'value', False),
                    ('>', 'list', 'list', 'value', False),
                        ('>', 'node', 'name', 0, False),
                            ('>', 'string', 'deco', 'value', False),
                            ('<', 'string', 'deco', 'value', False),
                        ('<', 'node', 'name', 0, False),
                    ('<', 'list', 'list', 'value', False),
                ('<', 'key', 'dotted_name', 'value', False),
            ('<', 'node', 'decorator', 0, False),
            ('>', 'node', 'endl', 1, False),
                ('>', 'formatting', 'list', 'formatting', False),
                ('<', 'formatting', 'list', 'formatting', False),
                ('>', 'string', '\n', 'value', False),
                ('<', 'string', '\n', 'value', False),
                ('>', 'string', '', 'indent', False),
                ('<', 'string', '', 'indent', False),
            ('<', 'node', 'endl', 1, False),
        ('<', 'list', 'list', 'decorators', False),
        ('>', 'constant', 'def', 'def', False),
        ('<', 'constant', 'def', 'def', False),
        ('>', 'formatting', 'list', 'first_formatting', False),
            ('>', 'node', 'space', 0, False),
                ('>', 'string', ' ', 'value', False),
                ('<', 'string', ' ', 'value', False),
            ('<', 'node', 'space', 0, False),
        ('<', 'formatting', 'list', 'first_formatting', False),
        ('>', 'string', 'fun', 'name', False),
        ('<', 'string', 'fun', 'name', False),
        ('>', 'formatting', 'list', 'second_formatting', False),
        ('<', 'formatting', 'list', 'second_formatting', False),
        ('>', 'constant', '(', '(', False),
        ('<', 'constant', '(', '(', False),
        ('>', 'formatting', 'list', 'third_formatting', False),
        ('<', 'formatting', 'list', 'third_formatting', False),
        ('>', 'list', 'list', 'arguments', False),
            ('>', 'node', 'def_argument', 0, False),
                ('>', 'key', 'name', 'target', False),
                    ('>', 'string', 'arg1', 'value', False),
                    ('<', 'string', 'arg1', 'value', False),
                ('<', 'key', 'name', 'target', False),
            ('<', 'node', 'def_argument', 0, False),
        ('<', 'list', 'list', 'arguments', False),
        ('>', 'formatting', 'list', 'fourth_formatting', False),
        ('<', 'formatting', 'list', 'fourth_formatting', False),
        ('>', 'constant', ')', ')', False),
        ('<', 'constant', ')', ')', False),
        ('>', 'formatting', 'list', 'fifth_formatting', False),
        ('<', 'formatting', 'list', 'fifth_formatting', False),
        ('>', 'constant', ':', ':', False),
        ('<', 'constant', ':', ':', False),
        ('>', 'formatting', 'list', 'sixth_formatting', False),
        ('<', 'formatting', 'list', 'sixth_formatting', False),
        ('>', 'list', 'list', 'value', False),
            ('>', 'node', 'endl', 0, False),
                ('>', 'formatting', 'list', 'formatting', False),
                ('<', 'formatting', 'list', 'formatting', False),
                ('>', 'string', '\n', 'value', False),
                ('<', 'string', '\n', 'value', False),
                ('>', 'string', '    ', 'indent', False),
                ('<', 'string', '    ', 'indent', False),
            ('<', 'node', 'endl', 0, False),
            ('>', 'node', 'pass', 1, False),
                ('>', 'string', 'pass', 'type', False),
                ('<', 'string', 'pass', 'type', False),
            ('<', 'node', 'pass', 1, False),
            ('>', 'node', 'endl', 2, False),
                ('>', 'formatting', 'list', 'formatting', False),
                ('<', 'formatting', 'list', 'formatting', False),
                ('>', 'string', '\n', 'value', False),
                ('<', 'string', '\n', 'value', False),
                ('>', 'string', '', 'indent', False),
                ('<', 'string', '', 'indent', False),
            ('<', 'node', 'endl', 2, False),
        ('<', 'list', 'list', 'value', False),
    ('<', 'node', 'def', 1, False),
    ])

    walker.walk(node)
