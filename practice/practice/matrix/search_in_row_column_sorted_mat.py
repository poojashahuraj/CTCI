# search element is row wise and column wise sorted matrix


def search_in_mat(ip_arr, value):
    first_row = 0
    last_column = len(ip_arr[0]) - 1
    while first_row < len(ip_arr) and last_column >= 0:
        mat_val = ip_arr[first_row][last_column]
        if mat_val == value:
            return first_row, last_column
        elif value > mat_val:
            first_row += 1
        else:
            last_column -= 1
    return -1, -1


ip_arr = [[10, 20, 30, 40],
          [12, 22, 32, 42],
          [14, 24, 34, 44],
          [16, 26, 36, 46]]
print search_in_mat(ip_arr, 34)
print search_in_mat(ip_arr, 33)
