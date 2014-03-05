#!/usr/bin/python
# -*- coding:Utf-8 -*-
from test_utils import parse_simple


def test_simple_import():
    "import   pouet"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet')],
          [{
            "type": "import",
            "value": [
                      {
                       "value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": "pouet",
                                           }],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None,
                      }
                      ],
                      "formatting": [{"type": "space", "value": "  "}],
                     }])

def test_import_basic_dot():
    "import   pouet.blob"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [{
            "type": "import",
            "value": [{
                       "value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {
                                            "type": "name",
                                            "value": "pouet",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "blob"
                                           }
                                          ],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None,
                      }
                     ],
            "formatting": [{"type": "space", "value": "  "}]
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name", "value": "pouet"},
                                           { "type": "dot", "value": ".", },
                                           { "type": "name", "value": "blob", }
                                          ],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None,
                      }
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])

def test_import_more_dot():
    "import   pouet.blob .plop"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{
            "type": "import",
            "value": [
                      {
                       "value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {
                                            "type": "name",
                                            "value": "pouet",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "blob"
                                           },
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "plop"
                                           }
                                          ],
                                }                                    ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None
                      }
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }
          ])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{ "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name",
                                            "value": "pouet"},
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "blob",
                                           },
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "plop"}
                                          ],
                                }
                       ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name",
                                            "value": "pouet"},
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "blob"},
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "plop",
                                           }
                                          ],
                                }
                       ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {
                                            "type": "name",
                                            "value": "pouet",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "blob"},
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "plop"}
                                          ],
                                }
                       ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name",
                                            "value": "pouet"},
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "blob",
                                           },
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "plop"}
                                          ],
                                }
                       ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', [('SPACE', ' ')]),
           ('NAME', 'plop')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name",
                                            "value": "pouet"},
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {"type": "name",
                                            "value": "blob"},
                                           {
                                            "type": "space",
                                            "value": " ",
                                           },
                                           {
                                            "type": "dot",
                                            "value": ".",
                                           },
                                           {
                                            "type": "name",
                                            "value": "plop",
                                           }
                                          ],
                                }
                       ,
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])

def test_import_as():
    "import   pouet as  b"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', '  ')]),
           ('NAME', 'pouet'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'b')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": "pouet",
                                           }],
                                },
                       "before_formatting": [{"type": "space", "value": " "}],
                       "as_": True,
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": 'b',
                       "type": "dotted_as_name",
                      }
                     ],
            "formatting": [{"type": "space", "value": "  "}],
           }])

def test_import_a_b():
    "import a, b"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'a',
                                           }],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'b'}]                     },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": " "}], }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'b',
                                           }]                     },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'a',
                                           }]                     },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'b'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}]                     },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'b',
                                           }],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None}
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])

def test_import_a_b_as_c():
    "import a, b.d as  c"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'a',
                                           }],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {
                                            "type": "name",
                                            "value": 'b'},
                                           {
                                            "type": "dot",
                                            "value": "."
                                           },
                                           {
                                            "type": "name",
                                            "value": 'd'}
                                          ],
                                },
                       "before_formatting": [{"type": "space", "value": " "}],
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": "c",
                       "type": "dotted_as_name",
                       "as_": True,
                      }
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {
                                            "type": "name",
                                            "value": 'b',
                                           },
                                           {
                                            "type": "dot",
                                            "value": "."                             },
                                           {"type": "name",
                                            "value": 'd'}                         ],
                                },
                       "as_": True,
                       "before_formatting": [{"type": "space", "value": " "}],
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": "c"                                    ,
                       "type": "dotted_as_name",
                      }
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [
                                           {"type": "name",
                                            "value": 'b'},
                                           {
                                            "type": "dot",
                                            "value": "."                             },
                                           {
                                            "type": "name",
                                            "value": 'd',
                                           }                         ],
                                },
                       "as_": True,
                       "before_formatting": [{"type": "space", "value": " "}],
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": "c",
                       "type": "dotted_as_name",
                      }
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
                 [{
                   "type": "import",
                   "value": [
                             {
                              "before_formatting": [],
                              "after_formatting": [],
                              "as_": False,
                              "target": None,
                              "value":
                              {
                               "value": [{
                                          "type": "name",
                                          "value": 'a',
                                         }],
                              "type": "dotted_name",
                              },
                              "type": "dotted_as_name",
                             },
                             {
                              "type": "comma", "value": ",",
                             },
                             {
                              "type": "space",
                              "value": " ",
                             },
                             {"value":
                              {
                               "type": "dotted_name",
                               "value": [
                                         {"type": "name",
                                          "value": 'b'},
                                         {
                                          "type": "dot",
                                          "value": ".",
                                         },
                                         {"type": "name",
                                          "value": 'd'}
                                        ],

                              },
                              "as_": True,
                              "before_formatting": [{"type": "space", "value": " "}],
                              "after_formatting": [{"type": "space", "value": "  "}],
                              "target": "c",
                              "type": "dotted_as_name",
                             }
                            ],
                   "formatting": [{"type": "space", "value": " "}], }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
          [{
            "type": "import",
            "value": [
                      {
                       "value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None
                      },
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {
                       "value":
                       {
                        "type": "dotted_name",
                        "value": [
                                  {
                                   "type": "name",
                                   "value": 'b',
                                  },
                                  {
                                   "type": "dot",
                                   "value": ".",
                                  },
                                  {"type": "name",
                                   "value": 'd'}
                                 ],
                       },
                       "as_": True,
                       "before_formatting": [{"type": "space", "value": " "}],
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": "c"                                    ,
                       "type": "dotted_as_name",
                      }
                     ],
            "formatting": [{"type": "space", "value": " "}],
           }])
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', '  ')]),
           ('NAME', 'c')],
          [{ "type": "import",
            "value": [
                      {
                       "value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'a'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None
                      },
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value":
                       {
                        "type": "dotted_name",
                        "value": [
                                  {"type": "name",
                                   "value": 'b'},
                                  {
                                   "type": "dot",
                                   "value": ".",
                                  },
                                  {
                                   "type": "name",
                                   "value": 'd',
                                  }
                                 ],
                       },
                       "as_": True,
                       "before_formatting": [{"type": "space", "value": " "}],
                       "after_formatting": [{"type": "space", "value": "  "}],
                       "target": "c",
                       "type": "dotted_as_name",
                      }
                     ],
            "formatting": [{"type": "space", "value": " "}], }])

def test_import_a_b_c_d():
    "import a, b, c, d"
    parse_simple([
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'c'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'd')],
          [{
            "type": "import",
            "value": [
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{
                                            "type": "name",
                                            "value": 'a',
                                           }],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {
                       "type": "space",
                       "value": " ",
                      },
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'b'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
                      {"type": "space",
                       "value": " "},
                      {"value": {
                                 "type": "dotted_name",
                                 "value": [{"type": "name",
                                            "value": 'c'}],
                                },
                       "type": "dotted_as_name",
                       "before_formatting": [],
                       "after_formatting": [],
                       "as_": False,
                       "target": None},
                      {
                       "type": "comma",
                       "value": ",",
                      },
    {"type": "space",
     "value": " "},
    {"value": {
               "type": "dotted_name",
               "value": [{"type": "name",
                          "value": 'd'}],
              },
     "type": "dotted_as_name",
     "before_formatting": [],
     "after_formatting": [],
     "as_": False,
     "target": None}                     ],
    "formatting": [{"type": "space", "value": " "}], }])

def test_from_a_import_b():
    "from a import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}]
           }])

def test_from_a_dot_c_import_b():
    "from a.C import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {"type": "name",
                                 "value": 'c'}
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {"type": "name",
                                 "value": 'a'},
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'c',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_a_dot_c_import_b_d():
    "from a.c import b, d"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'd')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {"type": "name",
                                 "value": 'c'}
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "comma",
                         "value": ",",
                        },
                        {
                         "type": "space",
                         "value": " ",
                        },
                        {"type": "name_as_name",
                         "value": 'd',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None}
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])
    parse_simple([
           ('FROM',
            'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'd')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {"type": "name",
                                 "value": 'c'}
                               ],
                     },
            "targets": [
                        {"type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None},
                        {
                         "type": "comma",
                         "value": ",",
                        },
                        {
                         "type": "space",
                         "value": " ",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'd',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])
    parse_simple([
           ('FROM',
            'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'd')],
          [{ "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {"type": "name",
                                 "value": 'a'},
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'c',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "comma",
                         "value": ",",
                        },
                        {
                         "type": "space",
                         "value": " ",
                        },
                        {"type": "name_as_name",
                         "value": 'd',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None}
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}]
           }])
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('COMMA', ',', [], [('SPACE', ' ')]),
           ('NAME', 'd')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {"type": "name",
                                 "value": 'a'},
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'c',
                                }
                               ],
                     },
            "targets": [
                        {"type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None},
                        {
                         "type": "comma",
                         "value": ",",
                        },
                        {
                         "type": "space",
                         "value": " ",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'd',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}]
           }])

def test_from_a_import_b_as_d():
    "from a import b as d"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b'),
           ('AS', 'as', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'd')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a'                                   }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [{"type": "space", "value": " "}],
                         "after_formatting": [{"type": "space", "value": " "}],
                         "as_": True,
                         "target": "d",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_a_import_parenthesis_b():
    "from a import (b)"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [{
                                 "type": "name",
                                 "value": 'a',
                                }],
                     },
            "targets": [
                        {
                         "type": "left_parenthesis",
                         "value": "(",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "right_parenthesis",
                         "value": ")",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_a_import_parenthesis_b_without_space():
    "from a import(b)"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')]),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "left_parenthesis",
                         "value": "(",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "right_parenthesis",
                         "value": ")",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [] }])

def test_from_a_import_parenthesis_b_comma():
    "from a import (b,)"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "left_parenthesis",
                         "value": "(",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "comma",
                         "value": ",",
                        },
                        {
                         "type": "right_parenthesis",
                         "value": ")",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}]
           }])

def test_from_a_import_parenthesis_b_space():
    "from a import (b )"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')', [('SPACE', ' ')]),
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "left_parenthesis",
                         "value": "(",
                        },
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        },
                        {
                         "type": "space",
                         "value": " ",
                        },
                        {
                         "type": "right_parenthesis",
                         "value": ")",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_a_import_star():
    "from a import *"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('STAR', '*')
          ],
          [{ "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "star",
                         "value": "*",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_a_import_star_without_space():
    "from a import*"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')]),
           ('STAR', '*')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "star",
                         "value": "*",
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": []
           }])

def test_from_dot_a_import_b():
    "from .a import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_dot_dot_dot_a_import_b():
    "from ...a import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_no_space_dot_a_import_b():
    "from.a import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                },
                                {
                                 "type": "name",
                                 "value": 'a',
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_dot_import_b():
    "from . import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{ "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                }                                    ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }                                ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_dot_no_space_import_b():
    "from .import b"
    parse_simple([
           ('FROM', 'from', [], [('SPACE', ' ')]),
           ('DOT', '.'),
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [{"type": "space", "value": " "}],
            "middle_formatting": [],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_no_space_dot_import_b():
    "from. import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', [('SPACE', ' ')], [('SPACE', ' ')]),
           ('NAME', 'b')
          ],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                        }
                       ],
            "before_formatting": [],
            "middle_formatting": [{"type": "space", "value": " "}],
            "after_formatting": [{"type": "space", "value": " "}] }])

def test_from_no_space_dot_no_sapceimport_b():
    "from.import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', [], [('SPACE', ' ')]),
           ('NAME', 'b')],
          [{
            "type": "from_import",
            "value": {
                      "type": "dotted_name",
                      "value": [
                                {
                                 "type": "dot",
                                 "value": ".",
                                }
                               ],
                     },
            "targets": [
                        {
                         "type": "name_as_name",
                         "value": 'b',
                         "before_formatting": [],
                         "after_formatting": [],
                         "as_": False,
                         "target": None,
                         }
                       ],
            "before_formatting": [],
            "middle_formatting": [],
            "after_formatting": [{"type": "space", "value": " "}] }])

# TODO: 'from. .import*
