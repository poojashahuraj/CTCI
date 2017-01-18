class RotateMatrix(object):
    def __init__(self):
        pass

    def rotate_matrix(self, mat_ip):
        "TODO: rotation of matrix in place we need to have NxN matrix."
        l = len(mat_ip)
        for m in range(l/2):
            for n in range(m, l-m-1):
                x = mat_ip[m][n]
                mat_ip[m][n] = mat_ip[n][l-m-1]
                mat_ip[n][l-m-1] = mat_ip[l-m-1][l-n-1]
                mat_ip[l-m-1][l-n-1] = mat_ip[l-n-1][m]
                mat_ip[l-n-1][m] = x
        return mat_ip

    def print_matrix(self, ip_mat):
        for i in range(len(ip_mat)):
            print ip_mat[i]

    def search_in_matrix(self, ip_arr, element):
        rows = len(ip_arr)
        columns = len(ip_arr[0])
        r = 0
        c = columns-1
        while r < rows-1 and c > 0:
            if ip_arr[r][c] == element:
                print "OK: {} is at [{}][{}]".format(element, r, c)
                return r,c
            if element > ip_arr[r][c]:
                r += 1
            else:
                c -= 1
        print "{} element not found.".format(element)
        return -1, -1


rm = RotateMatrix()
ip_arr = [[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
          [12, 13, 14, 15]]
rm.print_matrix(ip_arr)
rotates_mat = rm.rotate_matrix(ip_arr)
print "---------------------------"
rm.print_matrix(rotates_mat)
ip_mat = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]]
r = RotateMatrix()
r.print_matrix(ip_mat)
r.search_in_matrix(ip_mat, 25)
r.search_in_matrix(ip_mat,11)