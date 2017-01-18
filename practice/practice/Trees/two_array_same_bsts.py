"""
given two array find out if they will ocnstruct same BSTs
"""


def check_bst(arr1, arr2):
    if arr2 == arr1:
        return True
    if arr1[0] != arr2[0]:
        return False
    arr1_right = get_right_subtree(arr1[0], arr1)
    arr2_right = get_right_subtree(arr2[0], arr2)
    arr1_left = get_left_subtree(arr1[0], arr1)
    arr2_left = get_left_subtree(arr2[0], arr2)
    if check_bst(arr1_right, arr2_right) is True and check_bst(arr1_left, arr2_left) is True:
        return True
    return False


def get_right_subtree(root, ip_arr):
    op = [i for i in ip_arr if i >root]
    return op


def get_left_subtree(root, ip_arr):
    op = [i for i in ip_arr if i < root]
    return op

print check_bst([3,5,4,6,1,0,2], [3,1,5,2,4,6,0])
print check_bst([3,5,4,6,1,0,2], [3,1,6,2,4,5,0])