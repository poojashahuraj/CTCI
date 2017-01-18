"""
how to find common element in three sorted arrays.
"""
from collections import defaultdict


def find_ele_three_sorted(ip_arr1, ip_arr2, ip_arr3):
    op = []
    for i in ip_arr1:
        if is_element_present_in_arr(ip_arr2, i) is True and \
                        is_element_present_in_arr(ip_arr3, i) is True:
            op.append(i)
    return op


# this method has run time complexity equal to o(logn) because we are doing binary search, n is length of input array.
def is_element_present_in_arr(ip_arr, element):
    """
    This method return true if given element is present in given sorted array or not.
    do binary search of course as array is sorted.
    """
    start_index = 0
    end_index = len(ip_arr) - 1
    if element > ip_arr[end_index] or element < ip_arr[0]:
        return False
    while start_index < end_index:
        mid_index = start_index + (end_index - start_index) / 2
        if ip_arr[mid_index] < element:
            start_index = mid_index + 1
        elif ip_arr[mid_index] > element:
            end_index = mid_index
        else:
            # ip_arr[mid_index] == element:
            return True

    return False


# l1 is first list we iterate through each element and then l2 and l3 are remianing two lists where we do binary
# search of element for every elemet in l1
# o(l1)*(o(log l2) + o(log l3)) = l1 (log l2*l3), can we do better? of course.
print find_ele_three_sorted([1, 2, 3, 4],
                            [2, 3, 4, 5, 6],
                            [2, 3, 11, 12, 13])

print find_ele_three_sorted([1, 5, 10, 20, 40, 80],
                            [6, 7, 20, 80, 100],
                            [3, 4, 15, 20, 30, 70, 80, 120])


# we should iterate through each element only once and note this is sorted array.
# run time complexity of this algorithm is o(l1+l2+l3) which is better than previous

def common_ele_three_sorted(arr1, arr2, arr3):
    l1, l2, l3 = 0, 0, 0
    while l1 < len(arr1) and l2 < len(arr2) and l3 < len(arr3):
        if arr1[l1] == arr2[l2] == arr3[l3]:
            print arr1[l1],
            l1 += 1
            l2 += 1
            l3 += 1
        elif arr1[l1] < arr2[l2]:
            # we increment l1 till its greater than l2
            l1 += 1
        elif arr2[l2] < arr3[l3]:
            # we increment l2 till its greter than l3
            l2 += 1
        else:
            # at this point l3 is the smallest so increment l3
            l3 += 1


common_ele_three_sorted([1, 5, 10, 20, 40, 80],
                        [6, 7, 20, 80, 100],
                        [3, 4, 15, 20, 30, 70, 80, 120])
