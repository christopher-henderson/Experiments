#!/usr/bin/env python
from __future__ import print_function
from functools import wraps
from lines import getNumLines

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
    assert getNumLines(()) is 0

@Test
def one():
    assert getNumLines(((1,1),)) is 1

@Test
def axis():
    assert getNumLines(((0,1),)) is 1
    assert getNumLines(((0,1), (0,-1))) is 1
    assert getNumLines(((1,0),)) is 1
    assert getNumLines(((1,0), (-1,0))) is 1

@Test
def origin():
    assert getNumLines(((0,0),)) is 1
    assert getNumLines(((0,0), (0,0), (0,0), (0,0))) is 1
    assert getNumLines(((0,0), (1,1))) is 1
    assert getNumLines(((0,0), (1,1), (1,2))) is 2

@Test
def counterQuadrants():
    assert getNumLines(((1,1), (-1,-1), (2,2), (-2,-2))) is 1
    assert getNumLines(((-1,1), (1,-1))) is 1
    assert getNumLines(((2,2), (-2,-1))) is 2
    assert getNumLines(((-2,2), (2,-1))) is 2

@Test
def scientificInts():
    assert getNumLines(((1+10**10000, 10**10000), (1, 1))) is 2

def main():
    empty()
    one()
    axis()
    origin()
    counterQuadrants()
    scientificInts()

main()
