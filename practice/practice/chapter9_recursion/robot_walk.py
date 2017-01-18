"""
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions:
right and down. How many possible paths are there for the robot?

Lets solve this using dynamic programming, break down the problem and then solve it.
There are only two ways to reach one cell, say one from top and another from left
"""

def robot_walk(rows, columns):
    op = [[0 for i in range(columns)] for j in range(rows)]
    for j in range(columns):
        op[0][j] = 1
    for i in range(rows):
        op[i][0] = 1
    for i in range(1, rows):
        for j in range(1, columns):
            op[i][j] = op[i-1][j]+op[i][j-1]
    return op[rows-1][columns-1]

print robot_walk(3,3)
# robot walk with dynamic programming will take only o(rows*columns) runtime. As we hit each cell only once


def permutation_of_strin(ip_str):
    if len(ip_str) == 1:
        return [ip_str]
    op = []
    for index, value in enumerate(ip_str):
        op.extend(value+i for i in permutation_of_strin(ip_str[0:index]+ip_str[index+1:]))
    return op

print permutation_of_strin("AAB")