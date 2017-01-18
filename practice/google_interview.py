"""
You are given a sorted list of distinct integers from 0 to 99, for instance [0, 1, 2, 50, 52, 75].
Your task is to produce a string that describes numbers missing from the list; in this case "3-49,51,53-74,76-99".
"""
import collections


class GetMissingRange(object):
    def __init__(self):
        pass

    def get_range(self, ip):
        op_lst = []
        for index, value in enumerate(ip):
            if index == len(ip)-1:
                op_lst.append(str(value+1)+"-"+str(99))
            if index < len(ip)-1:
                if ip[index] +1 == ip[index+1]:
                    pass
                elif ip[index+1] == value+2:
                    op_lst.append(str(value+1))
                else:
                    op_lst.append(str(value+1)+str('-')+str(ip[index+1]-1))

        return op_lst

g = GetMissingRange()
print g.get_range([0, 1, 2, 50, 52, 75])

"""
How to find a duplicate element in an array of shuffled consecutive integers.
ip: [1,2,3,4,5,6,7,2] op: 2
Approach: so addition of n consecutive numbers n*(n+1)/2
1+2+3+4 = 10 = 4*5/2=10

Say given array is not necessarily integers of consecutive numbers
e.g.a = [1,2,3,2,1,5,6,5,5,5]
TO REMOVE duplicates from array use list(set(a))
To print duplicates do something like below.
"""
def print_duplicates(ip_arr):
    result_arr = {}
    for item, count in collections.Counter(ip_arr).items():
        if count > 1:
            result_arr[item] = count
    return result_arr
    # print [item for item, count in collections.Counter(ip_arr).items() if count > 1]

print print_duplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 5])
