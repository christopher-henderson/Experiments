#/usr/bin/env python
from __future__ import division

def mergeSort(collection):
    if len(collection) <= 1:
        return collection
    middle = len(collection) // 2
    left = mergeSort(collection[:middle:])
    right = mergeSort(collection[middle::])
    print (left,right)
    if len(left) is 0:
        return right
    elif len(right) is 0:
        return left
    THE REST

print (mergeSort([4,8,2,3,0,1]))
