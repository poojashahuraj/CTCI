"""
Count all possible paths from top left to bottom right of a mXn matrix. You can move only towards right or down.
Imagine a matrix 2x2. to reach at (2,2) there are only two unique ways.
one way (0,0)->(0,1)->(1,1)
second way: (0,0) -> (1,0) -> (1,1)

Solution:
break down the problem to dynamic programming way. to reach any step there are two ways: one comes from top and
other comes from left.
"""


def count_paths(rows_count, columns_count):
    op = [[0 for i in range(columns_count)] for j in range(rows_count)]
    # now set all elements in first row as 1, becasue there is only 1 way to get to any element in first row.
    for i in range(columns_count):
        op[0][i] = 1
    # now set all elements in first column as 1, because there is only 1 way to get to any cell in first column.
    for j in range(rows_count):
        op[j][0] = 1
    for i in range(1, rows_count):
        for j in range(1, columns_count):
            op[i][j] = op[i - 1][j] + op[i][j - 1]  # if in question diagonal move is allowed just add op[i-1][j-1]

    return op[rows_count - 1][columns_count - 1]


if __name__ == '__main__':
    print count_paths(1,1)
    print count_paths(3, 3)
    print count_paths(4,3)