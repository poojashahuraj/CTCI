"""
Given two integer arrays , give the sequence to crete new array
"""


def push_pop_seq(arr_1, arr_2):
    """

    :param arr_1:
    :param arr_2:
    :return:
    """
    aux = []
    str_op = ""
    for index, value in enumerate(arr_1):
        if arr_1[index] == arr_2[index]:
            aux.append(value)
            str_op += "push{}|".format(value)
            aux.pop()
            str_op += "pop{}|".format(value)
        else:
            aux.append(value)
            str_op += "push{}|".format(value)
    for i in range(len(aux)):
        p = aux.pop()
        str_op += "pop{}|".format(p)
    return str_op


print push_pop_seq([1, 2, 3, 4], [1, 2, 3, 4])
print push_pop_seq([1, 2, 3, 4], [4, 3, 2, 1])
