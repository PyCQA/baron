Baron
=====

Baron is a Full Syntax Tree (FST) for Python. It represents source code
as a structured tree, easily parsable by a computer. By opposition to an
`Abstract Syntax Tree
<http://en.wikipedia.org/wiki/Abstract_syntax_tree>`_ (AST) which drops
syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the
operation :file:`fst_to_code(code_to_fst(source_code)) == source_code`.

If you want to understand why this is important, read this:
https://github.com/psycojoker/baron#why-is-this-important

Installation
============

::

    pip install baron

Github (source, bug tracker, etc.)
===================================

https://github.com/psycojoker/baron

RedBaron
========

There is a good chance that you'll want to use `RedBaron
<https://redbaron.readthedocs.org>`_ instead of using Baron directly.
Think of Baron as the "bytecode of python source code" and RedBaron as some
sort of usable layer on top of it, a bit like dom/jQuery or html/Beautifulsoup.

Basic Usage
===========

Baron provides two main functions:

* :file:`parse` to transform a string into Baron's FST;
* :file:`dumps` to transform the FST back into a string.

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

Like said in the introduction, the FST keeps the formatting unlike ASTs.
Here the following 3 codes are equivalent but their formatting is
different. Baron keeps the difference so when dumping back the FST, all
the formatting is respected:

.. ipython:: python

    dumps(parse("a = 1"))

    dumps(parse("a=1"))

    dumps(parse( "a   =   1"))


Helpers
-------

Baron also provides 3 helper functions `show`, `show_file` and
`show_node` to explore the FST (in iPython for example). Those
functions will print a formatted version of the FST so you can play with
it to explore the FST and have an idea of what you are playing with.

Show
~~~~
:file:`show` is used directly on a string:

.. ipython:: python

    from baron.helpers import show

    show("a = 1")

    show("a +=  b")

Show_file
~~~~~~~~~
:file:`show_file` is used on a file path:

::

    from baron.helpers import show_file

    show_file("/path/to/a/file")

Show_node
~~~~~~~~~
:file:`show_node` is used on an already parsed string:

.. ipython:: python

    from baron.helpers import show_node

    fst = parse("a = 1")

    show_node(fst)

Under the hood, the FST is serialized into JSON so the helpers are
simply encapsulating JSON pretty printers.

Locate a Node
-------------

Since Baron produces a tree, a path is sufficient to locate univocally
a node in the tree. A common task where a path is involved is when
translating a position in a file (a line and a column) into a node of
the FST.

Baron provides 2 helper functions for that: :file:`position_to_node` and
:file:`position_to_path`. Both functions take a FST tree as first
argument, then the line number and the column number. Line and column
numbers **start at 1**, like in a text editor.

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


Bounding Box
------------

Sometimes you want to know what are the left most and right most
position of a rendered node or part of it. It is not a trivial task
since you do not know easily the each rendered line's length. That's why
two helpers :file:`node_to_bounding_box` and
:file:`path_to_bounding_box` are provided. Examples are worth a thousand
words so:

.. ipython:: python

    from baron.path import node_to_bounding_box, path_to_bounding_box

    fst = parse("a(1)\nb(2)")

    fst
    node_to_bounding_box(fst)
    path_to_bounding_box(fst, [])

    fst[0]
    node_to_bounding_box(fst[0])
    path_to_bounding_box(fst, [0])

    fst[0]["value"]
    node_to_bounding_box(fst[1])
    path_to_bounding_box(fst, [1])

    fst[0]["value"][1]
    node_to_bounding_box(fst[0]["value"][1])
    path_to_bounding_box(fst, [0, "value", 1])

    fst[0]["value"][1]["value"]
    node_to_bounding_box(fst[0]["value"][1]["value"])
    path_to_bounding_box(fst, [0, "value", 1, "value"])

The bounding box positions follow the same convention as for when
locating a node: the line and column start at 1.

As you can see, the major difference between the two functions is that
:file:`node_to_bounding_box` will always give a left position of
:file:`(1, 1)` since it considers you want the bounding box of the
whole node while :file:`path_to_bounding_box` takes the location of the
node in the fst into account.


Rendering the FST
=================

This section is quite advanced and you will maybe never need to use what
is in here. But if you want to process the whole rendered fst or part of
it as a chunk, please read along since several helpers are provided.

Understanding core rendering
----------------------------

Baron renders the FST back into source code by following the
instructions given by the :file:`nodes_rendering_order` dictionary. It
gives, for every FST node, the order in which the node must be rendered.

.. ipython:: python

    from baron import nodes_rendering_order
    from baron.helpers import show_node

    nodes_rendering_order["name"]
    show_node(parse("a_name")[0])
    nodes_rendering_order["tuple"]
    show_node(parse("(a_name,another_name,yet_another_name)")[0])
    nodes_rendering_order["comma"]

For a "name" node, it is a list containing a unique tuple but it can
contain multiple ones like for a "tuple" node.

To render a node, you just need to render each element of the list one
by one in the given order. As you can see, they are all formatted as a
3-tuple. The first column is the type which is one of the following:

.. ipython:: python

    from baron.render import node_types

    node_types

Apart for the "constant" node, the second column contains the key of the
FST node which must be rendered. The first column explains how that key
must be rendered. We'll see the third column later.

* A :file:`node` node is one of the nodes in the :file:`nodes_rendering_order`
  we just introduced, it is rendered by following the rules mentionned
  here. This is indeed a recursive definition.
* A :file:`key` node is either a branch of the tree if the corresponding FST
  node's key contains another node or a leaf if it contains a string. In
  the former case, it is rendered by rendering its content. In the
  latter, the string is outputted directly.
* A :file:`list` node is like a :file:`key` node but can contain 0, 1 or several
  other nodes. For example, Baron root node is a :file:`list` node since
  a python program is a list of statements. It is rendered by rendering
  each of its elements in order.
* A :file:`formatting` node is similar in behaviour to a :file:`list` node but
  contains only formatting nodes. This is basically where Baron
  distinguish itself from ASTs.
* A :file:`constant` node is a leaf of the FST tree. The second column
  always contain a string which is outputted directly. Compared to
  a :file:`key` node containing a string, the :file:`constant` node is
  identical for every instance of the nodes (e.g. the left parenthesis
  character :file:`(` in a function call node or the :file:`def` keyword
  of a function definition) while the :file:`key` node's value can
  change (e.g. the name of the function in a function call node).
* A :file:`bool` node is a node used exclusively for conditional
  rendering. It's exact use will be explained later on with the tuple's
  third column but the main point for now is to know that they are never
  rendered.


Walktrough
~~~~~~~~~~

Let's see all this is in action by rendering a "lambda" node. First, the
root node is always a "list" node and since we are only parsing one
statement, the root node contains our "lambda" node at index 0:

.. ipython:: python

    fst = parse("lambda x, y = 1: x + y")

    fst[0]["type"]

For reference, you can find the (long) FST produced by the lambda node at the
end of this section.

Now, let's see how to render a "lambda" node:

.. ipython:: python

    nodes_rendering_order["lambda"]

Okay, first the string constant "lambda", then a first_formatting node
which represents the space between the string "lambda" and the variable
"x".

.. ipython:: python

    fst[0]["first_formatting"]

The "first_formatting" contains a list whose unique element is a "space"
node.

.. ipython:: python

    fst[0]["first_formatting"][0]

    nodes_rendering_order["space"]

Which in turn is rendered by looking at the value key of the space node.
It's a string so it is outputted directly.

.. ipython:: python

    fst[0]["first_formatting"][0]["value"]

So far we have outputted "lambda ". Tedious but exhaustive.

We have exhausted the "first_formatting" node so we go back up the tree.
Next is the "list" node representing the arguments:

.. ipython:: python

    fst[0]["arguments"]

Rendering a "list" node is done one element at a time. First
a "def_argument", then a "comma" and again a "def_argument".

.. ipython:: python

    fst[0]["arguments"][0]

    nodes_rendering_order["def_argument"]

The first "def_argument" is rendered by first outputting the content of
a name "key" node, which is string and thus outputted directly:

.. ipython:: python

    fst[0]["arguments"][0]["name"]

Now, we have outputted "lambda x". At first glance we could say we
should render the second element of the "def_argument" node but as we'll
see in the next section, it is not the case because of the third column
of the tuple.

For reference, the FST of the lambda node:

.. ipython:: python

    show_node(fst[0])

Dependent rendering
~~~~~~~~~~~~~~~~~~~

Sometimes, some node elements must not be outputted. In our
"def_argument" example, all but the first are conditional. They are only
rendered if the FST's "value" node exists and is not empty. Let's
compare the two "def_arguments" FST nodes:

.. ipython:: python

    fst[0]["arguments"][0]

    fst[0]["arguments"][2]

    nodes_rendering_order[fst[0]["arguments"][2]["type"]]

The "value" is empty for the former "def_argument" but not for the
latter because it has a default value of "= 1".

.. ipython:: python

    dumps(fst[0]["arguments"][0])

    dumps(fst[0]["arguments"][2])

The rule here is that the third column of a node is one of:
* True, it is always rendered;
* False, it is never rendered;
* A string, it is rendered conditionnally. It is not rendered if the key
  it references is either empty or False. It also must reference an
  existing key. In our example above, it references the existing "value"
  key which is empty in the first case and not empty in the second.

This is how "bool" nodes are never outputted: their third column is
always False.

We will conclude here now that we have seen an example of every aspect
of FST rendering. Understanding everything is not required to use Baron
since several helpers like :file:`render`, :file:`RenderWalker` or
:file:`dumps` handle all the complexity under the hood.

Render Helper
-------------

Baron provides a render function helper which walks recursively the
:file:`nodes_rendering_order` dictionnary for you:

.. autofunction:: baron.render.render

RenderWalker Helper
-------------------

But even easier, Baron provides a walker class whose job is to walk the
fst while rendering it and to call user-provided callbacks at each step:
 
.. autoclass:: baron.render.RenderWalker

Internally, Baron uses the :file:`RenderWalker` for multiple tasks like
for the :file:`dumps` function:

.. ipython:: python

    from baron.render import RenderWalker

    def dumps(tree):
        return Dumper().dump(tree)

    class Dumper(RenderWalker):
        def before_leaf(self, constant, key):
            self.dump += constant

        def dump(self, tree):
            self.dump = ''
            self.walk(tree)
            return self.dump

As you can see it is quite simple since it only needs the
:file:`before_leaf` method.

PathWalker Helper
-----------------

If while walking you need to know the current path of the node, then you
should subclass :file:`PathWalker` instead:

.. autoclass:: baron.path.PathWalker

