# coding=utf-8
"""
Your company built an in-house calendar tool called HiCal.
You want to add a feature to see the times in a day when everyone is available.
e.g. input [(3,6),(2,4),(2,5)]
output should be [(2,6)]
So 2 to 6 time everyone is not FREE.
IP: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
op: [(0, 1), (3, 8), (9, 12)]

"""

def calender_free(ip_arr):
    sorted_ip = sorted(ip_arr)
    result_op = [sorted_ip[0]]
    for current in sorted_ip:
        start_time = current[0]
        end_time = current[1]
        previous_start_time = result_op[-1][0]
        previous_end_time =result_op[-1][1]
        if start_time == previous_start_time:
            result_op[-1] = (start_time, max(end_time, previous_end_time))
        elif previous_end_time >= start_time:
            result_op[-1] = (previous_start_time, max(end_time, previous_end_time))
        else:
            result_op.append((start_time, end_time))
    return result_op

print calender_free([(3,6),(2,4),(2,5)])
print calender_free([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

"""
A circus is designing a tower routine consisting of people standing atop one another’s shoulders.
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of peo- ple in such a tower.
EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
"""

def circus_ht_wt(ip_arr):
    sorted_ip_arr = sorted(ip_arr)
    result_arr = [sorted_ip_arr[0]]
    for current in sorted_ip_arr:
        height = current[0]
        weight = current[1]
        previous_ht = result_arr[-1][0]
        previous_wt = result_arr[-1][1]
        if height > previous_ht and weight > previous_wt:
            result_arr.append(current)
    return result_arr
print circus_ht_wt([(65, 100),(70, 150), (56, 90), (75, 190), (60, 95),(68, 110)])
