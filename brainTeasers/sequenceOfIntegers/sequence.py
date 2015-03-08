'''
@author: Christopher Henderson (chris@chenderson.org)
'''

def recursiveLargestSequence(numbers):
    #===========================================================================
    # Growth function: n + sum(size of sequences)
    # Worst case: 2n
    # O(n)
    #===========================================================================
    largest = 0
    setCopy = set(numbers)
    def recurseSequenceByStride(integer, stride):
        candidate = integer + stride
        if candidate not in setCopy:
            return 0
        else:
            setCopy.remove(candidate)
            return recurseSequenceByStride(candidate, stride) + 1

    while len(setCopy) is not 0:
        candidate = setCopy.pop()
        currentSize = 1
        #=======================================================================
        # Add the integers above 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(candidate, 1)
        #=======================================================================
        # Add the integers below 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(candidate, -1)
        if currentSize > largest:
            largest = currentSize
    return largest

def iterativeLargestSequence(numbers):
    #===========================================================================
    # Growth function: n + sum(size of sequences)
    # Worst Case: 2n
    # O(n)
    #===========================================================================
    setCopy = set(numbers)
    largest = 0
    while len(setCopy) is not 0:
        number = setCopy.pop()
        currentSize = 1
        sequenceContinues = True
        nextNumber = number
        #=======================================================================
        # Add the integers above 'number'.
        #=======================================================================
        while sequenceContinues:
            nextNumber += 1
            if nextNumber in setCopy:
                currentSize += 1
                setCopy.remove(nextNumber)
            else:
                sequenceContinues = False
        sequenceContinues = True
        nextNumber = number
        #=======================================================================
        # Add the integers below 'number'.
        #=======================================================================
        while sequenceContinues:
            nextNumber -= 1
            if nextNumber in setCopy:
                currentSize += 1
                setCopy.remove(nextNumber)
            else:
                sequenceContinues = False
        if currentSize > largest:
            largest = currentSize
    return largest