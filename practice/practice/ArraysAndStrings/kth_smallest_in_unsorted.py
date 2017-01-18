"""
Find kth smallest element in unsorted array.

"""


def kth_smallest_unsorted(ip_arr, k):
    # use modified bubble sort, for each iteration one smallest element will be bubbled up at top.
    # run time complexity will be o(nk), worst case when k == len(ip_arr), time complexicty becomes o(n^2) same as
    # bubble sort.
    # bubble sort and quick sort gives worst run time complexity as o(n^2), of course we can do better in sorting, use
    # merge sort, heap sort with run time complexity as o(nlogn)
    c = 0
    while c < k:
        for i, val in enumerate(ip_arr):
            for j in range(i+1, len(ip_arr)):
                if ip_arr[j] < ip_arr[i]:
                    temp = ip_arr[i]
                    ip_arr[i] = ip_arr[j]
                    ip_arr[j] = temp
                c += 1
    return ip_arr[k-1]

print kth_smallest_unsorted([9,6,5,3,2,1,0], 1)
print kth_smallest_unsorted([9,6,5,3,2,1,0], 2)
print kth_smallest_unsorted([9,6,5,3,2,1,0], 3)
