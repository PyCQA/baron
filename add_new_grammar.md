# How to modify what Baron can parse

This is a todo list of things to do to allows baron to parse new syntax.

This is the full version, for minor things like adding a new binary operator (like the "@" for matrix multiplication) this is not needed.

# Checklists

### Preparation

- [ ] first of all start by comparing [the grammar from python 2.7](https://docs.python.org/2/reference/grammar.html) with the [targeted version](https://docs.python.org/3.7/reference/grammar.html) (also available in https://github.com/PyCQA/baron/tree/master/grammar)
- [ ] check the reference page here https://baron.readthedocs.io/en/latest/grammar.html to see if things are already planned
- [ ] look at [baron's grammar](https://github.com/PyCQA/baron/blob/master/grammar/baron_grammar) to check if it's not colyding with something already done (very low chance)
- [ ] does the lexer needs to be modified? This is the case for new keywords and new statements
- [ ] be mentally prepared that you'll need to write tests for everything

### Modification

Lexer:

- [ ] if you need to modify the lexer, stars with it, check all the lexer steps (found here: https://github.com/PyCQA/baron/blob/master/baron/baron.py#L69, the correct line might change in the futur, it's the tokenize function)
    - `split` only needs to be modified if python ever introduce new character like "?" for example
    - `group` is if 2 characters needs to be merged like "?" and "="
    - `_tokenize` is for new token, obviously, like new keywords or new grouped characters
    - `space_group` will need to be modified for new keywords or statement, it's quite tricky, it's to group space on neighbour tokens (they will be unfold during grammar parsing) following the general rules of "a node needs to be responsible for its formatting"
    - `inner_group` is a variation of the previous one, it's for the case of tokens between `() [] {}`
    - `mark_indentation` is to handle inserting `IDENT`/`DEDENT` tokens, it very unlikely you'll ever need to work on this one except if python includes new statements (like the `with` statement)

- [ ] have tests for everything regarding the lexer (if possible in a TDD fashion)

Grammar:

The hardest part is going to be to correctly design the extension of the tree with new or by modifying existing nodes (if needed).

Before anything: RedBaron (and not Baron) is an API design project to make writing code that analyse and modify source code as easy as possible, Baron is here to support this task, this mean that this a tree designed to be intuitive to human, no easy to handle for interpreters.

Therefor, when you design a modification or an addition to the tree, you need to answer to the question: what will be the easiest to handle and the more intuitive for humans.

Here are some general advices:

- when that makes sens, prefer flat structure with lower number of nodes instead of sub nodes. For example: for the "async" keyword, extend the related nodes instead of creating a subnode
- prefer lists other single-child series of branches of a tree, for example, the python code "a.b.c.d" shouldn't be structured as "d->c->b->a" like in ast.py but as "[a, b, c, d]"
- uses attributes and nodes name as close as possible to python keywords and what is used in the python community (and close to the grammar)

Regarding the implementation:

- [ ] try to find the good file in which to put your code, the name and content should be enough for that https://github.com/PyCQA/baron/tree/master/baron
- [ ] write/update tests for everything regarding producing the new additions to the tree
- [ ] implement the new grammar (if relevant)
- [ ] modifying the rendering tree in [render.py](https://github.com/PyCQA/baron/blob/master/baron/render.py)
- [ ] write rendering and, if needed, rendering after modification, tests for everything here https://github.com/PyCQA/baron/blob/master/tests/test_dumper.py

And you should be good, congratz if you reached this point!

### Completion, documentation

- [ ] modify the reference page https://baron.readthedocs.io/en/latest/grammar.html
- [ ] [modify baron's grammar](https://github.com/PyCQA/baron/blob/master/grammar/baron_grammar)
- [ ] consider implementing the new additions in [RedBaron](https://github.com/pycqa/redbaron)
- [ ] udpate CHANGELOG
