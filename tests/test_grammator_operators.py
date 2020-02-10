#!/usr/bin/python
# -*- coding:Utf-8 -*-
import pytest
from baron.parser import ParsingError
from .test_utils import parse_simple


def test_simple_power():
    "a**b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_first_space_power():
    "a  **b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', '  ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": "  "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', '  ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": "  "}],
            "second_formatting": []
        }
    ])


def test_second_space_power():
    "a** b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_spaces_power():
    "a **  b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_power():
    "a **  b   **    c"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {"type": "name", "value": 'a'},
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {"type": "name", "value": 'b'},
                "second": {"type": "name", "value": 'c', },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_power_spaces():
    "a**  b   **    c"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {"type": "name", "value": 'b'},
                "second": {"type": "name", "value": 'c'},
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {"type": "name", "value": 'a'},
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {"type": "name", "value": 'b', },
                "second": {"type": "name", "value": 'c'},
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {"type": "name", "value": 'a'},
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    "a **b   **    c"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": "   "}],
                "second_formatting": [{"type": "space", "value": "    "}]
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    "a**b**c"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {"type": "name", "value": 'a'},
            "second": {
                "type": "binary_operator",
                "value": '**',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_power_factor():
    "a **  +b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('PLUS', '+'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '+',
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('PLUS', '+'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '+',
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_factor_minus():
    "a **  -b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '-',
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '-',
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_factor_tild():
    "a **  ~b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_operator_madness():
    "a **  ~+-b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b'
                        },
                        "formatting": [],
                    },
                    "formatting": [],
                },
                "formatting": []
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b',
                        },
                        "formatting": [],
                    },
                    "formatting": [],
                },
                "formatting": []
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b'
                        },
                        "formatting": [],
                    },
                    "formatting": []
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        (
            'NAME',
            'a'
        ),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b',
                        },
                        "formatting": [],
                    },
                    "formatting": []
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        (
            'NAME',
            'a'
        ),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": "~",
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b'
                        },
                        "formatting": []
                    },
                    "formatting": [],
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~'),
        ('PLUS', '+'),
        ('MINUS', '-'),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": "~",
                "target": {
                    "type": "unitary_operator",
                    "value": '+',
                    "target": {
                        "type": "unitary_operator",
                        "value": "-",
                        "target": {
                            "type": "name",
                            "value": 'b',
                        },
                        "formatting": []
                    },
                    "formatting": [],
                },
                "formatting": [],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_factor_tild_space():
    "a **  ~ b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_STAR', '**', [('SPACE', ' ')], [('SPACE', '  ')]),
        ('TILDE', '~', [], [('SPACE', ' ')]),
        ('NAME', 'b')
    ], [
        {
            "type": "binary_operator",
            "value": '**',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "unitary_operator",
                "value": '~',
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": "  "}]
        }
    ])


def test_power_trailer():
    "a.b"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
        }
    ])


def test_power_trailer_spaces():
    "a .b"
    "a.  b"
    "a  .   b"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
        }
    ])

    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": "  "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
        }
    ])

    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', '   ')], [('SPACE', '    ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [{"type": "space", "value": "   "}],
                    "second_formatting": [{"type": "space", "value": "    "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
            ],
        }
    ])


def test_power_trailers():
    "a.b.c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "c",
                },
            ],
        }
    ])
    "a.b.c.d.e"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOT', '.'),
        ('NAME', 'c'),
        ('DOT', '.'),
        ('NAME', 'd'),
        ('DOT', '.'),
        ('NAME', 'e'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "c",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "d",
                },
                {
                    "type": "dot",
                    "first_formatting": [],
                    "second_formatting": [],
                },
                {
                    "type": "name",
                    "value": "e",
                },
            ],
        }
    ])


def test_power_trailers_space():
    "a . b . c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('DOT', '.', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "dot",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "dot",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "c",
                },
            ],
        }
    ])


def test_power_trailer_power():
    "a.b**c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": "**",
            "first_formatting": [],
            "second_formatting": [],
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": "c",
            }
        }
    ])


def test_term_mult():
    "a*b"
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_term_mult_first_space():
    "a *b"
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_term_mult_second_space():
    "a* b"
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_mult_spaces():
    "a * b"
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('STAR', '*', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_mult_spaces_atomtrailers():
    "a.b * c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('STAR', '*', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '*',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_div():
    "a/b"
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_term_div_first_space():
    "a /b"
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_term_div_second_space():
    "a/ b"
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_div_spaces():
    "a / b"
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_div_spaces_atomtrailers():
    "a.b / c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('SLASH', '/', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_modulo():
    "a%b"
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_term_modulo_first_space():
    "a %b"
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_term_modulo_second_space():
    "a% b"
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_modulo_spaces():
    "a % b"
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PERCENT', '%', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_modulo_spaces_atomtrailers():
    "a.b % c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('PERCENT', '%', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '%',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_floor_division():
    "a//b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_term_floor_division_first_space():
    "a //b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_term_floor_division_second_space():
    "a// b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_floor_division_spaces():
    "a // b"
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_term_floor_division_spaces_atomtrailers():
    "a.b // c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('DOUBLE_SLASH', '//', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '//',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_combine_div_modulo_mult():
    "a/b%c*d"
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c",
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c",
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c",
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd',
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd',
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('SLASH', '/'),
        ('NAME', 'b'),
        ('PERCENT', '%'),
        ('NAME', 'c'),
        ('STAR', '*'),
        ('NAME', 'd'),
    ], [
        {
            "type": "binary_operator",
            "value": '/',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '%',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "binary_operator",
                    "value": '*',
                    "first": {
                        "type": "name",
                        "value": "c"
                    },
                    "second": {
                        "type": "name",
                        "value": 'd',
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                "first_formatting": [],
                "second_formatting": [],
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_arith_expr_plus():
    "a+b"
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_arith_expr_add_first_space():
    "a +b"
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_arith_expr_add_second_space():
    "a+ b"
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_add_spaces():
    "a + b"
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_add_spaces_atomtrailers():
    "a.b + c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('PLUS', '+', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_substract():
    "a-b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_arith_expr_substract_first_space():
    "a -b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_arith_expr_substract_second_space():
    "a- b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_substract_spaces():
    "a - b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_substract_spaces_atomtrailers():
    "a.b - c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_at():
    "a@b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_arith_expr_at_first_space():
    "a @b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_arith_expr_at_second_space():
    "a@ b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_at_spaces():
    "a @ b"
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('MINUS', '@', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '@',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_at_spaces_atomtrailers():
    "a.b - c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('MINUS', '-', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '-',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_chained_add_substract():
    "a+b-c"
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('PLUS', '+'),
        ('NAME', 'b'),
        ('MINUS', '-'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '+',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '-',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_arith_expr_left_shift():
    "a<<b"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_arith_expr_left_shift_first_space():
    "a <<b"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_arith_expr_left_shift_second_space():
    "a<< b"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_left_shift_spaces():
    "a << b"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_left_shift_spaces_atomtrailers():
    "a.b << c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('LEFT_SHIFT', '<<', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_right_shift():
    "a>>b"
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_arith_expr_right_shift_first_space():
    "a >>b"
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_arith_expr_right_shift_second_space():
    "a>> b"
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_right_shift_spaces():
    "a >> b"
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_arith_expr_right_shift_spaces_atomtrailers():
    "a.b >> c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '>>',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_chained_left_right_shift():
    "a<<b>>c"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SHIFT', '<<'),
        ('NAME', 'b'),
        ('RIGHT_SHIFT', '>>'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '<<',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '>>',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_and_expr():
    "a&b"
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_and_expr_first_space():
    "a &b"
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_and_expr_second_space():
    "a& b"
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_and_expr_spaces():
    "a & b"
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_and_expr_spaces_atomtrailers():
    "a.b & c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('AMPER', '&', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_chained_left_and_expr():
    "a&b&c"
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AMPER', '&'),
        ('NAME', 'b'),
        ('AMPER', '&'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '&',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '&',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_xor_expr():
    "a^b"
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_xor_expr_first_space():
    "a ^b"
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_xor_expr_second_space():
    "a^ b"
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_xor_expr_spaces():
    "a ^ b"
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_xor_expr_spaces_atomtrailers():
    "a.b ^ c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_chained_left_xor_expr():
    "a^b^c"
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'b'),
        ('CIRCUMFLEX', '^'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '^',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '^',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


def test_expr():
    "a|b"
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])


def test_expr_first_space():
    "a |b"
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": []
        }
    ])


def test_expr_second_space():
    "a| b"
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_expr_spaces():
    "a | b"
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_expr_spaces_atomtrailers():
    "a.b | c"
    parse_simple([
        ('NAME', 'a'),
        ('DOT', '.'),
        ('NAME', 'b'),
        ('VBAR', '|', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "atomtrailers",
                "value": [
                    {
                        "type": "name",
                        "value": "a",
                    },
                    {
                        "type": "dot",
                        "first_formatting": [],
                        "second_formatting": [],
                    },
                    {
                        "type": "name",
                        "value": "b",
                    }
                ],
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}]
        }
    ])


def test_chained_left_expr():
    "a|b|c"
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b",
                },
                "second": {
                    "type": "name",
                    "value": "c"
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": []
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('VBAR', '|'),
        ('NAME', 'b'),
        ('VBAR', '|'),
        ('NAME', 'c'),
    ], [
        {
            "type": "binary_operator",
            "value": '|',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "binary_operator",
                "value": '|',
                "first": {
                    "type": "name",
                    "value": "b"
                },
                "second": {
                    "type": "name",
                    "value": "c",
                },
                "first_formatting": [],
                "second_formatting": []
            },
            "first_formatting": [],
            "second_formatting": [],
        }
    ])


comparison_tokens = (
    ('LESS', '<'),
    ('GREATER', '>'),
    ('EQUAL_EQUAL', '=='),
    ('LESS_EQUAL', '<='),
    ('GREATER_EQUAL', '>='),
    ('NOT_EQUAL', '<>'),
    ('NOT_EQUAL', '!='),
    ('IN', 'in'),
    ('IS', 'is'),
)


def test_comparison():
    "a<b"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])


def test_comparison_first_space():
    "a <b"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
            }
        ])


def test_comparison_second_space():
    "a< b"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_comparison_spaces():
    "a < b"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_comparison_spaces_atomtrailers():
    "a.b < c"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            ('DOT', '.'),
            ('NAME', 'b'),
            (token_name, value, [('SPACE', ' ')], [('SPACE', ' ')]),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "atomtrailers",
                    "value": [
                        {
                            "type": "name",
                            "value": "a",
                        },
                        {
                            "type": "dot",
                            "first_formatting": [],
                            "second_formatting": [],
                        },
                        {
                            "type": "name",
                            "value": "b",
                        }
                    ],
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_chained_comparison():
    "a<b<c"
    for token_name, value in comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b"
                    },
                    "second": {
                        "type": "name",
                        "value": "c"
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b"
                    },
                    "second": {
                        "type": "name",
                        "value": "c"
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b",
                    },
                    "second": {
                        "type": "name",
                        "value": "c"
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b",
                    },
                    "second": {
                        "type": "name",
                        "value": "c"
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b"
                    },
                    "second": {
                        "type": "name",
                        "value": "c",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value),
            ('NAME', 'b'),
            (token_name, value),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": "",
                    "formatting": [],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": "",
                        "formatting": [],
                    },
                    "first": {
                        "type": "name",
                        "value": "b"
                    },
                    "second": {
                        "type": "name",
                        "value": "c",
                    },
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])


advanced_comparison_tokens = (
    (('NOT', 'not', [], [('SPACE', ' ')]), ('IN', 'in')),
    (('IS', 'is', [], [('SPACE', ' ')]), ('NOT', 'not')),
)


def test_advanced_comparison():
    "a<b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])


def test_advanced_comparison_first_space():
    "a <b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', " ")], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', " ")], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [],
            }
        ])


def test_advanced_comparison_second_space():
    "a< b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2, [], [('SPACE', " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2, [], [('SPACE', " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_advanced_comparison_spaces():
    "a < b"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', " ")], after_space),
            (token_name2, value2, [], [('SPACE', " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [('SPACE', " ")], after_space),
            (token_name2, value2, [], [('SPACE', " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a'
                },
                "second": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_advanced_comparison_spaces_atomtrailers():
    "a.b < c"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            ('DOT', '.'),
            ('NAME', 'b'),
            (token_name, value, [("SPACE", " ")], after_space),
            (token_name2, value2, [], [("SPACE", " ")]),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "atomtrailers",
                    "value": [
                        {
                            "type": "name",
                            "value": "a",
                        },
                        {
                            "type": "dot",
                            "first_formatting": [],
                            "second_formatting": [],
                        },
                        {
                            "type": "name",
                            "value": "b",
                        }
                    ],
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            }
        ])


def test_chained_advanced_comparison():
    "a<b<c"
    for (token_name, value, _, after_space), (token_name2, value2) in advanced_comparison_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {
                    "type": "name",
                    "value": 'a',
                },
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {"type": "name", "value": 'a'},
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {"type": "name", "value": 'a'},
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {"type": "name", "value": 'a'},
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {"type": "name", "value": 'a'},
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'b'),
            (token_name, value, [], after_space),
            (token_name2, value2),
            ('NAME', 'c'),
        ], [
            {
                "type": "comparison",
                "value": {
                    "type": "comparison_operator",
                    "first": value,
                    "second": value2,
                    "formatting": [{"type": "space", "value": after_space[0][1]}],
                },
                "first": {"type": "name", "value": 'a'},
                "second": {
                    "type": "comparison",
                    "value": {
                        "type": "comparison_operator",
                        "first": value,
                        "second": value2,
                        "formatting": [{"type": "space", "value": after_space[0][1]}],
                    },
                    "first": {"type": "name", "value": "b"},
                    "second": {"type": "name", "value": "c"},
                    "first_formatting": [],
                    "second_formatting": [],
                },
                "first_formatting": [],
                "second_formatting": [],
            }
        ])


def test_not():
    "not a"
    parse_simple([
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ], [
        {
            "type": "unitary_operator",
            "value": 'not',
            "target": {
                "type": "name",
                "value": 'a',
            },
            "formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_not_not():
    "not not a"
    parse_simple([
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ], [
        {
            "type": "unitary_operator",
            "value": 'not',
            "target": {
                "type": "unitary_operator",
                "value": 'not',
                "target": {"type": "name", "value": 'a', },
                "formatting": [{"type": "space", "value": " "}]
            },
            "formatting": [{"type": "space", "value": " "}]
        }
    ])
    parse_simple([
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NOT', 'not', [], [('SPACE', ' ')]),
        ('NAME', 'a'),
    ], [
        {
            "type": "unitary_operator",
            "value": 'not',
            "target": {
                "type": "unitary_operator",
                "value": 'not',
                "target": {"type": "name", "value": 'a', },
                "formatting": [{"type": "space", "value": " "}]
            },
            "formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_and():
    "a and b"
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_and_and():
    "a and b and c"
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'and',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_or():
    "a or b"
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'b'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'b',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_or_or():
    "a or b or c"
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'or',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_or_and():
    "a or b and c"
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b',
                },
                "second": {
                    "type": "name",
                    "value": 'c'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('AND', 'and', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "boolean_operator",
            "value": 'or',
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "boolean_operator",
                "value": 'and',
                "first": {
                    "type": "name",
                    "value": 'b'
                },
                "second": {
                    "type": "name",
                    "value": 'c',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_ternary_operator():
    "a if b else c"
    parse_simple([
        ('NAME', 'a'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('ELSE', 'else', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "ternary_operator",
            "value": {
                "type": "name",
                "value": 'b',
            },
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'c'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('ELSE', 'else', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "ternary_operator",
            "value": {
                "type": "name",
                "value": 'b'
            },
            "first": {
                "type": "name",
                "value": 'a',
            },
            "second": {
                "type": "name",
                "value": 'c'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('IF', 'if', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('ELSE', 'else', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "ternary_operator",
            "value": {
                "type": "name",
                "value": 'b'
            },
            "first": {
                "type": "name",
                "value": 'a'
            },
            "second": {
                "type": "name",
                "value": 'c',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "third_formatting": [{"type": "space", "value": " "}],
            "fourth_formatting": [{"type": "space", "value": " "}],
        }
    ])


def test_assignment():
    "a = b"
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "name",
                "value": 'b',
            },
            "target": {
                "type": "name",
                "value": 'a'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "name",
                "value": 'b'
            },
            "target": {
                "type": "name",
                "value": 'a',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])


def test_assignment_assignment():
    "a = b = c"
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c',
                },
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {
                "type": "name",
                "value": 'a'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c',
                },
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {
                "type": "name",
                "value": 'a'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c'
                },
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {
                "type": "name",
                "value": 'a'
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c'
                },
                "target": {
                    "type": "name",
                    "value": 'b',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {"type": "name", "value": 'a'},
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c'
                },
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {
                "type": "name",
                "value": 'a',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "assignment",
                "value": {
                    "type": "name",
                    "value": 'c'
                },
                "target": {
                    "type": "name",
                    "value": 'b'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "operator": "",
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            },
            "target": {
                "type": "name",
                "value": 'a',
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])


def test_assignment_star_expr():
    "a, *b = c"
    parse_simple([
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('STAR', '*', [], []),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "name",
                "value": 'c',
            },
            "target": {
                "type": "tuple",
                "value": [
                    {
                        "type": "name",
                        "value": "a"
                    },
                    {
                        "type": "comma",
                        "first_formatting": [],
                        "second_formatting": [
                            {
                                "type": "space",
                                "value": " "
                            }
                        ]
                    },
                    {
                        "type": "star_expression",
                        "formatting": [],
                        "value": {
                            "type": "name",
                            "value": "b",
                        }
                    }
                ],
                "first_formatting": [],
                "second_formatting": [],
                "third_formatting": [],
                "fourth_formatting": [],
                "with_parenthesis": False,
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])
    "a, *  b = c"
    parse_simple([
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('STAR', '*', [], [('SPACE', '  ')]),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "assignment",
            "value": {
                "type": "name",
                "value": 'c',
            },
            "target": {
                "type": "tuple",
                "value": [
                    {
                        "type": "name",
                        "value": "a"
                    },
                    {
                        "type": "comma",
                        "first_formatting": [],
                        "second_formatting": [
                            {
                                "type": "space",
                                "value": " "
                            }
                        ]
                    },
                    {
                        "type": "star_expression",
                        "formatting": [{
                            "type": "space",
                            "value": "  "
                        }],
                        "value": {
                            "type": "name",
                            "value": "b",
                        }
                    }
                ],
                "first_formatting": [],
                "second_formatting": [],
                "third_formatting": [],
                "fourth_formatting": [],
                "with_parenthesis": False,
            },
            "first_formatting": [{"type": "space", "value": " "}],
            "second_formatting": [{"type": "space", "value": " "}],
            "operator": "",
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])


augmented_assignment_tokens = (
    ('PLUS_EQUAL', '+='),
    ('MINUS_EQUAL', '-='),
    ('STAR_EQUAL', '*='),
    ('SLASH_EQUAL', '/='),
    ('PERCENT_EQUAL', '%='),
    ('AMPER_EQUAL', '&='),
    ('AT_EQUAL', '@='),
    ('VBAR_EQUAL', '|='),
    ('CIRCUMFLEX_EQUAL', '^='),
    ('LEFT_SHIFT_EQUAL', '<<='),
    ('RIGHT_SHIFT_EQUAL', '>>='),
    ('DOUBLE_STAR_EQUAL', '**='),
    ('DOUBLE_SLASH_EQUAL', '//='),
)


def test_augmented_assignment():
    "a += b"
    for token_name, value in augmented_assignment_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "assignment",
                "operator": value[:-1],
                "value": {
                    "type": "name",
                    "value": 'b',
                },
                "target": {
                    "type": "name",
                    "value": 'a'
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            }
        ])
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
            ('NAME', 'b'),
        ], [
            {
                "type": "assignment",
                "operator": value[:-1],
                "value": {
                    "type": "name",
                    "value": 'b'
                },
                "target": {
                    "type": "name",
                    "value": 'a',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            }
        ])


# TODO fix this mess
def test_augmented_assignment_augmented_assignment():
    "a += b"
    # for token_name, value in augmented_assignment_tokens:
    #     with pytest.raises(Exception):
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             {
    #                 "type": "assignment",
    #                 "operator": augmented_assignment(__2__operator=__2__value[:-1], __2__value={
    #                     "type": "name",
    #                     "value": 'c',
    #                 }, __2__target={
    #                     "type": "name",
    #                     "value": 'b'
    #                 }, __2__first_space=" ", __2__second_space=" ", )[:-1],
    #                 "value": augmented_assignment(__2__operator=__2__value[:-1], __2__value={
    #                     "type": "name",
    #                     "value": 'c',
    #                 }, __2__target={
    #                     "type": "name",
    #                     "value": 'b'
    #                 }, __2__first_space=" ", __2__second_space=" ", ),
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'a'
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }
    #         ])
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             augmented_assignment(operator=value[:-1], value={
    #                 "type": "assignment",
    #                 "operator": value[:-1],
    #                 "value": {
    #                     "type": "name",
    #                     "value": 'c',
    #                 },
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'b'
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }, target={
    #                 "type": "name",
    #                 "value": 'a'
    #             }, first_space=" ", second_space=" ", )
    #         ])
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             {
    #                 "type": "assignment",
    #                 "operator": augmented_assignment(__4__operator=__4__value[:-1], __4__value={
    #                     "type": "name",
    #                     "value": 'c'
    #                 }, __4__target={
    #                     "type": "name",
    #                     "value": 'b',
    #                 }, __4__first_space=" ", __4__second_space=" ", )[:-1],
    #                 "value": augmented_assignment(__4__operator=__4__value[:-1], __4__value={
    #                     "type": "name",
    #                     "value": 'c'
    #                 }, __4__target={
    #                     "type": "name",
    #                     "value": 'b',
    #                 }, __4__first_space=" ", __4__second_space=" ", ),
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'a'
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }
    #         ])
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             augmented_assignment(operator=value[:-1], value={
    #                 "type": "assignment",
    #                 "operator": value[:-1],
    #                 "value": {
    #                     "type": "name",
    #                     "value": 'c'
    #                 },
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'b',
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }, target={"type": "name", "value": 'a'}, first_space=" ", second_space=" ", )
    #         ])
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             {
    #                 "type": "assignment",
    #                 "operator": augmented_assignment(__6__operator=__6__value[:-1], __6__value={
    #                     "type": "name",
    #                     "value": 'c'
    #                 }, __6__target={
    #                     "type": "name",
    #                     "value": 'b'
    #                 }, __6__first_space=" ", __6__second_space=" ", )[:-1],
    #                 "value": augmented_assignment(__6__operator=__6__value[:-1], __6__value={
    #                     "type": "name",
    #                     "value": 'c'
    #                 }, __6__target={
    #                     "type": "name",
    #                     "value": 'b'
    #                 }, __6__first_space=" ", __6__second_space=" ", ),
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'a',
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }
    #         ])
    #         parse_simple([
    #             ('NAME', 'a'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'b'),
    #             (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
    #             ('NAME', 'c'),
    #         ], [
    #             augmented_assignment(operator=value[:-1], value={
    #                 "type": "assignment",
    #                 "operator": value[:-1],
    #                 "value": {
    #                     "type": "name",
    #                     "value": 'c'
    #                 },
    #                 "target": {
    #                     "type": "name",
    #                     "value": 'b'
    #                 },
    #                 "first_formatting": [{"type": "space", "value": " "}],
    #                 "second_formatting": [{"type": "space", "value": " "}],
    #             }, target={
    #                 "type": "name",
    #                 "value": 'a',
    #             }, first_space=" ", second_space=" ", )
    #         ])


def test_augmented_assignment_yield_b():
    "a += yield b"
    for token_name, value in augmented_assignment_tokens:
        parse_simple([
            ('NAME', 'a'),
            (token_name, value, [("SPACE", " ")], [("SPACE", " ")]),
            ('YIELD', 'yield', [], [('SPACE', ' ')]),
            ('NAME', 'b'),
        ], [
            {
                "type": "assignment",
                "operator": value[:-1],
                "value": {
                    "formatting": [
                        {
                            "type": "space",
                            "value": " "
                        }
                    ],
                    "type": "yield",
                    "value": {
                        "type": "name",
                        "value": "b",
                    },
                },
                "target": {
                    "type": "name",
                    "value": 'a',
                },
                "first_formatting": [{"type": "space", "value": " "}],
                "second_formatting": [{"type": "space", "value": " "}],
                "annotation": {},
                "annotation_first_formatting": [],
                "annotation_second_formatting": [],
            }
        ])


def test_a_equal_yield_b():
    """
    a = yield b
    """
    parse_simple([
        ('NAME', 'a'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('YIELD', 'yield', [("SPACE", "")], [("SPACE", " ")]),
        ('NAME', 'b'),
    ], [
        {
            "first_formatting": [{"type": "space", "value": " "}],
            "type": "assignment",
            "operator": "",
            "target": {
                "type": "name",
                "value": "a"
            },
            "value": {
                "type": "yield",
                "formatting": [{"type": "space", "value": " "}],
                "value": {
                    "type": "name",
                    "value": "b"
                },
            },
            "second_formatting": [{"type": "space", "value": " "}],
            "annotation": {},
            "annotation_first_formatting": [],
            "annotation_second_formatting": [],
        }
    ])


def test_expr_comma_list():
    "a or b,c+d"
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a',
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                }
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b',
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                }
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c',
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                }
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd',
                    },
                    "first_formatting": [],
                    "second_formatting": []
                }
            ],
        }
    ])


def test_expr_comma_list_3_items():
    "a or b,c+d,e"
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a',
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "name",
                    "value": 'e'
                },
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b',
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "name",
                    "value": 'e'
                },
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c',
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "name",
                    "value": 'e'
                },
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd',
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "name",
                    "value": 'e'
                },
            ],
        }
    ])
    parse_simple([
        ('NAME', 'a'),
        ('OR', 'or', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ','),
        ('NAME', 'c'),
        ('PLUS', '+'),
        ('NAME', 'd'),
        ('COMMA', ','),
        ('NAME', 'e'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "boolean_operator",
                    "value": 'or',
                    "first": {
                        "type": "name",
                        "value": 'a'
                    },
                    "second": {
                        "type": "name",
                        "value": 'b'
                    },
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "binary_operator",
                    "value": '+',
                    "first": {
                        "type": "name",
                        "value": 'c'
                    },
                    "second": {
                        "type": "name",
                        "value": 'd'
                    },
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": []
                },
                {
                    "type": "name",
                    "value": 'e',
                },
            ],
        }
    ])


def test_await_a():
    "await a"
    parse_simple([
        ('NAME', 'await', [], []),
        ('SPACE', ' '),
        ('NAME', 'a'),
    ], [
        {
            'formatting': [{'type': 'space', 'value': ' '}],
            'type': 'await',
            "value": {'type': 'atomtrailers', 'value': [{'type': 'name', 'value': 'a'}]},
        },
    ])


def test_await_a_bad_keyword():
    "await a"
    with pytest.raises(ParsingError):
        parse_simple([
            ('NAME', 'not_await', [], []),
            ('SPACE', ' '),
            ('NAME', 'a'),
        ], [])


def test_implicit_tuple_space():
    "a, b , c"
    parse_simple([
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "c",
                }
            ],
        }
    ])


def test_implicit_tuple_one_item():
    "a ,"
    parse_simple([
        ('NAME', 'a'),
        ('COMMA', ',', [('SPACE', ' ')]),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                }
            ]
        }
    ])


def test_implicit_tuple_trailing_comma():
    "a, b ,"
    parse_simple([
        ('NAME', 'a'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('COMMA', ',', [('SPACE', ' ')]),
    ], [
        {
            "type": "tuple",
            "with_parenthesis": False,
            "first_formatting": [],
            "second_formatting": [],
            "third_formatting": [],
            "fourth_formatting": [],
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "comma",
                    "first_formatting": [],
                    "second_formatting": [{"type": "space", "value": " "}],
                },
                {
                    "type": "name",
                    "value": "b",
                },
                {
                    "type": "comma",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                }
            ]
        }
    ])


def test_subscript_ellipsis():
    "a[...]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('ELLIPSIS', '...'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "ellipsis",
                        "first_formatting": [],
                        "second_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_ellipsis_space():
    "a[ ...   ]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '[', [('SPACE', ' ')]),
        ('ELLIPSIS', '...'),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', '   ')]),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": "   "}],
                    "fourth_formatting": [],
                    "value": {
                        "type": "ellipsis",
                        "first_formatting": [],
                        "second_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_test():
    "a[b]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "name",
                        "value": "b",
                    }
                }
            ]
        }
    ])


def test_subscript_slice_empty():
    "a[:]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {},
                        "upper": {},
                        "step": {},
                        "has_two_colons": False,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_empty_both():
    "a[: :]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('COLON', ':'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {},
                        "upper": {},
                        "step": {},
                        "has_two_colons": True,
                        "first_formatting": [],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_one():
    "a[b :]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "upper": {},
                        "step": {},
                        "has_two_colons": False,
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_both_one():
    "a[b : : ]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('COLON', ':', [], []),
        ('RIGHT_SQUARE_BRACKET', ']', [('SPACE', ' ')]),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [{"type": "space", "value": " "}],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "upper": {},
                        "step": {},
                        "has_two_colons": True,
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_upper():
    "a[:b]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':'),
        ('NAME', 'b'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "upper": {
                            "type": "name",
                            "value": "b",
                        },
                        "lower": {},
                        "step": {},
                        "has_two_colons": False,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_upper_both():
    "a[:b :]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':'),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "upper": {
                            "type": "name",
                            "value": "b",
                        },
                        "lower": {},
                        "step": {},
                        "has_two_colons": True,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [{"type": "space", "value": " "}],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_step():
    "a[: : b]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'b'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "upper": {},
                        "lower": {},
                        "step": {
                            "type": "name",
                            "value": "b",
                        },
                        "has_two_colons": True,
                        "first_formatting": [],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [],
                        "fourth_formatting": [{"type": "space", "value": " "}],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_lower_upper():
    "a[b : c]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "upper": {
                            "type": "name",
                            "value": "c",
                        },
                        "step": {},
                        "has_two_colons": False,
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_lower_upper_both():
    "a[b : c :]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [('SPACE', ' ')]),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "upper": {
                            "type": "name",
                            "value": "c",
                        },
                        "step": {},
                        "has_two_colons": True,
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [{"type": "space", "value": " "}],
                        "fourth_formatting": [],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_lower_step():
    "a[b:: c]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "step": {
                            "type": "name",
                            "value": "c",
                        },
                        "upper": {},
                        "has_two_colons": True,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [{"type": "space", "value": " "}],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_upper_step():
    "a[:b: c]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('COLON', ':'),
        ('NAME', 'b'),
        ('COLON', ':', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "upper": {
                            "type": "name",
                            "value": "b",
                        },
                        "step": {
                            "type": "name",
                            "value": "c",
                        },
                        "lower": {},
                        "has_two_colons": True,
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [{"type": "space", "value": " "}],
                    }
                }
            ]
        }
    ])


def test_subscript_slice_lower_upper_step():
    "a[b : c : d]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COLON', ':', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'd'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "slice",
                        "lower": {
                            "type": "name",
                            "value": "b",
                        },
                        "upper": {
                            "type": "name",
                            "value": "c",
                        },
                        "step": {
                            "type": "name",
                            "value": "d",
                        },
                        "has_two_colons": True,
                        "first_formatting": [{"type": "space", "value": " "}],
                        "second_formatting": [{"type": "space", "value": " "}],
                        "third_formatting": [{"type": "space", "value": " "}],
                        "fourth_formatting": [{"type": "space", "value": " "}],
                    }
                }
            ]
        }
    ])


def test_subscript_test_implicit_tuple():
    "a[b, c]"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_SQUARE_BRACKET', '['),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_SQUARE_BRACKET', ']'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "getitem",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": {
                        "type": "tuple",
                        "first_formatting": [],
                        "second_formatting": [],
                        "third_formatting": [],
                        "fourth_formatting": [],
                        "with_parenthesis": False,
                        "value": [
                            {
                                "type": "name",
                                "value": "b",
                            },
                            {
                                "type": "comma",
                                "first_formatting": [],
                                "second_formatting": [{"type": "space", "value": " "}],
                            },
                            {
                                "type": "name",
                                "value": "c",
                            }
                        ],
                    }
                }
            ]
        }
    ])


def test_call_empty():
    "a()"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [],
                }
            ]
        }
    ])


def test_call_empty_with_space():
    "a ( )"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [],
                }
            ]
        }
    ])


def test_call_empty_with_space_fourth_formatting():
    "a ( )"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '(', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('RIGHT_PARENTHESIS', ')', [], [('SPACE', ' ')]),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [{"type": "space", "value": " "}],
                    "second_formatting": [{"type": "space", "value": " "}],
                    "third_formatting": [],
                    "fourth_formatting": [{"type": "space", "value": " "}],
                    "value": [],
                }
            ]
        }
    ])


def test_call_one():
    "a(b)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "b",
                            }
                        }
                    ],
                }
            ]
        }
    ])


def test_call_two():
    "a(b, c)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "b",
                            }
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "c",
                            }
                        }
                    ],
                }
            ]
        }
    ])


def test_call_two_star_arg():
    "a(b, c, *d)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('STAR', '*'),
        ('NAME', 'd'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "b",
                            }
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "c",
                            }
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "type": "list_argument",
                            "annotation": {},
                            "annotation_first_formatting": [],
                            "annotation_second_formatting": [],
                            "formatting": [],
                            "value": {
                                "type": "name",
                                "value": "d",
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_call_two_star_arg_kwarg():
    "a(b, c, *d, **e)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('STAR', '*'),
        ('NAME', 'd'),
        ('COMMA', ',', [], [('SPACE', ' ')]),
        ('DOUBLE_STAR', '**'),
        ('NAME', 'e'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "b",
                            }
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "target": {},
                            "first_formatting": [],
                            "second_formatting": [],
                            "type": "call_argument",
                            "value": {
                                "type": "name",
                                "value": "c",
                            }
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "type": "list_argument",
                            "annotation": {},
                            "annotation_first_formatting": [],
                            "annotation_second_formatting": [],
                            "formatting": [],
                            "value": {
                                "type": "name",
                                "value": "d",
                            },
                        },
                        {
                            "type": "comma",
                            "first_formatting": [],
                            "second_formatting": [{"type": "space", "value": " "}],
                        },
                        {
                            "type": "dict_argument",
                            "annotation": {},
                            "annotation_first_formatting": [],
                            "annotation_second_formatting": [],
                            "formatting": [],
                            "value": {
                                "type": "name",
                                "value": "e",
                            },
                        }
                    ],
                }
            ]
        }
    ])


def test_call_named():
    "a(b = c)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'b'),
        ('EQUAL', '=', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'c'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "value": {
                                "type": "name",
                                "value": "c",
                            },
                            "first_formatting": [{"type": "space", "value": " "}],
                            "second_formatting": [{"type": "space", "value": " "}],
                            "type": "call_argument",
                            "target": {
                                "value": "b",
                                "type": "name",
                            }
                        }
                    ],
                }
            ]
        }
    ])


def test_call_generator():
    "a(x for y in z)"
    parse_simple([
        ('NAME', 'a'),
        ('LEFT_PARENTHESIS', '('),
        ('NAME', 'x'),
        ('FOR', 'for', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'y'),
        ('IN', 'in', [('SPACE', ' ')], [('SPACE', ' ')]),
        ('NAME', 'z'),
        ('RIGHT_PARENTHESIS', ')'),
    ], [
        {
            "type": "atomtrailers",
            "value": [
                {
                    "type": "name",
                    "value": "a",
                },
                {
                    "type": "call",
                    "first_formatting": [],
                    "second_formatting": [],
                    "third_formatting": [],
                    "fourth_formatting": [],
                    "value": [
                        {
                            "generators": [
                                {
                                    "first_formatting": [{"type": "space", "value": " "}],
                                    "second_formatting": [{"type": "space", "value": " "}],
                                    "third_formatting": [{"type": "space", "value": " "}],
                                    "fourth_formatting": [{"type": "space", "value": " "}],
                                    "type": "comprehension_loop",
                                    "ifs": [],
                                    "target": {
                                        "type": "name",
                                        "value": "z",
                                    },
                                    "iterator": {
                                        "type": "name",
                                        "value": "y",
                                    },
                                }
                            ],
                            "type": "argument_generator_comprehension",
                            "result": {
                                "type": "name",
                                "value": "x",
                            }
                        }
                    ],
                }
            ]
        }
    ])
