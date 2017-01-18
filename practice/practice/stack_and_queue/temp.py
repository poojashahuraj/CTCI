"""
In an array that has one value for more than half of its elements, how can you find that value?
e.g. ip = [3, 3, 4, 2, 4, 4, 2, 4, 4]
length is 9 and 4 appeared 5 times.
so answer is 4

"""
from collections import defaultdict

ip = [3, 3, 4, 2, 4, 4, 2, 4, 4]


def example(ip_arr):
    dict_a = defaultdict(int)
    for i in ip_arr:
        dict_a[i] += 1
    half = len(ip_arr)//2
    for i in dict_a.keys():
        if dict_a[i] > half:
            return i
print example(ip)

###
# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n\n'
# 'steps. Conversely, if it\'s negative, move backward n steps. Determine if there is a loop in this array.\n'
# 'For example, given the array [2, -1, 1, 2, 2], index 0 maps to index 2, 1 maps to 0, 2 maps to 3, and so on.\n'
# 'There is a loop in this array because 0 maps to 2, 2 maps to 3, and 3 maps to 0 (use the modulo operator).\n')


# Given an array of integers (positive or negative) find the lowest positive integer NOT present in that array.
# e.g. [8, 9, 17,-6, -4, 3, 2, 1] answer will be 5.
# 5 is the lowest positive integer which is not present in array
def find_an_lowest_positive(ip_arr):
    op = [0]*(len(ip_arr)+1)
    n = len(ip_arr)
    for val in ip_arr:
        if not val < 1 and not val > n:
            op[val] = 1
    # in op ignore the 0th index of course, becasue we store occurence of 1 to n with index
    # return the first index of 0, after removing first element
    op.pop(0)
    return op.index(0)+1

print find_an_lowest_positive([8, 9, 17, -6, -4, 3, 2, 1])
print find_an_lowest_positive([8, 9, 17, -6, 4, 3, 2, 1])