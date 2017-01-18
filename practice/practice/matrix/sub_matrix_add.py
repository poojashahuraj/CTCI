"""
A 2D matrix is given to you. Now user will give 2 positions (x1,y1) and (x2,y2),
which is basically the upper left and lower right coordinate of a rectangle formed within the matrix.
You have to print sum of all the elements within the area of rectangle in O(1) running time.
Now you can do any pre computation with the matrix.
But when it is done you should answer all your queries in constant time.

Example : consider this 2D matrix
1 3 5 1 8
8 3 5 3 7
6 3 9 6 0

Now consider 2 points given by user (0, 2) and (2, 4).
Your solution should print: 44.
i.e., the enclosed area is
5 1 8
5 3 7
9 6 0
"""


def sub_arr_add(ip_arr, x1, y1, x2, y2):
    sum = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += ip_arr[i][j]
    return sum


ip_arr = [[1, 3, 5, 1, 8],
          [8, 3, 5, 3, 7],
          [6, 3, 9, 6, 0]]
print sub_arr_add(ip_arr, 0, 2, 2, 4)
