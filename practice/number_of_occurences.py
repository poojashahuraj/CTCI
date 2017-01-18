"""
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[].
Expected time complexity is O(Logn)
"""


def occurrences(arr, num):
    first = 0
    last = 0
    for idx, val in enumerate(arr):
        if val == num:
            first = idx
            break
    for idx, val in reversed(list(enumerate(arr))):
        if val == num:
            last = idx
            break
    occurrence = last-first+1
    print "Number {} appeared {} times in {}.".format(num, occurrence, arr)
    return occurrence

ip = [1, 1, 2, 2, 2, 2, 2, 3, 4]
occurrences(ip, 2)

