Welcome to Baron's documentation!
=================================

Introduction
------------

Baron is a Full Syntax Tree (FST) for Python. It represents source code
as a structured tree, easily parsable by a computer. By opposition to
an `Abstract Syntax Tree
<http://en.wikipedia.org/wiki/Abstract_syntax_tree>`_ (AST) which drops
syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the
operation :file:`fst_to_code(code_to_fst(source_code)) == source_code`.

If you want to understand why this is important, read this:
https://github.com/PyCQA/baron#why-is-this-important

Github (code, bug tracker, etc.)
--------------------------------

https://github.com/PyCQA/baron

Installation
------------

::

    pip install baron

RedBaron
--------

There is a good chance that you'll want to use `RedBaron
<https://redbaron.readthedocs.io>`_ instead of using Baron directly.
Think of Baron as the "bytecode of python source code" and RedBaron as
some sort of usable layer on top of it, a bit like dom/jQuery or
html/Beautifulsoup.

Basic usage
-----------

.. ipython:: python
    :suppress:

    import sys
    sys.path.append("..")

.. ipython:: python

    from baron import parse, dumps

    source_code = "a = 1"
    fst = parse(source_code)
    fst
    generated_source_code = dumps(fst)
    generated_source_code
    source_code == generated_source_code

Table of content
----------------

.. toctree::
   :maxdepth: 2

   basics
   advanced
   technical


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

