#!/usr/bin/env python
from cyPrime import CyPrime
from pyPrime import PyPrime
from time import time

# Testing done on a 4.7 GHz i7, Fedora 20

# One million primes in ~1.8 seconds.
start = time()
print CyPrime(1000000)
print (time()-start)

# One million primes in ~56.8 seconds.
start = time()
print PyPrime(1000000)
print (time()-start)
