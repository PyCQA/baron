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

.. image:: grammar-python-2.7-3.6-diff-1.png
