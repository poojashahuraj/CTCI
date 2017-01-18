#!/usr/bin/env python3


def generate_spiral_matrix(rows, columns):
    mat = [[0 for i in range(columns)] for j in range(rows)]
    value = 0
    end = rows * columns
    top = 0
    bottom = rows-1
    left = 0
    right = columns-1
    direction = 0
    while top <= bottom and left <= right and end >= value:
        if direction == 0:
            for i in range(left, right+1):
                mat[top][i] = value
                value += 1
            direction = 1
            top += 1
        elif direction == 1:
            for j in range(top, bottom+1):
                mat[j][right] = value
                value += 1
            right -= 1
            direction = 2
        elif direction == 2:
            for k in range(right, left-1, -1):
                mat[bottom][k] = value
                value += 1
            direction = 3
            bottom -= 1
        elif direction == 3:
            for l in range(bottom, top-1, -1):
                mat[l][left] = value
                value += 1
            direction = 0
            left += 1
    return mat


if __name__ == '__main__':
    x = generate_spiral_matrix(3,3)
    for i in range(len(x)):
        print x[i]
    print "======================================"
    y = generate_spiral_matrix(4, 4)
    for i in range(len(y)):
        print y[i]
