from __future__ import division

def sqrt(x, accuracy=13):
    if x < 0:
        raise ValueError('math domain error')
    if x == 0:
        return 0.0
    newtonEstimation = lambda a: (x/a + a)/2
    guess = 1
    for iteration in xrange(accuracy):
        guess = newtonEstimation(guess)
    return guess