# write a algorithm if either one element in a row or column is zero then full row is zero


class Matrix(object):
    def __init__(self):
        pass

    def delete_rows(self, arr):
        rows_len = len(arr)
        columns_len = len(arr[0])
        rows_with_zeros = []
        columes_with_zeros = []
        for i in range(rows_len):
            for j in range(columns_len):
                if arr[i][j] == 0:
                    rows_with_zeros.append(i)
                    columes_with_zeros.append(j)

        for i in rows_with_zeros:
            for j in range(columns_len):
                arr[i][j] = 0
        for k in columes_with_zeros:
            for l in range(rows_len):
                arr[l][k] = 0
        return arr
s = Matrix()
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 0],
       [2, 4, 6, 8, 0],
       [1, 0, 5, 7, 9],
       [1, 3, 6, 7, 8]]
result = s.delete_rows(arr)
for i in range(len(result)):
    print result[i]
