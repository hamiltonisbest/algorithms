import random
import time

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

def foo():
#    a = [20, 10, 10, 1, 2, 2, 1, 1, 100, 10, 20, 19]
    a = [random.randint(0, 1000000) for i in xrange(1000000)]
    print "quick sort.............................................."
    t0 = time.time()
    quick_sort(a, 0, len(a) - 1)
    t1 = time.time()
    print t1 - t0, " seconds elapsed"

if __name__ == '__main__':
    foo()
