"""
Write a program to find intersection of two sorted array in python?
"""


def merge_two_sorted_arr(arr1, arr2):
    new_arr = []
    head1 = 0
    head2 = 0
    while head1 < len(arr1) and head2 < len(arr2):
        if arr1[head1] < arr2[head2]:
            new_arr.append(arr1[head1])
            head1 += 1
        elif arr1[head1] > arr2[head2]:
            new_arr.append(arr2[head2])
            head2 += 1
        else:
            new_arr.append(arr1[head1])
            new_arr.append(arr2[head2])
            head1 += 1
            head2 += 1

    if head2 < len(arr2):
        for i in range(head2, len(arr2)):
            new_arr.append(arr2[i])
    elif head1 < len(arr1):
        for i in range(head1, len(arr1)):
            new_arr.append(arr1[i])
    return new_arr


# For run time complexicity say m is length of first array and n is len of second array.
# then first while loop ran for min(m, n) and next for loop ran for max(m,n), so run time complexity is o(m+n).

print merge_two_sorted_arr([1, 3, 5, 7, 9], [2, 2, 2, 4, 6, 8, 10, 12, 14])
