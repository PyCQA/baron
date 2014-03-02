#!/usr/bin/python
# -*- coding:Utf-8 -*-
from test_utils import parse_simple, dotted_as_name, from_import, name_as_name


def test_simple_import():
    "import   pouet"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": "pouet", }], })                     ], "space": "  ", }])

def test_import_basic_dot():
    "import   pouet.blob"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  { "type": "name", "value": "pouet", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "blob"}                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  {"type": "name", "value": "pouet"},                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": "blob", }                                                 ], }                                    )                     ], "space": "  ", }])

def test_import_more_dot():
    "import   pouet.blob .plop"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  { "type": "name", "value": "pouet", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "blob"},                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "plop"}                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  {"type": "name", "value": "pouet"},                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": "blob", },                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "plop"}                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  {"type": "name", "value": "pouet"},                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "blob"},                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": "plop", }                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  { "type": "name", "value": "pouet", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "blob"},                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "plop"}                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  {"type": "name", "value": "pouet"},                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": "blob", },                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "plop"}                                                 ], }                                    )                     ], "space": "  ", }])
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('DOT', '.'),
           ('NAME', 'blob'),
           ('DOT', '.', ' '),
           ('NAME', 'plop')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [                                                  {"type": "name", "value": "pouet"},                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": "blob"},                                                  { "type": "space", "value": " ", },                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": "plop", }                                                 ], }                                    )                     ], "space": "  ", }])

def test_import_as():
    "import   pouet as  b"
    parse_simple([
           ('IMPORT', 'import', '', '  '),
           ('NAME', 'pouet'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'b')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": "pouet", }], },                                     before_space=" ",                                     as_=True,                                     after_space="  ",                                     target='b')                     ], "space": "  ", }])

def test_import_a_b():
    "import a, b"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}]                     })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }]                     })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }]                     }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}]                     }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], })                     ], "space": " ", }])

def test_import_a_b_as_c():
    "import a, b.d as  c"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [                             {"type": "name", "value": 'b'},                             {                                 "type": "dot",                                 "value": "."                             },                             {"type": "name", "value": 'd'}                         ],                      },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [                             { "type": "name", "value": 'b', },                             {                                 "type": "dot",                                 "value": "."                             },                             {"type": "name", "value": 'd'}                         ],                      },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [                             {"type": "name", "value": 'b'},                             {                                 "type": "dot",                                 "value": "."                             },                             { "type": "name", "value": 'd', }                         ],                      },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                     dotted_as_name({                         "type": "dotted_name",                         "value": ([{ "type": "name", "value": 'a', }])                     }),                     { "type": "comma", "value": ",", },                     { "type": "space", "value": " ", },                     dotted_as_name(                                     { "type": "dotted_name", "value": [                                                  {"type": "name", "value": 'b'},                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": 'd'}                                                 ], },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                     dotted_as_name({                         "type": "dotted_name",                         "value": ([{"type": "name", "value": 'a'}])                     }),                     { "type": "comma", "value": ",", },                     { "type": "space", "value": " ", },                     dotted_as_name(                                     { "type": "dotted_name", "value": [                                                  { "type": "name", "value": 'b', },                                                  { "type": "dot", "value": ".", },                                                  {"type": "name", "value": 'd'}                                                 ], },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('DOT', '.'),
           ('NAME', 'd'),
           ('AS', 'as', ' ', '  '),
           ('NAME', 'c')],
          [{ "type": "import", "value": [                     dotted_as_name({                         "type": "dotted_name",                         "value": ([{"type": "name", "value": 'a'}])                     }),                     { "type": "comma", "value": ",", },                     { "type": "space", "value": " ", },                     dotted_as_name(                                     { "type": "dotted_name", "value": [                                                  {"type": "name", "value": 'b'},                                                  { "type": "dot", "value": ".", },                                                  { "type": "name", "value": 'd', }                                                 ], },                                     as_=True,                                     before_space=" ",                                     after_space="  ",                                     target="c"                                    )                     ], "space": " ", }])

def test_import_a_b_c_d():
    "import a, b, c, d"
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'a', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'a'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'b', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'b'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'c', }], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'd'}],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'c'}], }),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'd', }],                     },)                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'a', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'b', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{ "type": "name", "value": 'c', }],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{"type": "name", "value": 'd'}], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])
    parse_simple([
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'a'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'c'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [{ "type": "import", "value": [                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'a'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'b'}],                     },),                      { "type": "comma", "value": ",", },                      {"type": "space", "value": " "},                      dotted_as_name({                         "type": "dotted_name",                         "value": [{"type": "name", "value": 'c'}],                     },),                      { "type": "comma", "value": ",", },                      { "type": "space", "value": " ", },                      dotted_as_name({ "type": "dotted_name", "value": [{ "type": "name", "value": 'd', }], })                     ], "space": " ", }])

def test_from_a_import_b():
    "from a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_a_dot_c_import_b():
    "from a.C import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', },                                     { "type": "dot", "value": ".", },                                     {"type": "name", "value": 'c'}                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     {"type": "name", "value": 'a'},                                     { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'c', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_a_dot_c_import_b_d():
    "from a.c import b, d"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', },                                     { "type": "dot", "value": ".", },                                     {"type": "name", "value": 'c'}                                    ], },
                       targets=[
                                name_as_name('b'),
                                { "type": "comma", "value": ",", },
                                { "type": "space", "value": " ", },
                                name_as_name('d')
                               ]
                      )])
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('DOT', '.'),
           ('NAME', 'c'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b'),
           ('COMMA', ',', '', ' '),
           ('NAME', 'd')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     {"type": "name", "value": 'a'},                                     { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'c', }                                    ], },
                       targets=[
                                name_as_name('b'),
                                { "type": "comma", "value": ",", },
                                { "type": "space", "value": " ", },
                                name_as_name('d')
                               ]
                      )])

def test_from_a_import_b_as_d():
    "from a import b as d"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b'),
           ('AS', 'as', ' ', ' '),
           ('NAME', 'd')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name(
                                             'b',
                                             as_=True,
                                             before_space=" ",
                                             after_space=" ",
                                             target="d"
                                            )
                               ]
                      )])

def test_from_a_import_parenthesis_b():
    "from a import (b)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "left_parenthesis", "value": "(", },
                                name_as_name('b'),
                                { "type": "right_parenthesis", "value": ")", }
                               ]
                      )])

def test_from_a_import_parenthesis_b_without_space():
    "from a import(b)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ''),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "left_parenthesis", "value": "(", },
                                name_as_name('b'),
                                { "type": "right_parenthesis", "value": ")", }
                               ],
                       after_space=""
                      )])

def test_from_a_import_parenthesis_b_comma():
    "from a import (b,)"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('COMMA', ','),
           ('RIGHT_PARENTHESIS', ')')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "left_parenthesis", "value": "(", },
                                name_as_name('b'),
                                { "type": "comma", "value": ",", },
                                { "type": "right_parenthesis", "value": ")", }
                               ]
                      )])

def test_from_a_import_parenthesis_b_space():
    "from a import (b )"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('LEFT_PARENTHESIS', '('),
           ('NAME', 'b'),
           ('RIGHT_PARENTHESIS', ')', ' ', ''),
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "left_parenthesis", "value": "(", },
                                name_as_name('b'),
                                { "type": "space", "value": " ", },
                                { "type": "right_parenthesis", "value": ")", }
                               ]
                      )])

def test_from_a_import_star():
    "from a import *"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('STAR', '*')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "star", "value": "*", }
                               ]
                      )])

def test_from_a_import_star_without_space():
    "from a import*"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ''),
           ('STAR', '*')],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                { "type": "star", "value": "*", }
                               ],
                       after_space=""
                      )])

def test_from_dot_a_import_b():
    "from .a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_dot_dot_dot_a_import_b():
    "from ...a import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", },                                                  { "type": "dot", "value": ".", },                                                  { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                                  { "type": "dot", "value": ".", },                                     { "type": "dot", "value": ".", },                                                  { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('DOT', '.'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", },                                     { "type": "dot", "value": ".", },                                     { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_no_space_dot_a_import_b():
    "from.a import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('NAME', 'a'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import({ "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", },                                     { "type": "name", "value": 'a', }                                    ], },
                       targets=[
                                name_as_name('b')
                               ],
                       before_space=""
                      )])

def test_from_dot_import_b():
    "from . import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", }                                    ], },
                       targets=[
                                name_as_name('b')
                               ]
                      )])

def test_from_dot_no_space_import_b():
    "from .import b"
    parse_simple([
           ('FROM', 'from', '', ' '),
           ('DOT', '.'),
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'b')
          ],
          [from_import({ "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", }                                    ], },
                       targets=[
                                name_as_name('b')
                               ],
                       middle_space=""
                      )])

def test_from_no_space_dot_import_b():
    "from. import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', ' ', ' '),
           ('NAME', 'b')
          ],
          [from_import(
                       { "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", }                                    ], },
                       targets=[
                                name_as_name('b')
                               ],
                       before_space=""
                      )])

def test_from_no_space_dot_no_sapceimport_b():
    "from.import b"
    parse_simple([
           ('FROM', 'from'),
           ('DOT', '.'),
           ('IMPORT', 'import', '', ' '),
           ('NAME', 'b')],
          [from_import({ "type": "dotted_name", "value": [                                     { "type": "dot", "value": ".", }                                    ], },
                       targets=[
                                name_as_name('b')
                               ],
                       middle_space="",
                       before_space=""
                      )])

# TODO: 'from. .import*
