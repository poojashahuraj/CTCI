"""
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is
followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal.
If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array. This is also a difficult array problem to solve and you need lot of practice to solve this kind of problems in real interviews, especially when you see it first time.

How to rearrange array in alternating positive and negative number?
Input: {1, 2, 3, -4, -1, 4}
Output: {-4, 1, -1, 2, 3, 4}

Input: {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
"""


def alternating_positive_negative(ip_arr):
    pos =[]
    neg = []
    for i in ip_arr:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    # we iterated through each element in array only once and added them in different queue, till here run time
    # complexicity is o(n)
    l1 = len(pos)
    l2 = len(neg)
    i,j = 0,0
    op = []
    while i < l1 and j < l2:
        op.append(neg.pop(0))
        op.append(pos.pop(0))
        i +=1
        j +=1
    if i < l1:
        op.extend(pos)
    elif j < l2:
        op.extend(neg)
    return op
assert alternating_positive_negative([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]) == \
       [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
assert alternating_positive_negative([1, 2, 3, -4, -1, 4]) == [-4, 1, -1, 2, 3, 4]