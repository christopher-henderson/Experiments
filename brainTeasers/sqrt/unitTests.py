#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from functools import wraps
from sqrt import sqrt
from math import sqrt as builtinSqrt

assertion = 0
exception = 0
passed = 0

def Test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        global assertion
        global exception
        global passed
        try:
            function(*args, **kwargs)
        except Exception as e:
            if isinstance(e, AssertionError):
                assertion += 1
                print ("ASSERTION: {FUNC}: {ERROR}".format(FUNC=function.__name__, ERROR=e))
            else:
                exception += 1
                print ("EXCEPTION: {FUNC}: {ERROR}".format(FUNC=function.__name__, ERROR=e))
        else:
            print ("PASSED: {FUNC}".format(FUNC=function.__name__))
    return wrapper

def withinTolerance(a, b, tolerance=1/10**9):
    return a//tolerance == b//tolerance

@Test
def testRange():
    assert all(withinTolerance(sqrt(x), builtinSqrt(x)) for x in xrange(100000))

def main():
    testRange()

main()