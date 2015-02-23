'''
@author: Christopher Henderson (chris@chenderson.org)
'''

def recursiveLargestSequence(numbers):
    #===========================================================================
    # Growth function: n + sum(size of sequences)
    # Worst case: 2n
    # O(n)
    #===========================================================================
    unorderedSet = set(numbers)
    tailsOfSequences = set()
    largest = 0
    headsOfSequences = (num for num in unorderedSet if num not in tailsOfSequences)
        
    def recurseSequenceByStride(integer, stride):
        candidate = integer + stride
        if candidate not in unorderedSet:
            return 0
        else:
            tailsOfSequences.add(candidate)
            return recurseSequenceByStride(candidate, stride) + 1

    for number in headsOfSequences:
        currentSize = 1
        #=======================================================================
        # Add the integers above 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(number, 1)
        #=======================================================================
        # Add the integers below 'number'.
        #=======================================================================
        currentSize += recurseSequenceByStride(number, -1)
        if currentSize > largest:
            largest = currentSize
    return largest

def iterativeLargestSequence(numbers):
    #===========================================================================
    # Growth function: n + sum(size of sequences)
    # Worst Case: 2n
    # O(n)
    #===========================================================================
    unorderedSet = set(numbers)
    tailsOfSequences = set()
    largest = 0
    headsOfSequences = (num for num in unorderedSet if num not in tailsOfSequences)
    for number in headsOfSequences:
        currentSize = 1
        sequenceContinues = True
        nextNumber = number
        #=======================================================================
        # Add the integers above 'number'.
        #=======================================================================
        while sequenceContinues:
            nextNumber += 1
            if nextNumber in unorderedSet:
                currentSize += 1
                tailsOfSequences.add(nextNumber)
            else:
                sequenceContinues = False
        sequenceContinues = True
        nextNumber = number
        #=======================================================================
        # Add the integers below 'number'.
        #=======================================================================
        while sequenceContinues:
            nextNumber -= 1
            if nextNumber in unorderedSet:
                currentSize += 1
                tailsOfSequences.add(nextNumber)
            else:
                sequenceContinues = False
        if currentSize > largest:
            largest = currentSize
    return largest