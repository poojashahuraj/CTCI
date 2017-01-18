# find the first repeating element in given array
# ip_arr = [10, 5, 3, 4, 3, 5, 6] answer is 5
from collections import defaultdict


def first_repeating_ele_hashmap(ip_arr):
    dict_a = defaultdict(list)
    # for each element lets store, index of the element which occurred at first and count
    for index, value in enumerate(ip_arr):
        try:
            dict_a[value][0]
        except IndexError as e:
            dict_a[value] = [index, 0]
        # increase the count every time u see element
        dict_a[value][1] +=1
    # this is the list of lists each of length two, 0th element is index of first occurrences and 1st element is count
    # of how many times it occurred.
    # we sorted with index of occurence.
    op = sorted(dict_a.values())
    for i in op:
        if i[1] > 1:
            return ip_arr[i[0]]

ip = [[10, 5, 3, 4, 3, 5, 6], [10, 5, 3, 4, 3, 4, 6]]
for i in ip:
    print "First repeating char in {} arr is {}.".format(i, first_repeating_ele_hashmap(i))