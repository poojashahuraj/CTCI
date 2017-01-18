"""
How to find the smallest positive integer value that cannot be represented as sum of any subset of a given array?
Input: {1, 3, 6, 10, 11, 15};
Output: 2

ip:[1, 2, 3, 4, 7]
   [1, 3, 6, 10, 17]
5 = 4+1
6 = 4+2
7
8 = 4+3+1
9 = 4+3+2
10 = 4+3+2+1
11 is the smallest number which can not be presented by sub arrays.
challenging part is run time complexity should be o(n).


Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2

Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10

Input:  arr[] = {1, 2, 5, 10, 20, 40};
Output: 4

Input:  arr[] = {1, 2, 3, 4, 5, 6};
Output: 22      [2, 4, 7, 10,15,21]
"""


def find_smallest_positive(ip_arr):
    n = len(ip_arr)
    res = 1
    i = 0
    while i < n and res >= ip_arr[i]:
        print res
        res = res + ip_arr[i]
        i += 1
    print "==========="
    return res

ip = [[1, 3, 6, 10, 11, 15], [1, 1, 1, 1], [1, 1, 3, 4], [1, 2, 5, 10, 20, 40], [1, 2, 3, 4, 5, 6]]
print "Smallest positive int that can not be represented as sum of sub array:"
for i in ip:
    print "Array {}, val:{}".format(
        i, find_smallest_positive(i))
    print "----------------------"
print find_smallest_positive([1, 1, 3, 4])
