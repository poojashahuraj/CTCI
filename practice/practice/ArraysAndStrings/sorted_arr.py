"""
Given a sorted array and a number x, find the pair in array whose sum is closest to x
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
"""
import sys


def sorted_arr(ip_arr, given_sum):
    left = 0
    right = len(ip_arr)-1
    r1 = ip_arr[left]
    r2 = ip_arr[right]
    min_diff_so_far = sys.maxint

    while left < right:
        addition = ip_arr[left] + ip_arr[right]
        min_diff = abs(given_sum - addition)
        if abs(min_diff) < min_diff_so_far:
            min_diff_so_far = min_diff
            r1 = ip_arr[left]
            r2 = ip_arr[right]

        if min_diff == 0:
            return r1, r2

        if addition > given_sum:
            right -= 1
        else:
            left += 1
    return r1, r2

print sorted_arr([10,22,28,29,30,40], 54)