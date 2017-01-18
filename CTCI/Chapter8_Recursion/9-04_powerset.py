"""
# 9.4. Write a method to return all subsets of a set.
"""
from unittest import TestCase
def subset_of_sets(ip_arr):
    result = [[]]
    for index, val in enumerate(ip_arr):
        result.extend([subset + [val] for subset in result])
    return result

print subset_of_sets([1,2,3])

