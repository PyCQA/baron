Grammar reference
=================

This page is here to serve as a reference for the grammar implementation. Baron
started as a python2.7 grammar implementation following `the official
specification for that <https://docs.python.org/2/reference/grammar.html>`_ and
supporting both :file:`print statement` and :file:`print function`.

The evolution path regarding python3* is the adopt the same strategy that
lib2to3 and try to support a combination of both grammar as much as possible.

This page describe the decisions taken regarding this dual support and it's
progress. Hopefully there will be very few conflicting situations.

Current goal is `python 3.6 specification <https://docs.python.org/3.6/reference/grammar.html>`_.

Python 2 and python 3.6 grammar differences
===========================================

As a reference and an overview, here is screenshot of vimdiff showing the difference between python 2.7 and python 3.6 grammar differences.

.. image:: grammar-python-2.7-3.6-diff-1.png

.. image:: grammar-python-2.7-3.6-diff-2.png

.. image:: grammar-python-2.7-3.6-diff-3.png

List of differences
===================

**Some of the diff have been edited to isolate the focused difference of the
section**

Print function
~~~~~~~~~~~~~~

.. image:: ./grammar_diff/print_function.png

Already done since the start.

TODO
----

Typed arguments
~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/typed_args.png

Function return type
~~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/function_return_type.png

Nonlocal statement
~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/nonlocal_statement.png

Exec function
~~~~~~~~~~~~~

.. image:: ./grammar_diff/exec_function.png

*var generalisation
~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/testlist_start_expressiong.png

.. image:: ./grammar_diff/star_expr.png

.. image:: ./grammar_diff/star_expr_in_testlist_comp.png

.. image:: ./grammar_diff/star_expr_in_expr_list.png

Raise from
~~~~~~~~~~

.. image:: ./grammar_diff/raise_from.png

Ellipsis in from import
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/ellipsis_in_from_import.png

New lambda grammar
~~~~~~~~~~~~~~~~~~

I have no idea on what to do with this one yet.

.. image:: ./grammar_diff/new_lambda_grammar.png

.. image:: ./grammar_diff/new_grammar_for_if_cond.png

Remove old list comprehension syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'm not sure on how to handle both situations (and it is needed? Old list
comprehension syntax is like super edgy, I really wonder if anyonne has
actually used that one that?)

.. image:: ./grammar_diff/remove_old_list_comprehension_syntax.png

.. image:: ./grammar_diff/no_more_list_for_rule.png

False|True|None|... are now atoms in the grammar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Do I need to do anything about that?

.. image:: ./grammar_diff/more_atoms.png

Inheritance in class definition uses arglist now
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I have no idea on why this is here but that's easy to change.

.. image:: ./grammar_diff/class_inherit_is_arglist_now.png

Yield From
~~~~~~~~~~

.. image:: ./grammar_diff/yield_from.png








Nothing to do
-------------

Those are things that have been removed from python3 grammar but we still need
to support (and we already do) so we don't have to do anything.

No more commat syntax in except close
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/no_more_commat_in_execption_close.png

No more backquote syntax
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/no_more_backquote_syntax.png

No more '.' '.' '.' in the grammar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./grammar_diff/ellipsis_is_first_class_now_not_needed_anymore.png
