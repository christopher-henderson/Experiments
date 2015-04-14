try:
    from Queue import Queue
except ImportError:
    from queue import Queue

'''
Write a function that returns the position of the
first, non-repeating, character within a given string input.

O(n)

Note: Dyanmic languages strike again, so this will work with
any subscriptable, iterable, object and not just strings.
'''

def firstUniqueOfCollection(collection):
    isUnique = dict()
    metaDataQueue = Queue()
    for index,element in enumerate(collection):
        if element not in isUnique:
            isUnique[element] = True
            metaDataQueue.put({'element': element, 'index': index})
        else:
            isUnique[element] = False
    while not metaDataQueue.empty():
        record = metaDataQueue.get()
        if isUnique[record['element']]:
            return record['index']
    else:
        return -1
