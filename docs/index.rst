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


Financial support
-----------------

Baron and RedBaron are a very advanced piece of engineering that requires a lot
of time of concentration to work on. Until the end of 2018, the development
has been a full volunteer work mostly done by [Bram](https://github.com/psycojoker),
but now, to reach the next level and bring those projects to the stability and
quality you expect, we need your support.

You can join our contributors and sponsors on our transparent
[OpenCollective](https://opencollective.com/redbaron), every contribution will
count and will be mainly used to work on the projects stability and quality but
also on continuing, on the side, the R&D side of those projects.

Our supporters
~~~~~~~~~~~~~~

.. image:: https://opencollective.com/redbaron/tiers/i-like-this,-keep-going!/badge.svg?label=I like this, keep going!&color=brightgreen
.. image:: https://opencollective.com/redbaron/tiers/it-looks-cool!/badge.svg?label=It looks cool!&color=brightgreen
.. image:: https://opencollective.com/redbaron/tiers/oh-god,-that-saved-me-so-much-time!/badge.svg?label=Oh god, that saved me so much time!&color=brightgreen

\

.. image:: https://opencollective.com/redbaron/tiers/i-like-this,-keep-going!.svg?avatarHeight=36&width=600

Become our first sponsor!

.. image:: https://opencollective.com/redbaron/tiers/long-term-sponsor.svg?avatarHeight=36&width=600

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

