# Find if there is a subarray with 0 sum

# time complexity of this solution is o(n^2) because we are iterating through the each element in array n times exactly
def subarray_with_zero_sum(ip_arr):
    max_len = 0
    for index1, value1 in enumerate(ip_arr):
        curr_sum = 0
        for index2 in range(index1, len(ip_arr)):
            curr_sum += ip_arr[index2]
            if curr_sum == 0:
                max_len = max(max_len, index2 - index1 + 1)
    return max_len
print subarray_with_zero_sum([2, 1, -1])
print subarray_with_zero_sum([15, -2, 2, -8, 1, 7, 10, 13])


"""
A python program to find maximum length subarray with 0 sum in o(n) time
"""


def sub_array_with_zero_sum_using_hashmap(ip_arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0
    for i in range(len(ip_arr)):
        curr_sum += arr[i]
        # of course consider these two coroner cases defi very very IMP
        if arr[i] is 0 and max_len is 0:
            max_len = 1
        if curr_sum is 0:
            max_len = i + 1
        # if sum is already present in hash map then we found sequence with zero sum
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            # now put sum as key and index of i as value
            hash_map[curr_sum] = i

    return max_len


# test array
arr = [15, -2, 2, -8, 1, 7, 10, 13]

print "Length of the longest 0 sum subarray is %d" % sub_array_with_zero_sum_using_hashmap(arr)