#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='baron',
      version='0.1.2',
      description='Full Syntax Tree for python to make writing refactoring code a realist task',
      author='Laurent Peuch',
      long_description=open("README.md", "r").read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/baron',
      install_requires=['rply'],
      packages=['baron'],
      license='lgplv3+',
      scripts=[],
      keywords='ast fst refactoring syntax tree',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 2 :: Only',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Topic :: Software Development',
                   'Topic :: Software Development :: Code Generators',
                   'Topic :: Software Development :: Libraries',
                   ],
      )
