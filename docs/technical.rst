Rendering the FST
=================

This section is quite advanced and you will maybe never need to use
what is in here. But if you want to process the whole rendered fst or
part of it as a chunk, please read along since several helpers are
provided.

Understanding core rendering
----------------------------

Baron renders the FST back into source code by following the
instructions given by the :file:`nodes_rendering_order` dictionary. It
gives, for every FST node, the order in which the node components must be
rendered and the nature of those components.

.. ipython:: python

    from baron import nodes_rendering_order, parse
    from baron.helpers import show_node

    nodes_rendering_order["name"]
    show_node(parse("a_name")[0])
    nodes_rendering_order["tuple"]
    show_node(parse("(a_name,another_name,yet_another_name)")[0])
    nodes_rendering_order["comma"]

For a "name" node, it is a list containing a unique component stored in a tuple
but it can contain multiple ones like for a "tuple" node.

To render a node, you just need to render each element of the list, one
by one, in the given order. As you can see, they are all formatted as
a 3-tuple. The first column is the type which is one of the following:

.. ipython:: python

    from baron.render import node_types

    node_types

With the exception of the "constant" node, the second column contains the key
of the FST node which must be rendered. The first column explains how that key
must be rendered. We'll see the third column later.

* A :file:`node` node is one of the nodes in the
  :file:`nodes_rendering_order` we just introduced, it is rendered by
  following the rules mentionned here. This is indeed a recursive
  definition.
* A :file:`key` node is a branch of the tree that contains another node (a
  python dictionary).
* A :file:`string` node is a leaf of the tree that contains a variable value,
  like the name of a function.
  former case, it is rendered by rendering its content.
* A :file:`list` node is like a :file:`key` node but can contain 0, 1 or
  several other nodes stored in a python list. For example, Baron root node is
  a :file:`list` node since a python program is a list of statements. It is
  rendered by rendering each of its elements in order.
* A :file:`formatting` node is similar in behaviour to a :file:`list`
  node but contains only formatting nodes. This is basically where Baron
  distinguish itself from other ASTs.
* A :file:`constant` node is a leaf of the FST tree. The second column
  always contain a string which is outputted directly. Compared to
  a :file:`string` node, the :file:`constant` node is
  identical for every instance of the nodes (e.g. the left parenthesis
  character :file:`(` in a function call node or the :file:`def` keyword
  of a function definition) while the :file:`string` node's value can
  change (e.g. the name of the function in a function definition node).
* A :file:`bool` node is a node used exclusively for conditional
  rendering. It's exact use will be explained later on with the tuple's
  third column but the main point for now is to know that they are never
  rendered.


Walkthrough
~~~~~~~~~~

Let's see all this is in action by rendering a "lambda" node. First, the
root node is always a "list" node and since we are only parsing one
statement, the root node contains our "lambda" node at index 0:

.. ipython:: python

    fst = parse("lambda x, y = 1: x + y")

    fst[0]["type"]

For reference, you can find the (long) FST produced by the lambda node
at the end of this section.

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

Which in turn is rendered by printing the value of the string of the space
node.

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
a name "string" node:

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

    from baron import dumps

    dumps(fst[0]["arguments"][0])

    dumps(fst[0]["arguments"][2])

The rule here is that the third column of a node is one of:

* True, it is always rendered;
* False, it is never rendered;
* A string, it is rendered conditionnally. It is not rendered if the key it references is either empty or False. It also must reference an existing key. In our example above, it references the existing "value" key which is empty in the first case and not empty in the second.

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

::

    from baron.render import RenderWalker

    def dumps(tree):
        return Dumper().dump(tree)

    class Dumper(RenderWalker):
        def before_constant(self, constant, key):
            self.dump += constant

        def before_string(self, string, key):
            self.dump += string

        def dump(self, tree):
            self.dump = ''
            self.walk(tree)
            return self.dump

As you can see it is quite simple since it only needs the
:file:`before_constant` and the :file:`before_string` methods with the same
exact code.

PathWalker Helper
-----------------

If while walking you need to know the current path of the node, then you
should subclass :file:`PathWalker` instead:

.. autoclass:: baron.path.PathWalker

Here is a succint example of what you should expect when using the
:file:`PathWalker`:

.. ipython:: python

    from baron.path import PathWalker

    fst = parse("a = 1")

    class PathWalkerPrinter(PathWalker):
        def before(self, key_type, item, render_key):
            super(PathWalkerPrinter, self).before(key_type, item, render_key)
            print(self.current_path)

        def after(self, key_type, item, render_key):
            print(self.current_path)
            super(PathWalkerPrinter, self).after(key_type, item, render_key)

    walker = PathWalkerPrinter()
    walker.walk(fst)

Like in the example, don't forget to call the before and after methods
of the parent class. Furthermore, you need to respect the order
specified above, that is:

* Calling :file:`super().before()` should be done before your code using
  the :file:`self.path` attribute.
* Calling :file:`super().after()` should be done after your code using
  the :file:`self.path` attribute.

