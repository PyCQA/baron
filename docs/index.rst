Baron
=====

Baron is a Full Syntax Tree (FST) for Python. It represents source code
as a structured tree, easily parsable by a computer. By opposition to an
`Abstract Syntax Tree
<http://en.wikipedia.org/wiki/Abstract_syntax_tree>`_ (AST) which drops
syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the
operation :file:`fst_to_code(code_to_fst(source_code)) == source_code`.

Installation
============

::

    pip install baron

RedBaron
========

There is a good chance that you'll want to use `RedBaron
<https://github.com/Psycojoker/redbaron>`_ instead of using Baron directly.
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

Rendering the FST
-----------------

Baron renders the FST back into source code by following the
instructions given by the :file:`nodes_rendering_order` dictionary. It
gives, for everynode FST node, the order in which the node must be rendered.

.. ipython:: python

    from baron import nodes_rendering_order
    from baron.helpers import show_node

    nodes_rendering_order["name"]
    show_node(parse("a_name")[0])
    nodes_rendering_order["tuple"]
    show_node(parse("(a_name,another_name,yet_another_name)")[0])
    nodes_rendering_order["comma"]

For a "name" node, it is a list containing an unique tuple but it can
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
* A :file:`constant` node is a leaf of the FST tree. The second column always
  contains a string which is outputted directly. Compared to a :file:`key`
  node containing a string, the :file:`constant` node is identical for every
  instance of the nodes (e.g. the left parenthesis character :file:`(` in
  a function call node of the :file:`def` keyword of a function definition)
  while the :file:`key` node's value can change (e.g.  the name of the
  function in a function
  call node).


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
see in the next section, it is not the case thanks to the third column
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
latter because only the latter has a default assignment "= 1".

.. ipython:: python

    dumps(fst[0]["arguments"][0])

    dumps(fst[0]["arguments"][2])

We will conclude here now that we have seen an example of every aspect
of FST rendering. Understanding everything is not required to use Baron
since :file:`dumps` handles all the complexity.

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

That's where :file:`position_to_path` is useful. It returns a dictionary
in JSON format which contains 3 values:

* the :file:`path` key contains the path: a list of int and strings which
  represent either the key to take in a Node or the index in a ListNode
  (e.g. "target", "value", 0)
* the :file:`type` key tells the type of the FST node (e.g.
  "function", "assignment", "class")
* the :file:`position_in_rendering_list` key is the rendering position
  of the node compared to its parent node. This is especially needed
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

The first one gives the node and the second one the node path. Both also give
its type but what does the keys in the path correspond to exactly? The path
tells you that to get to the node, you must take the 4th index of the root
ListNode, followed twice by the "value" key of first the "assignment" Node and
next the "atomtrailers" Node. Finally, take the 0th index in the resulting
ListNode:

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
are located in the rendering dictionary:

.. ipython:: python

    from baron import nodes_rendering_order

    nodes_rendering_order["call"]

    nodes_rendering_order["call"][1]

Because the parenthesis is a constant, there is no specific node for the
parenthesis. So the path can only go as far as the parent node, here "call",
and show you the position in the rendering dictionary.

For example, it allows you to distinguish the left and right parenthesis in a
call.

.. ipython:: python

    position_to_path(tree, 3, 20)

    nodes_rendering_order["call"][5]

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

RenderWalker
============

Internally, Baron uses a walker to traverse a FST tree, it's a generic
class that you are free to use. To do so, you inherit from it and
overload the chosen methods. You then launch an instance using it's
:file:`walk` method. Here is how the :file:`Dumper` (called by the
function :file:`dumps`) is written using it:

.. ipython:: python

    from baron.render import RenderWalker

    class Dumper(RenderWalker):
        """Usage: Dumper().dump(tree)"""
        def on_leaf(self, constant, pos, key):
            self.dump += constant
            return self.CONTINUE
        def dump(self, tree):
            self.dump = ''
            self.walk(tree)
            return self.dump

The available methods that you can overload are:

* :file:`before_list` called before encountering a list of nodes
* :file:`after_list` called after encountering a list of nodes
* :file:`before_formatting` called before encountering a formatting list
* :file:`after_formatting` called after encountering a formatting list
* :file:`before_node` called before encountering a node
* :file:`after_node` called after encountering a node
* :file:`before_key` called before encountering a key type entry
* :file:`after_key` called after encountering a key type entry
* :file:`on_leaf` called when encountering a leaf of the FST (can be a constant (like "def" in a function definition) or an actual value like the value a name node)

Every methods has the same signature: :file:`(self, node, render_pos, render_key)`.


Table of Content
================

.. toctree::
   :maxdepth: 2
