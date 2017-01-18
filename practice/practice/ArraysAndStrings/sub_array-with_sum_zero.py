"""
How to find if there is a sub array with sum equal to zero
There is whole set of array related questions which are based upon sub-array or only selective elements of array e.g.
from some range, this is one of such problem. Here you are given an array of positive and negative numbers,
find if there is a sub-array with 0 sum.
4,0
6,1
3,2

Examples:
Input: {4, 2, -3, 1, 6}
Output: true
There is a sub-array with zero sum from index 1 to 3.
"""
import sys
from collections import defaultdict

# use hashmap again
# this is best solution you will have as u are iterating through the array onle once, hence run time complexity is o(n)

def sub_array_with_zero_sum(ip_arr):
    dict_a = defaultdict(int)
    cur_sum = 0
    for i in ip_arr:
        cur_sum +=i
        if cur_sum == 0:
            return True
        if cur_sum in dict_a.keys():
            return True
        else:
            dict_a[cur_sum] = i
    return False

print sub_array_with_zero_sum([4, 2, -3, 1, 6])
print sub_array_with_zero_sum([4,3,2])
