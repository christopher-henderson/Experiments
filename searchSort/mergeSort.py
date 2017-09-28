#/usr/bin/env python
from __future__ import division

def mergeSort(collection):
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    left = mergeSort(collection[:mid:])
    right = mergeSort(collection[mid::])
    return merge(left, right)

def merge(a, b):
    if len(a) is 0:
        return b
    if len(b) is 0:
        return a
    i = 0
    j = 0
    result = list()
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    elif j < len(b):
        result.extend(b[j:])
    return result

print (mergeSort([4,8,2,3,0,1]))
