Introduction
============

Baron is a FST for Python, a Full Syntax Tree. By opposition to an AST which
drops some syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the operation
<code>ast\_to\_code(code\_to\_ast(source\_code)) == source\_code</code>.

Why is this important?
======================

The usage of a FST might not be obvious at first sight so let's consider a
series of problems to illustrate it. Let's say that you want to write a program that will:

* rename a variable in a source file... without clashing with things that are not a variable (example: stuff inside a string)
* inline a function/method
* extract a function/method from a series of line of code
* split a class into several classes
* split a file into several modules
* convert your whole code base from one ORM to another
* do custom refactoring operation not implemented by IDE/rope
* implement the class browser of smalltalk for python (the whole one where you can edit the code of the methods, not just showing code)

It is very likely that you will end up with the awkward feeling of writing
clumpsy weak code that is very likely to break because you didn't though about
all the annoying special cases and the formatting keeps bothering you. You may
end up playing with [ast.py](http://docs.python.org/2/library/ast.html) until
you realize that it removes too much information to be suitable for those
situations. You will probably ditch this task as simple too complicated and
really not worth the effort. You are missing a good abstraction that will take
care of all of the code structure and formatting for you so you can concentrate
on your task.

The FST tries to be this abstraction. With it you can now work on a tree which
represents your code with its formatting. Moreover, since it is the exact
representation of your code, modifying it and converting it back to a string
will give you back your code only modified where you have modified the tree.

Said in another way, what I'm trying to achieve with Baron is a paradigm change in
which writing code that will modify code is now a realist task that is worth
the price (I'm not saying a simple task, but a realist task, it's still a
complex task).

Other
-----

Having a FST (or at least a good abstraction build on it) also makes it easier
to do code generation and code analysis while those two operations are already
quite feasible (using [ast.py](http://docs.python.org/2/library/ast.html) for
example and a templating engine).

Some technical details
======================

Baron produces a FST in the form of JSON (and by JSON I mean Python lists
and dicts that can be dumped into JSON) for maximum interoperability.

Baron FST is quite similar to Python AST with some modifications to be more
intuitive to humans, since Python AST has been made for CPython interpreter.

Since playing directly with JSON is a bit raw I'm going to build an abstraction
on top of it that will looks like BeautifulSoup/jQuery.

State of the project
====================

Currently, Baron has been tested on the top 100 projects and the FST converts
back exactly into the original source code. So, it can be considered quite
stable, but it is far away from having been battle tested.

Since the project is very young and no one is already using it except my
project, I'm open to modifications of the FST nodes but I will become
conversative very fast once it gets some adoption and will probably accept to
modify it only once or two in the future with clear indications on how to
migrate.

Installation
============

    pip install baron

Usage
=====

```python
from baron import parse, dumps

ast = parse(source_code_string)
source_code_string == dumps(ast)
```

Documentation
=============

At the moment Baron doesn't have any documentation yet. The usage of the only
2 functions provided by Baron is shown above. Apart from that, Baron provides 2
helper functions to explore the FST (in iPython for example). Example:

```python
from baron.helpers import show, show_file

show(string)
show_file(file_path)
```

Those 2 functions will print a formated version of the FST so you can play with
it to explore the FST and have an idea of what you are playing with. Example:

```python
In [5]: from baron.helpers import show

In [6]: show("a +  b")
[
    {
        "first_formatting": [
            {
                "type": "space", 
                "value": " "
            }
        ], 
        "value": "+", 
        "second_formatting": [
            {
                "type": "space", 
                "value": "  "
            }
        ], 
        "second": {
            "type": "name", 
            "value": "b"
        }, 
        "type": "binary_operator", 
        "first": {
            "type": "name", 
            "value": "a"
        }
    }, 
    {
        "indent": "", 
        "formatting": [], 
        "type": "endl", 
        "value": "\n"
    }
]
```

Every node has a <code>type</code> key and all nodes of the same type share the same
structure (if you find that it is not the case, please open an issue). And
nearly all nodes have a <code>value</code> key (except the obvious one that
never change like 'pass') that represents the data.

The <code>*\_formatting</code> value represents the formatting of the node. They
are always around syntax element of Python, here, the "+" (the only exception
to this rules are string since you code things like that in Python:
<code>"a" ru'b' "cd" """ef"""</code>). The translation
looks like this:

    a +  b
    |||| |
    first
     ||| |
    first_formatting
      || |
    value|
       | |
    second_formatting
         |
    second

The exact way to render a node can be find in the [code of the dumps
function](https://github.com/Psycojoker/baron/blob/master/baron/dumper.py).

If there isn't any "\n" at the end of the parsed string, Baron will add one to
respect Python grammar. This is the <code>endl</code> node here.

Tests
=====
Run either `py.test tests/` or `nosetests` in the baron directory.

Misc
====
[Old blog post announcing the project.](http://worlddomination.be/blog/2013/the-baron-project-part-1-what-and-why.html) Not that much up to date.
