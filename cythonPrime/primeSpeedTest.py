#!/usr/bin/env python
from timeit import timeit

# Testing done on a 4.7 GHz i7, Fedora 20

# One million primes in ~1.8 seconds.
print (timeit(setup='from cyPrime import CyPrime', stmt='CyPrime(1000000)', number=1))

# One million primes in ~56.8 seconds.
print (timeit(setup='from pyPrime import PyPrime', stmt='PyPrime(1000000)', number=1))
