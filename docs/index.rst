Baron
=====

Baron is a Full Syntax Tree (FST) for Python. By opposition to an AST which
drops some syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the operation
fst_to_code(code_to_fst(source_code)) == source_code.

Installation
============

::

    pip install baron

Basic Usage
===========

Baron provides two main functions: `parse` to transform a string into
the fst and `dumps` to transform the fst back into a string:

.. ipython:: python
    :suppress:

    import sys
    sys.path.append("..")

.. ipython:: python

    from baron import parse, dumps

    source_code = "a = 1"
    fst = parse(source_code)
    generated_source_code = dumps(fst)
    generated_source_code
    source_code == generated_source_code

Like said in the introduction, the FST keeps the formatting:

.. ipython:: python

    source_code = "a=1"
    generated_source_code = dumps(parse(source_code))
    generated_source_code


Helpers
-------

Baron also provides 3 helper functions `show`, `show_file` and
`show_node` to explore the FST (in iPython for example).  Those
functions will print a formatted version of the FST so you can play with
it to explore the FST and have an idea of what you are playing with.

`show` is used directly on a string:

.. ipython:: python

    from baron.helpers import show

    show("a = 1")

    show("a +=  b")

`show_file` is used on the path of a file:

::

    from baron.helpers import show_file

    show_file("/path/to/a/file")

`show_node` is used on an already parsed string:

.. ipython:: python

    from baron import parse
    from baron.helpers import show_node

    fst = parse("a = 1")

    show_node(fst)



RedBaron
========

There is a good chance that you'll want to use `RedBaron
<https://github.com/Psycojoker/redbaron>`_ instead of using Baron directly.
Think of Baron as the "bytecode of python source code" and RedBaron as some
sort of usable layer on top of it, a bit like dom/jQuery or html/Beautifulsoup.

Table of Content
================

.. toctree::
   :maxdepth: 2
