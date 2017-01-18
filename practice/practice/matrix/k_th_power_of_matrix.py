"""
Write a code to calculate kth power of matrix.
"""
def calculate_kth_power(ip_matrix, power):
    op = ip_matrix
    while power > 1:
        op = matrix_multiplication(op, ip_matrix)
        power -= 1
    return op


def matrix_multiplication(matrix_a, matrix_b):
    r1 = len(matrix_a)
    r2 = len(matrix_b)
    c1 = len(matrix_a[0])
    c2 = len(matrix_b[0])
    if c1 !=r2:
        print "Two matrixces are not compatible for multiplication."
        return -1
    op = [[0 for i in range(c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                op[i][j] += matrix_a[i][k]* matrix_b[j][k]
    return op


def mat_print(ip_mat):
    for i in range(len(ip_mat)):
        print ip_mat[i]

ip_mat = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]
op = calculate_kth_power(ip_mat,4)
mat_print(op)