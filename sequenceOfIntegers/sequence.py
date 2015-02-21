'''
@author: Christopher Henderson (chris@chenderson.org)
'''

def recursiveLargestSequence(numbers):
    unorderedSet = set(numbers)
    tailsOfSequences = set()
    largest = 0
    currentSize = 0
    #===========================================================================
    # Only values that have NOT been placed into the tailsOfSequences set are candidates
    # for being the head of a sequence.
    #===========================================================================
    headsOfSequences = (num for num in unorderedSet if num not in tailsOfSequences)

    def recurseSequence(integer):
        if integer + 1 not in unorderedSet:
            result = 1
        else:
            result = recurseSequence(integer + 1) + 1
        tailsOfSequences.add(integer)
        return result

    for number in headsOfSequences:
        currentSize = recurseSequence(number)
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
        if currentSize > largest:
            largest = currentSize
    return largest