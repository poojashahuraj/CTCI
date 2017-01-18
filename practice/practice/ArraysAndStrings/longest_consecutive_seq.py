# Write a program to find length of longest consecutive sequence in array of integers?
from collections import defaultdict


def longest_consecutive_seq(ip_arr):
    dict_a = defaultdict(int)
    for i in ip_arr:
        dict_a[i] += 1
    maxlen = 1
    for n in ip_arr:
        tmp = n + 1
        l = 1
        while dict_a.has_key(tmp):
            l += 1
            del dict_a[tmp]
            tmp += 1
        tmp = n - 1
        while dict_a.has_key(tmp):
            l += 1
            del dict_a[tmp]
            tmp -= 1
        maxlen = max(l, maxlen)
    return maxlen


print longest_consecutive_seq([100, 4, 200, 5, 1, 3, 2, 6])
# see only one for loop at line 10, so run time complexicity is o(n)
