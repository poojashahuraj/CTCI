# find a subarray in given array
ip_arr = [-2,-3, 4, -1, -2, 1, 5, -2]
max_sum = 7
import sys

def max_sum_contiguous_arr(ip_arr):
    # dont even think about sorting dumb, need to find contiguous array elements
    max_sum = -sys.maxint -1
    max_ending_here = -sys.maxint - 1

    for i in ip_arr:
        if i < 0:
            max_ending_here = max(max_ending_here, i)
            max_sum = max_ending_here
        elif i >= 0:
            max_ending_here = max(max_ending_here, i)
            max_sum = max(max_ending_here, max_sum)