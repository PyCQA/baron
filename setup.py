#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(name='baron',
      version='0.6.3',
      description='Full Syntax Tree for python to make writing refactoring code a realist task',
      author='Laurent Peuch',
      long_description=read_md("README.md") + "\n\n" + open("CHANGELOG", "r").read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/PyCQA/baron',
      install_requires=['rply'],
      packages=['baron'],
      license='lgplv3+',
      scripts=[],
      keywords='ast fst refactoring syntax tree',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Topic :: Software Development',
          'Topic :: Software Development :: Code Generators',
          'Topic :: Software Development :: Libraries',
      ],
      )
