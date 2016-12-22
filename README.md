Introduction
============

Baron is a Full Syntax Tree (FST) library for Python. By opposition to an [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) which
drops some syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the operation
<code>fst\_to\_code(code\_to\_fst(source\_code)) == source\_code</code>.

Installation
============

    pip install baron

Basic Usage
===========

```python
from baron import parse, dumps

fst = parse(source_code_string)
source_code_string == dumps(fst)
```

Except if you want to do low level things, **use
[RedBaron](https://github.com/PyCQA/redbaron) instead of using Baron
directly**. Think of Baron as the "bytecode of python source code" and RedBaron
as some sort of usable layer on top of it.

If you don't know what Baron is or don't understand yet why it might be
useful for you, read the [« Why is this important? » section](#why-is-this-important).

Documentation
=============

Baron documentation is available on [Read The Docs](http://baron.readthedocs.io/en/latest/).

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
clumpsy weak code that is very likely to break because you didn't thought about
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
the price (I'm not saying a simple task, but a realistic one: it's still a
complex task).

Other
-----

Having a FST (or at least a good abstraction build on it) also makes it easier
to do code generation and code analysis while those two operations are already
quite feasible (using [ast.py](http://docs.python.org/2/library/ast.html) 
and a templating engine for example).

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
project, I'm open to changes of the FST nodes but I will quickly become
conservative once it gets some adoption and will probably accept to
modify it only once or twice in the future with clear indications on how to
migrate.

**Baron is targeting python 2.[67]**. It has not been tested on python3 but
should be working for most parts (except the new grammar like <code>yield from</code>,
obviously). Baron **runs** under python 2 and python 3.

Tests
=====
Run either `py.test tests/` or `nosetests` in the baron directory.

Community
=========

You can reach us on [irc.freenode.net#baron](https://webchat.freenode.net/?channels=%23baron) or [irc.freenode.net##python-code-quality](https://webchat.freenode.net/?channels=%23%23python-code-quality).

Code of Conduct
===============

As a member of [PyCQA](https://github.com/PyCQA), Baron follows its [Code of Conduct](http://meta.pycqa.org/en/latest/code-of-conduct.html).

Misc
====
[Old blog post announcing the project.](http://worlddomination.be/blog/2013/the-baron-project-part-1-what-and-why.html) Not that much up to date.
