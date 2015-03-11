from __future__ import division

def sqrt(x, guess=1):
    '''
    Implemented using Newton's Method.
    '''
    #===========================================================================
    # When calculating the square root for a range
    # of integers from 0...1000000 the average number
    # of iterations before maximum precision of the algorithm is
    # reached is 15.0124850125
    #===========================================================================
    if x < 0:
        raise ValueError('math domain error')
    if x == 0:
        return 0.0
    newtonEstimation = lambda a: (x/a + a)/2
    currentGuess = newtonEstimation(guess)
    previousGuess = guess
    while previousGuess != currentGuess:
        previousGuess = currentGuess
        currentGuess = newtonEstimation(currentGuess)
    return currentGuess