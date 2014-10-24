#!/usr/bin/env python
#python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Cython Prime Finder',
  ext_modules = cythonize("cyPrime.pyx"),
)
