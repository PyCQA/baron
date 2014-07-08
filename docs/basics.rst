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

    source_code = "def f(x = 1):\n    return x\n"
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

    dumps(parse("a   =   1"))


Helpers
-------

Baron also provides 3 helper functions `show`, `show_file` and
`show_node` to explore the FST (in iPython for example). Those functions
will print a formatted version of the FST so you can play with it to
explore the FST and have an idea of what you are playing with.

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

