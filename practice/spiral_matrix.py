class SpiralMatrix(object):
    def __init__(self):
        pass

    def run(self, input_arr, rows, columns):
        rt_list = []
        if rows <= columns:
            iterations = rows
        else:
            iterations = columns
        for i in range(iterations):
            i += 1
        # print first row
        for i in range(columns):
            
        # print last column top down
        # print last row right to left
        # print first column bottom to up


sm = SpiralMatrix()
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print a[0][1]
