Introduction
============

Baron is a FST for python, a Full Syntax Tree. By opposition to an AST which
drop some syntax informations in the process of its creation (like empty lines,
comments, formatting), a FST keeps everything and guarantee the operation
<code>ast\_to\_code(code\_to\_ast(source\_code)) == source\_code</code>.

Installation
============

NOT WORKING YET.

    pip install baron

Usage
=====

```python
from baron import parse, dumps

ast = parse(source_code_string)
source_code_string = dumps(ast)
```

Tests
=====
Run either "py.test" or "nosetests" in the baron directory.

Misc
====
[Old blog post announcing the project.](http://worlddomination.be/blog/2013/the-baron-project-part-1-what-and-why.html) Not that much up to date.
