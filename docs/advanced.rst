Advanced Usage
==============

The topics presented here are less often needed but are still very useful.

Locate a Node
-------------

Since Baron produces a tree, a path is sufficient to locate univocally
a node in the tree. A common task where a path is involved is when
translating a position in a file (a line and a column) into a node of
the FST.

Baron provides 2 helper functions for that:

* :file:`position_to_node(fst, line, column)`
* :file:`position_to_path(fst, line, column)`

Both take a FST tree as first argument, then the line number and the
column number. Line and column numbers **start at 1**, like in a text
editor.

:file:`position_to_node` returns an FST node. This is okay if you only
want to know which node it is but not enough to locate the node in the
tree. Indeed, there can be mutiple identical nodes within the tree.

That's where :file:`position_to_path` is useful. It returns a list of
int and strings which represent either the key to take in a Node or the
index in a ListNode. For example: :file:`["target", "value", 0]`)

Let's first see the difference between the two functions:

.. ipython:: python

    from baron import parse
    from baron.path import position_to_node, position_to_path
    from baron.helpers import show_node

    some_code = """from baron import parse\nfrom baron.helpers import show_node\nfst = parse("a = 1")\nshow_node(fst)"""
    print some_code

    tree = parse(some_code)

    node = position_to_node(tree, (3, 8))
    show_node(node)
    path = position_to_path(tree, (3, 8))
    path

The first one gives the node and the second one the node's path in the
tree. The latter tells you that to get to the node, you must take the
4th index of the root ListNode, followed twice by the "value" key of
first the "assignment" Node and next the "atomtrailers" Node. Finally,
take the 0th index in the resulting ListNode:

.. ipython:: python

    show_node(tree[4]["value"]["value"][0])

Neat. This is so common that there is a function to do that:

.. ipython:: python

    from baron.path import path_to_node

    show_node(path_to_node(tree, path))

With the two above, that's a total of three functions to locate a node.

You can also locate easily a "constant" node like a left parenthesis in
a :file:`funcdef` node:

.. ipython:: python

    from baron.path import position_to_path

    fst = parse("a(1)")

    position_to_path(fst, (1, 1))
    position_to_path(fst, (1, 2))
    position_to_path(fst, (1, 3))
    position_to_path(fst, (1, 4))

By the way, out of bound positions are handled gracefully:

.. ipython:: python

    print(position_to_node(fst, (-1, 1)))
    print(position_to_node(fst, (1, 0)))
    print(position_to_node(fst, (1, 5)))
    print(position_to_node(fst, (2, 4)))


Bounding Box
------------

Sometimes you want to know what are the left most and right most
position of a rendered node or part of it. It is not a trivial task
since you do not know easily each rendered line's length. That's why
baron provides two helpers:

* :file:`node_to_bounding_box(fst)`
* :file:`path_to_bounding_box(fst, path)`

Examples are worth a thousand words so:

.. ipython:: python

    from baron.path import node_to_bounding_box, path_to_bounding_box
    from baron import dumps

    fst = parse("a(1)\nb(2)")

    fst
    print dumps(fst)
    node_to_bounding_box(fst)
    path_to_bounding_box(fst, [])

    fst[0]
    print dumps(fst[0])
    node_to_bounding_box(fst[0])
    path_to_bounding_box(fst, [0])

    fst[0]["value"]
    print dumps(fst[0]["value"])
    node_to_bounding_box(fst[1])
    path_to_bounding_box(fst, [1])

    fst[0]["value"][1]
    print dumps(fst[0]["value"][1])
    node_to_bounding_box(fst[0]["value"][1])
    path_to_bounding_box(fst, [0, "value", 1])

    fst[0]["value"][1]["value"]
    print dumps(fst[0]["value"][1]["value"])
    node_to_bounding_box(fst[0]["value"][1]["value"])
    path_to_bounding_box(fst, [0, "value", 1, "value"])

The bounding box's `top_left` and `bottom_right` positions follow the
same convention as for when locating a node: the line and column start
at 1.

As you can see, the major difference between the two functions is that
:file:`node_to_bounding_box` will always give a left position of
:file:`(1, 1)` since it considers you want the bounding box of the whole
node while :file:`path_to_bounding_box` takes the location of the node
in the fst into account.
