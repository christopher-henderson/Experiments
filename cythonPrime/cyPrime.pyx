from cpython.array cimport array
from cpython cimport bool
from libc.stdlib cimport malloc,free
from math import sqrt

def prime(int ceiling):
    cdef unsigned int *primes = <unsigned int *>malloc(ceiling * sizeof(unsigned int))
    if not primes:
        raise MemoryError('Failed to allocate memory for the primes array.')
    cdef unsigned int primesFound
    cdef unsigned int n
    cdef double mid
    cdef bool prime
    n = 3
    primesFound = 1
    while primesFound < ceiling:
        prime = True
        mid = sqrt(n)
        for div in range(ceiling):
            if primes[div] > mid:
                break
            elif n % primes[div] is 0:
                prime = False
                break
        if prime:
            primes[primesFound] = n
            primesFound += 1
        n += 2
    try:
        return primes[-1]
    finally:
        free(primes)
