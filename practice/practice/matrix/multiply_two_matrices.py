def multiply_two_matrices(mat_1, mat_2):
    rows_1 = len(mat_1)
    rows_2 = len(mat_2)
    columns_1 = len(mat_1[0])
    columns_2 = len(mat_2[0])
    if columns_1 != rows_2:
        return -1
    op = [[0 for i in range(columns_2)] for j in range(rows_1)]
    for i in range(rows_1):
        for j in range(columns_2):
            for k in range(rows_2):
                op[i][j] += mat_1[i][k]*mat_2[k][j]
    return op

mat_1 = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
mat_2 = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]

print multiply_two_matrices(mat_1, mat_2)

