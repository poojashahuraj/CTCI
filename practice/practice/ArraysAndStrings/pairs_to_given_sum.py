"""
How to find all pairs on integer array whose sum is equal to given number
"""
from collections import defaultdict

op = []


def find_all_pairs_of_integers_with_sum(ip_arr, given_sum):
    sorted_arr = list(sorted(ip_arr))
    dict_a = defaultdict(int)
    for i in sorted_arr:
        dict_a[i] += 1
    set_arr = sorted(list(set(sorted_arr)))
    first_index = 0
    last_index = len(set_arr)-1
    while first_index < last_index:
        temp_sum = set_arr[first_index] + set_arr[last_index]
        if temp_sum == given_sum:
            min_occur = min(dict_a[set_arr[first_index]], dict_a[set_arr[last_index]])
            for j in range(min_occur):
                op.append((set_arr[first_index], set_arr[last_index]))
            first_index += 1
            last_index -= 1
        elif temp_sum > given_sum:
            last_index -= 1
        elif temp_sum < given_sum:
            first_index += 1
    return op
print find_all_pairs_of_integers_with_sum([2, 4, 3, 2, 5, 5, 6, -2, 4, 7, 8, 9], 7)

"""
To put it simple, ADT is a logical description and data structure is concrete.
ADT is the logical picture of the data and the operations to manipulate the component elements of the data.
Data structure is the actual representation of the data during the implementation and the algorithms to manipulate
the data elements. ADT is in the logical level and data structure is in the implementation level.
"""