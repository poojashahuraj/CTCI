def zero_matrix(ip_arr):
    rows = len(ip_arr)
    columns = len(ip_arr[0])
    rows_with_zero = []
    columns_with_zero = []
    for i in range(rows):
        for j in range(columns):
            if ip_arr[i][j] == 0:
                rows_with_zero.append(i)
                columns_with_zero.append(j)
    for i in range(rows):
        for j in range(columns):
            if i in rows_with_zero or j in columns_with_zero:
                ip_arr[i][j] = 0
    return ip_arr


def print_mat(ip_arr):
    rows = len(ip_arr)
    for i in range(rows):
        print ip_arr[i]


ip_arr = [[1, 2, 3, 0],
          [2, 3, 0, 1],
          [1, 5, 1, 4],
          [2, 9, 1, 3]]
print_mat(ip_arr)
print "---------------------"
print_mat(zero_matrix(ip_arr))

ip_arr = [[1, 2, 3, 3],
          [2, 3, 0, 1],
          [1, 5, 1, 4],
          [2, 9, 1, 3]]
print_mat(ip_arr)
print "---------------------"
print_mat(zero_matrix(ip_arr))