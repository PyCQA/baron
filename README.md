Introduction
============

Baron is a Full Syntax Tree (FST) library for Python. By opposition to an [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) which
drops some syntax information in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantees the operation
<code>fst\_to\_code(code\_to\_fst(source\_code)) == source\_code</code>.

Roadmap
=======

Current roadmap is as boring as needed:

* bug fixs
* new small features (walker pattern, maybe code generation) and performance improvement.

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

Unless you want to do low level things, **use
[RedBaron](https://github.com/PyCQA/redbaron) instead of using Baron
directly**. Think of Baron as the "bytecode of python source code" and RedBaron
as some sort of usable layer on top of it.

If you don't know what Baron is or don't understand yet why it might be
useful for you, read the [« Why is this important? » section](#why-is-this-important).

Documentation
=============

Baron documentation is available on [Read The Docs](http://baron.readthedocs.io/en/latest/).

Contributing
============

If you want to implement new grammar elements for newer python versions, here
are the documented steps for that:
https://github.com/PyCQA/baron/blob/master/add_new_grammar.md

Also note that reviewing most grammar modifications takes several hours of
advanced focusing (we can't really afford bugs here) so don't despair if you PR
seems to be hanging around, sorry for that :/

And thanks in advance for your work!

Financial support
=================

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
--------------


[![badge with number of supporters at tier I like this, keep going!](https://opencollective.com/redbaron/tiers/i-like-this,-keep-going!/badge.svg)
![badge with number of supporters at tier it looks cool!](https://opencollective.com/redbaron/tiers/it-looks-cool!/badge.svg)
![badge with number of supporters at tier Oh god, that saved me so much time!](https://opencollective.com/redbaron/tiers/oh-god,-that-saved-me-so-much-time!/badge.svg)](https://opencollective.com/redbaron/tiers/)


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
end up playing with [ast.py](https://docs.python.org/3/library/ast.html) until
you realize that it removes too much information to be suitable for those
situations. You will probably ditch this task as simply too complicated and
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
quite feasible (using [ast.py](https://docs.python.org/3/library/ast.html) 
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

Baron is supporting python 2 grammar and up to python 3.7 grammar.

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
