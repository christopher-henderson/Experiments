#!/usr/bin/env python
from __future__ import print_function
from functools import wraps
from integerPalendrome import *

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
def PositiveTestRange():
    assert all(isPalendrome(getNextPalendrome(number)) for number in range(10**5)), "Values within range 0...100,000 failed to evaluate to a palendrome."

@Test
def NegativeRestRange():
    assert all(isPalendrome(getNextPalendrome(number)) for number in range(-10**5, 0)), "Values within range -100,000...0 failed to evaluate to a palendrome."

@Test
def TestScientificIntegers():
    #===========================================================================
    # 1001 digits long.
    #===========================================================================
    assert isPalendrome(getNextPalendrome(10**1000))
    #===========================================================================
    # 10001 digits long.
    #===========================================================================
    assert isPalendrome(getNextPalendrome(10**10000))

def main():
    PositiveTestRange()
    NegativeRestRange()
    TestScientificIntegers()

main()