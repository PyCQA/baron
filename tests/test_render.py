import pytest
from baron.render import node_types, nodes_rendering_order


@pytest.fixture(params=nodes_rendering_order.keys())
def dictionnary_node(request):
    return nodes_rendering_order[request.param]


def test_dictionnary_key_validity(dictionnary_node):
    for key_type, render_key, dependent in dictionnary_node:
        assert key_type in node_types


def test_dictionnary_dependent_validity(dictionnary_node):
    for key_type, render_key, dependent in dictionnary_node:
        assert dependent == True \
            or isinstance(dependent, str) \
            or (isinstance(dependent, list) and all([isinstance(d, str) for d in dependent]))
