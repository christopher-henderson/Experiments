from collections import OrderedDict

#===============================================================================
# Write a function that returns the position of the
# first, non-repeating, character within a given string input.
#===============================================================================

def firstUniqueOfCollection(collection):
    invertedIndex = OrderedDict()
    for index,element in enumerate(collection):
        if element not in invertedIndex:
            invertedIndex[element] = {'index': index, 'count': 1}
        else:
            invertedIndex[element]['count'] += 1
    for element,metaData in invertedIndex.items():
        if metaData['count'] is 1:
            return metaData['index']
    else:
        return -1