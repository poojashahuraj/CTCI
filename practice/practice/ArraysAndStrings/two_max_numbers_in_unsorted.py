"""
How to find top two numbers from an integer array
"""
import sys


def find_top_two(ip_arr):
    """
    simplest approach is modify bubble sort to get two max numbers which will take o(2n)
    think of solution with only one pass.
    """
    highest = -sys.maxint - 1
    second_highest = -sys.maxint - 1
    for i in ip_arr:
        if i >= highest:
            second_highest = highest
            highest = i
        elif i < highest:
            if i > second_highest:
                second_highest = i
    return highest, second_highest
# see run time complexity is o(n) only becasue we are iterating through array only once.

ip = [[1, 2, 3, 4], [-1, -2, 0, 1], [-4, 4, 0, -3, -2, 4], [0,0,-1]]
for i in ip:
    print "Max elements in array {}, are {}, {}".format(i, find_top_two(i), find_two_nums(i))