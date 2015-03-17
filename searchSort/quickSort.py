#!/usr/bin/env python
from __future__ import division

def quickSort(collection):
    if len(collection) <= 1:
        return collection
    middle = collection.pop(len(collection) // 2)
    left = quickSort([item for item in collection if item <= middle])
    right = quickSort([item for item in collection if item > middle])
    return left + [middle] + right

print (quickSort([3,6,5,5,7,1,8]))