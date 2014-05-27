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

Like said in the introduction, the FST keeps the formatting contrary to
an AST. Here the following 3 codes are equivalent but their formatting
is different. Baron sees the difference so when dumping back the FST,
all the formatting is kept:

.. ipython:: python

    dumps(parse("a = 1"))

    dumps(parse("a=1"))

    dumps(parse( "a   =   1"))


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

    from baron.helpers import show_node

    fst = parse("a = 1")

    show_node(fst)

Under the hood, the FST follows the JSON format so the helpers are
simply encapsulting json pretty printers.

Locate a Node
-------------

Since Baron produces a tree, a path is sufficient to locate univocally
a node in the tree. A common task where a path is involved is when
translating a position in a file (a line and a column) into a node of
the FST.

Baron provides 2 helper functions for that: :file:`position_to_node` and
:file:`position_to_path`. Both function takes a FST tree as first
argument, then the line number and the column number. Line and column
numbers **start at 1**, like in a text editor.

:file:`position_to_node` returns an FST node. This is okay if you only
want to know which node it is but not enough to locate the node in the
tree. Indeed, there can be mutiple identical nodes within the tree.

That's where :file:`position_to_path` is useful. It returns a dictionary
in JSON format which contains 3 values:

* the :file:`path` key contains the path: a list of int and strings which
  represent either the key to take in a Node or the index in a ListNode
  (e.g. "target", "value", 0)
* the :file:`type` key tells the type of the FST node (e.g.
  "function", "assignment", "class")
* the :file:`position_in_rendering_list` key is the rendering position
  of the the node compared to its parent node. This is especially needed
  when the character pointed on is actually not a node itself but only
  a part of a parent node. It's a little complicated but don't worry,
  examples will follow.

Let's first see the difference between the two functions:

.. ipython:: python

    from baron import parse
    from baron.finder import position_to_node, position_to_path

    some_code = """\
    from baron import parse
    from baron.helpers import show_node
    fst = parse("a = 1")
    show_node(fst)
    """

    tree = parse(some_code)

    node = position_to_node(tree, 3, 8)
    show_node(node)
    path = position_to_path(tree, 3, 8)
    path

Okay, the first gives the node and the second the path to the node. Both
also give its type but what does the keys in the path correspond to
exactly? The path tells you that to get to the node, you must take the
4th index of the root ListNode, followed twice by the "value" key of
first the "assignment" Node and next the "atomtrailers" Node. Finally,
take the 0th index in the resulting ListNode. Mmmh, let's try:

.. ipython:: python

    show_node(tree[4]["value"]["value"][0])

Neat. This is so common that there is a function to do that:

.. ipython:: python

    from baron.finder import path_to_node

    show_node(path_to_node(tree, path))

With the two above, that's a total of three functions to locate a node.

And what about the :file:`position_in_rendering_list`? To understand,
the best is an example. What happens if you try to locate the node
corresponding to the left parenthesis on line 3?

.. ipython:: python

    position_to_path(tree, 3, 12)

    show_node(tree[4]["value"]["value"][1])

As you can see, the information given by the path is that I'm on a call
node. No parenthesis in sight. That's where the
:file:`position_in_rendering_list` proves useful. It tells you where you
are located in the rendering dictionnary:

.. ipython:: python

    from baron import rendering_dictionnary

    rendering_dictionnary["call"]

    rendering_dictionnary["call"][1]

Oh I see. Because the parenthesis is a constant, there is no specific
node for the parenthesis. So the path can only go as far as the parent
node, here "call", and show you the position in the rendering
dictionnary.

Yes, that's it. For example, it allows you to distinguish the left and
right parenthesis in a call. 

.. ipython:: python

    position_to_path(tree, 3, 20)

    rendering_dictionnary["call"][5]

To conclude this section, let's look at a last example of path:

.. ipython:: python

    from baron.finder import position_to_path

    fst = parse("a(1)")

    position_to_path(fst, 1, 1)
    position_to_path(fst, 1, 2)
    position_to_path(fst, 1, 3)
    position_to_path(fst, 1, 4)

By the way, out of bound positions are handled gracefully:

.. ipython:: python

    print(position_to_node(fst, -1, 1))
    print(position_to_node(fst, 1, 0))
    print(position_to_node(fst, 1, 5))
    print(position_to_node(fst, 2, 4))


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
