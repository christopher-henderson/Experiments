from __future__ import division

def isPalendrome(number):
    if not isinstance(number, str):
        forwards = str(number).replace('-', '')
    else:
        forwards = number.replace('-', '')
    backwards = forwards[-1::-1]
    return forwards == backwards
 
def getNextPalendrome(number):
    if isPalendrome(number):
        #=======================================================================
        # If we are starting on a palendrome then the difference
        # calculated in _calculatedNextPalendrome will always
        # evaluate to 0 and we won't go anywhere. Thus, if we
        # are starting on a palendrome, nudge it up by one and
        # continue on. Note, this is also what handles 0..9.
        #=======================================================================
        result = number + 1
    else:
        result = number
    result = _calculatedNextPalendrome(result)
    if not isPalendrome(result):
        #=======================================================================
        # This is vexxing and most hopefully a placeholder.
        # What is happening is there are a handful of predictable
        # wrong results. These occur with double digit numbers,
        # as well as "turn of the century" numbers. For example:
        # 191...199 will evaluate to 201. I noticed that if we land
        # in one of these cases, then all we have to do is put our
        # value through the palendrome calculator one more time.
        # 
        # This seems a bit sleazy, but is honestly not that expensive
        # considering that _calculatedNextPalendrome is n/2 where n
        # is the length of the number.
        # 
        # Now that we are consistently getting correct answers, the next
        # step may be to construct statistics to see if there is any pattern
        # to the appearance of palendromes on the number line. This
        # may provide insight into the before mentioned trouble cases
        # and lead to a single pass algorithm. But, for now, this
        # gets correct answers and trying to protect against the special
        # cases smells like it would be more egregious than this "hack".
        #=======================================================================
        result = _calculatedNextPalendrome(result)
    return result

def _calculatedNextPalendrome(result):
    #===========================================================================
    # Obtain the order of magnitude of the most signifcant digit.
    #===========================================================================
    upperOrderOfMagnitude = len(str(result).replace('-', '')) - 1
    #===========================================================================
    # Set the order of magnitude of the least significant digit to 0.
    #===========================================================================
    lowerOrderOfMagnitude = 0
    while lowerOrderOfMagnitude < upperOrderOfMagnitude:
        #===========================================================================
        # This loop starts at the outer edges of the given number. As lowerOrderOfMagnitude
        # is incremented and upperOrderOfMagnitude is decremented we begin to move towards
        # the middle of the number.
        #  
        # At each iteration of the loop we pluck out two symmetrical digits within the number
        # and find the difference. If the difference is negative, then add 10 (e.g if left digit is 3
        # and right digit is 9, then 3-9+10=4, which added to 9 will make the right digit equivalent to
        # the left digit).
        # 
        # Take this difference between the left digit and the right digit and multiply it
        # by 10**(current lowest order of magnitude). For example, if on the first pass the difference
        # is 9, then the difference will be 9*10**0 = 9. If on the second pass the difference is 8, then
        # the difference will be 8*10**1 = 80. Increment the ongoing result number by this difference.
        # 
        # Continue while there are symmetrical numbers to consider.
        #===========================================================================
        #=======================================================================
        # Chop off numbers to left of our digit with modulus and then chop off numbers to
        # the right of it with floor division.
        #=======================================================================
        rightDigit = (result % 10**(lowerOrderOfMagnitude+1)) // (10**(lowerOrderOfMagnitude))
        #=======================================================================
        # Chop off numbers to the right of our digit with floor division and chop off numbers to
        # the left of it with modulus.
        #=======================================================================
        leftDigit = (result // 10**upperOrderOfMagnitude) % 10
        difference = leftDigit - rightDigit
        if difference < 0:
            difference += 10
        result += difference*10**(lowerOrderOfMagnitude)
        lowerOrderOfMagnitude += 1
        upperOrderOfMagnitude -= 1
    return result