# how to reverse a given array in place? of course u can suse one two extra temp variables but not in built funcitons.


def reverse_arr(ip_arr):
    start_idx = 0
    end_idx = len(ip_arr)-1
    while start_idx < end_idx:
        temp = ip_arr[start_idx]
        ip_arr[start_idx] = ip_arr[end_idx]
        ip_arr[end_idx] = temp
        start_idx += 1
        end_idx -= 1
    return ip_arr
print reverse_arr([1, 2, 3, 4, 5, 6])
print reverse_arr([1, 2, 3, 4, 5])
