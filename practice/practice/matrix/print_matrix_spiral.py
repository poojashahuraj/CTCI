"""
direction
0 = horizontal left to right
1 = Vertical top to bottom
2 = horizontal right to left
4 = vertical bottom to top
"""


def print_spiral(ip_mat):
    direction = 0
    top = 0
    bottom = len(ip_mat)-1
    left = 0
    right = len(ip_mat[0])-1
    result = []
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right+1):
                result.append(ip_mat[top][i])
            top += 1
            direction = 1
        elif direction == 1:
            for j in range(top, bottom+1):
                result.append(ip_mat[j][right])
            right -= 1
            direction = 2
        elif direction == 2:
            for k in range(right, left-1, -1):
                result.append(ip_mat[bottom][k])
            bottom -= 1
            direction = 3
        elif direction == 3:
            for l in range(bottom, top-1, -1):
                result.append(ip_mat[l][left])
            left += 1
            direction = 0
    return result


ip = [[01, 02, 03, 04, 05],
      [11, 12, 13, 14, 15],
      [21, 22, 23, 24, 25],
      [31, 32, 33, 34, 35],
      [41, 42, 43, 44, 55]]
print print_spiral(ip)
