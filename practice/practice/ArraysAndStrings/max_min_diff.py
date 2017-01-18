"""
find the value of max[a[i]-i a[j]-j]
"""
import sys


def find_max_min(ip_arr):
    op = [-1] * len(ip_arr)
    max_dif = -sys.maxint - 1
    min_diff = sys.maxint
    for index, value in enumerate(ip_arr):
        val = ip_arr[index] - index
        max_dif = max(max_dif, val)
        min_diff = min(min_diff, val)
        op[index] = val
    return max_dif - min_diff


# run time complexity of the problem is o(n)
print find_max_min([9, 15, 4, 12, 13])


# find the maximum sum of strictly incresing sub array
# positive , increasing, max sum continuous, duplicates
# [1,2,3,2,5,1,7] = 8

def find_max_sum(ip_sum):
    max_sum = -sys.maxint - 1
    index = 1
    while index < len(ip_sum):
        s = 0
        while ip_sum[index-1] < ip_sum[index]:
            # this means iterate through array till its increasing
            s = s + ip_sum[index]
            index += 1
        s += ip_sum[index]
        max_sum = max(s, max_sum)
        index += 1
    return max_sum

print find_max_sum([1, 2, 3, 2, 5, 1, 7])


