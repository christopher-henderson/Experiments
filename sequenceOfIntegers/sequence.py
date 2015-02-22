'''
@author: Christopher Henderson (chris@chenderson.org)
'''

def recursiveLargestSequence(numbers):
    unorderedSet = set(numbers)
    tailsOfSequences = set()
    largest = 0
    #===========================================================================
    # Only values that have NOT been placed into the tailsOfSequences set are candidates
    # for being the head of a sequence.
    #===========================================================================
    headsOfSequences = (num for num in unorderedSet if num not in tailsOfSequences)
        
    def recurseSequenceByStride(integer, stride):
        if integer + stride not in unorderedSet:
            return 0
        else:
            tailsOfSequences.add(integer)
            return recurseSequenceByStride(integer + stride, stride) + 1

    for number in headsOfSequences:
        currentSize = 1
        #=======================================================================
        # Add the integers above 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(number, 1)
        #=======================================================================
        # Add the integers bellow 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(number, -1)
        if currentSize > largest:
            largest = currentSize
    return largest

def iterativeLargestSequence(numbers):
    unorderedSet = set(numbers)
    tailsOfSequences = set()
    largest = 0
    currentSize = 0
    #===========================================================================
    # Only values that have NOT been placed into the tailsOfSequences set are candidates
    # for being the head of a sequence.
    #===========================================================================
    headsOfSequences = (num for num in unorderedSet if num not in tailsOfSequences)
    for number in headsOfSequences:
        currentSize = 1
        sequenceContinues = True
        nextNumber = number
        while sequenceContinues:
            nextNumber += 1
            if nextNumber in unorderedSet:
                currentSize += 1
                tailsOfSequences.add(nextNumber)
            else:
                sequenceContinues = False
        sequenceContinues = True
        nextNumber = number - 1
        while sequenceContinues:
            if nextNumber in unorderedSet:
                currentSize += 1
                tailsOfSequences.add(nextNumber)
                nextNumber -= 1
            else:
                sequenceContinues = False
        if currentSize > largest:
            largest = currentSize
    return largest