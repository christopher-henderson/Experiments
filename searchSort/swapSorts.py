from random import randrange


def sort(collection, key=lambda item: item):
    size = len(collection)
    if size < 20:
        return insertion_sort(collection, key)
    else:
        return quick_sort(collection, 0, size - 1, key)


def insertion_sort(collection, key):
    for i in range(len(collection)):
        j = i
        while j > 0 and key(collection[j - 1]) > key(collection[j]):
            temp = collection[j]
            collection[j] = collection[j - 1]
            collection[j - 1] = temp
            j -= 1


def quick_sort(collection, low, high, key):
    if low < high:
        p = partition(collection, low, high, key)
        quick_sort(collection, low, p, key)
        quick_sort(collection, p + 1, high, key)


def partition(collection, low, high, key):
    pivot = key(collection[low])
    low -= 1
    high += 1
    while True:
        low += 1
        while key(collection[low]) < pivot:
            low += 1
        high -= 1
        while key(collection[high]) > pivot:
            high -= 1
        if low < high:
            temp = collection[low]
            collection[low] = collection[high]
            collection[high] = temp
        else:
            return high


def main():
    collection = [randrange(20) for _ in range(30)]
    print (collection)
    sort(collection)
    print (collection)


main()
