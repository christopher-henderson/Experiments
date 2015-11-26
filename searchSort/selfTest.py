from random import randrange, shuffle


def quick_sort(collection, low, high):
    if low < high:
        p = partition(collection, low, high)
        quick_sort(collection, low, p)
        quick_sort(collection, p + 1, high)


def partition(collection, low, high):
    pivot = collection[(low + high) // 2]
    low -= 1
    high += 1
    while True:
        high -= 1
        while collection[high] > pivot:
            high -= 1
        low += 1
        while collection[low] < pivot:
            low += 1
        if low < high:
            temp = collection[low]
            collection[low] = collection[high]
            collection[high] = temp
        else:
            return high


def bubble_sort(collection):
    for _ in range(len(collection)):
        for index in range(len(collection) - 1):
            if collection[index] > collection[index + 1]:
                temp = collection[index]
                collection[index] = collection[index + 1]
                collection[index + 1] = temp


def main():
    test = [randrange(100) for _ in range(100)]
    fixture = sorted(test)

    quick_sort(test, 0, len(test) - 1)
    assert test == fixture
    shuffle(test)

    bubble_sort(test)
    assert test == fixture
    shuffle(test)


main()
