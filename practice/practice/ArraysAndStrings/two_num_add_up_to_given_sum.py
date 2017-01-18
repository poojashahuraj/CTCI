"""
Given an array of integers write a program that will determine if any two numbers add up to a specified number N.
"""
from collections import defaultdict


def two_num_add_up(ip_arr, k):
    op = []
    for i in range(len(ip_arr)):
        s = None
        for j in range(i, len(ip_arr)):
            s = ip_arr[i]+ip_arr[j]
            if s == k:
                op.append([ip_arr[i],ip_arr[j]])
    return op
# run time complexicity is o(n^2) for this solution, can be improved by using hash table
print two_num_add_up([1,2,3,4], 5)


def two_num_add_hash(ip_arr, k):
    dict_a = defaultdict(int)
    for i in ip_arr:
        dict_a[i] += 1
    op = []
    for i in ip_arr:
        n = k - i
        if n in dict_a.keys():
            op.append([n,i])
    return op

print two_num_add_hash([1, 2, 3, 4], 5)
