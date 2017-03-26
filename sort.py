import random
import time

#quick sort#########################################
def quick_sort(a, left, right):
    if left >= right:
        return a
    key = a[left]
    low = left
    high = right
    while left < right:
        while left < right and a[right] >= key:
            right -= 1
        a[left] = a[right]
        while left < right and a[left] <= key:
            left += 1
        a[right] = a[left]
    a[right] = key
    quick_sort(a, low, left - 1)
    quick_sort(a, left + 1, high)

#merge sort#########################################
def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) >> 1
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid + 1, right)

def merge(a, left, pivot, right):
    i, j = left, pivot
    while i < j and j <= right:
        if a[i] > a[j]:
            k, key = j, a[j]
            while k > i and a[k - 1] > key:
                a[k] = a[k - 1]
                k -= 1
            a[k] = key
            j += 1
        i += 1

def foo():
#    a = [20, 10, 10, 1, 2, 2, 1, 1, 100, 10, 20, 19]
    a = [random.randint(0, 1000000) for i in xrange(1000000)]
    print "quick sort.............................................."
    start = time.time()
    quick_sort(a, 0, len(a) - 1)
    end = time.time()
    print end - start, " seconds elapsed"
    print "merge sort.............................................."
    merge_sort(a, 0, len(a) - 1)
    start = time.time()
    merge_sort(a, 0, len(a) - 1)
    end = time.time()
    print end - start, " seconds elapsed"

if __name__ == '__main__':
    foo()
