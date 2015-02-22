#!/usr/bin/env python
from __future__ import print_function
from functools import wraps
from random import shuffle
from sequence import *

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

@Test
def empty():
    test = []
    assert recursiveLargestSequence(test) is 0
    assert iterativeLargestSequence(test) is 0

@Test
def one():
    test = [0]
    assert recursiveLargestSequence(test) is 1
    assert iterativeLargestSequence(test) is 1

@Test
def negatives():
    test = [-1,-2,-3,-4, -100, 101, -50]
    shuffle(test)
    assert recursiveLargestSequence(test) is 4, recursiveLargestSequence(test)
    assert iterativeLargestSequence(test) is 4

@Test
def positives():
    test = [1, 2, 3, 4, 100, 101, 50]
    shuffle(test)
    assert recursiveLargestSequence(test) is 4
    assert iterativeLargestSequence(test) is 4

@Test
def nearby():
    test = [-2, -1, 1, 2, 3, 4, 6, 7, 8, 10, 11]
    shuffle(test)
    assert recursiveLargestSequence(test) is 4
    assert iterativeLargestSequence(test) is 4


@Test
def mixedPositiveNegative():
    test = [-3, -2, -1, 0, 1, 2, 3, 100, 101, 50, 60]
    shuffle(test)
    assert recursiveLargestSequence(test) is 7
    assert iterativeLargestSequence(test) is 7

@Test
def scientificInts():
    base = 10*100000
    test = [base, base+1, base+2, base-1, base-2, 10, 15, 20]
    shuffle(test)
    assert recursiveLargestSequence(test) is 5
    assert iterativeLargestSequence(test) is 5

def main():
    empty()
    one()
    negatives()
    positives()
    nearby()
    mixedPositiveNegative()
    scientificInts()

main()