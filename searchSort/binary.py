#/usr/bin/env python
from __future__ import division

def binarySearch(collection, target):
    if len(collection) is 0:
        return False
    middle = len(collection) // 2
    if collection[middle] == target:
        return True
    if target > collection[middle]:
        return binarySearch(collection[middle+1::], target)
    if target < collection[middle]:
        return binarySearch(collection[:middle:], target)
