from cpython.array cimport array
from cpython cimport bool
from math import sqrt

def prime(int ceiling):
    primes = [2]
    cdef int n
    cdef double mid
    cdef bool prime
    n = 3
    while len(primes) < ceiling:
        prime = True
        mid = sqrt(n)
        for div in primes:
            if div > mid:
                break
            elif n%div is 0:
                prime = False
                break
        if prime:
            primes.append(n)
        n += 2
    return primes[-1]
