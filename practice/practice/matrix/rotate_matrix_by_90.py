"""
Write a program to rotate a matrix by 90 degrees.
only square martix can be rotated in same place, for another kinda matrix u need different matrix to store at new place.
"""
from collections import defaultdict


def rotate_matrix_anti_clockwise(ip_mat):
    l = len(ip_mat)
    # m is counter for outer layer
    # n is counter for elements in that layer. range (m, l-1-m). that is start from m to l-1(becasue indices start from 0)
    # l-1-m because from right side also u should remove m columns
    for m in range(l/2):
        for n in range(m, l-m-1):
            x = ip_mat[m][n]
            # u chose to keep column constant here so its anticlockwise
            ip_mat[m][n] = ip_mat[n][l-m-1]
            ip_mat[n][l-m-1] = ip_mat[l-m-1][l-n-1]
            ip_mat[l-m-1][l-n-1] = ip_mat[l-n-1][m]
            ip_mat[l-n-1][m] = x
    return ip_mat


def rotate_matrix_clockwise(ip_mat):
    l = len(ip_mat)
    for m in range(l/2):
        for n in range(m, l-m-1):
            x = ip_mat[m][n]
            # u chose to keep column constant here so its anticlockwise
            ip_mat[m][n] = ip_mat[l-m-1][n]
            ip_mat[l-m-1][n] = ip_mat[l-m-1][l-n-1]
            ip_mat[l-m-1][l-n-1] = ip_mat[m][l-n-1]
            ip_mat[m][l-n-1] = x
    return ip_mat


def print_mat(ip_mat):
    for i in range(len(ip_mat)):
        print ip_mat[i]


if __name__ == '__main__':
    ip_mat = [[0, 1, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print_mat(ip_mat)
    print "--------------------------------"
    op = rotate_matrix_anti_clockwise(ip_mat)
    op = rotate_matrix_clockwise(ip_mat)
    print_mat(op)


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        smaller_than_pivot = [i for i in l[1:] if i <= pivot]
        larger_than_pivot = [i for i in l[1:] if i > pivot]
        op = quick_sort(smaller_than_pivot) + [pivot] + quick_sort(larger_than_pivot)
        return op

print quick_sort([3, 2, 1, 5, 4, 6, 8])
