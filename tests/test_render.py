import pytest
from baron.render import node_types, rendering_dictionnary


@pytest.fixture(params=rendering_dictionnary.keys())
def dictionnary_node(request):
    return {'key': request.param, 'value': rendering_dictionnary[request.param]}


def test_dictionnary_key_validity(dictionnary_node):
    for key_type, render_key, dependent in dictionnary_node['value']:
        assert key_type in node_types


def test_dictionnary_dependent_validity(dictionnary_node):
    for key_type, render_key, dependent in dictionnary_node['value']:
        assert dependent == True \
            or isinstance(dependent, str) \
            or (isinstance(dependent, list) and all([isinstance(d, str) for d in dependent]))
