# 9.2. Imagine a robot sitting on the upper left corner of an X by Y grid. The
# robot can only move in two directions: right and down. How many possible
# paths are there for the robot to go from (0, 0) to (X, Y)?
#
# FOLLOW UP
#
# Imagine certain spots are "off limits", such that the robot cannot step on
# them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.

def robot(rows, columns):
    op = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        op[i][0] = 1
    for j in range(columns):
        op[0][j] = 1

    for m in range(1, rows):
        for n in range(1, columns):
            op[m][n] = op[m][n-1]+op[m-1][n]
    for i in op:
        print i
    return op[rows-1][columns-1]

print "Robot can reach to right most coroner in {} ways.".format(robot(2,2))
print "Robot can reach to right most coroner in {} ways.".format(robot(3,3))