Baron
=====

Baron is a FST for Python, a Full Syntax Tree. By opposition to an AST which
drops some syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the operation
ast_to_code(code_to_ast(source_code)) == source_code.

Installation
============

::

    pip install baron

Basic Usage
===========

::

    from baron import parse, dumps

    ast = parse(source_code_string)
    source_code_string == dumps(ast)

RedBaron
========

There is great chances that you'll probably want to use
[RedBaron](https://github.com/Psycojoker/redbaron) instead of using Baron
directly. Think of Baron as the "bytecode of python source code" and RedBaron
as some sort of usable layer on top of it.

Table of Content
================

.. toctree::
   :maxdepth: 2
