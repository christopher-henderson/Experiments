#/usr/bin/env python
from __future__ import division
'''
Created on Feb 16, 2015

@author: Christopher Henderson (chris@chenderson.org)
'''

class NormalizedRational(object):
    '''
        This class normalizes a point so that any other point that can land
        on the same line hashes to the same value.
        
        - All points on the x-axis are converted to (0, 1)
        - All points on the y-axis are converted to (1, 0)
        - The origin remains the origin.
        - All other points have their rational reduced. If the point
            lies within quadrants III or IV then they are flipped to I or II.

        @param int numerator
        @param int denominator
    '''
    def __init__(self, numerator, denominator):
        x_axis = numerator == 0 and denominator != 0
        y_axis = denominator == 0 and numerator != 0
        origin = numerator == 0 and denominator == 0
        if x_axis:
            self.rational = (0, 1)
        elif y_axis:
            self.rational = (1, 0)
        elif origin:
            self.rational = (0, 0)
        else:
            self.rational = self._normalizeRational(numerator, denominator)

    def _normalizeRational(self, numerator, denominator):
            #===================================================================
            # Euclid's algorithm for GCD.
            # https://en.wikipedia.org/wiki/Euclidean_algorithm
            # @TODO research a possibly fast approach.
            #===================================================================
            GCD = abs(numerator)
            tempDenominator = abs(denominator)
            temp = 0
            while (tempDenominator > 0):
                temp = tempDenominator
                tempDenominator = GCD % tempDenominator
                GCD = temp
            return self._foldQuadrantsIIIandIV(numerator//GCD, denominator//GCD)

    def _foldQuadrantsIIIandIV(self, y, x):
        quadrantIII = y < 0 and x < 0
        quadrantIV = y < 0 and x > 0
        if quadrantIII or quadrantIV:
            return (y*-1, x*-1)
        else:
            return (y, x)

    def __eq__(self, other):
        if not isinstance(other, NormalizedRational):
            return False
        return self.rational == other.rational
    
    def __hash__(self):
        return hash(self.rational)

def getNumLines(points):
    lines = set()
    for point in points:
        lines.add(NormalizedRational(point[1], point[0]))
    if NormalizedRational(0, 0) in lines and len(lines) is not 1:
        return len(lines) - 1
    else:
        return len(lines)
