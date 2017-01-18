# find the smallest element in sorted rotated array


def min_in_sorted_rotated_arr(ip_arr):
    start_idx = 0
    end_idx = len(ip_arr)-1
    while start_idx < end_idx:
        mid_index = start_idx + (end_idx-start_idx) / 2
        if ip_arr[start_idx] < ip_arr[mid_index] < ip_arr[end_idx]:
            print "array is not rotated at all."
            return
        elif ip_arr[mid_index] < ip_arr[end_idx]:
            # this means second half is good and is not rotated,
            # so move end to mid meaning search is first half only.
            end_idx = mid_index
        elif ip_arr[start_idx] < ip_arr[mid_index]:
            start_idx = mid_index+1
        else:
            start_idx += 1
    return ip_arr[start_idx]

print min_in_sorted_rotated_arr([7, 8, 9, 1, 2, 3, 4, 5, 6])
print min_in_sorted_rotated_arr([9, 0, 1])
print min_in_sorted_rotated_arr([9, 3])
# we are searching elements using binary search so run time complexity is log(n)
