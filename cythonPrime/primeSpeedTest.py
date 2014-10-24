#!/usr/bin/env python
from cyPrime.cyPrime import prime as cyPrime
from pyPrime.pyPrime import prime as pyPrime
from time import time

start = time()
print cyPrime(1000000)
print (time()-start)

start = time()
print pyPrime(1000000)
print (time()-start)
