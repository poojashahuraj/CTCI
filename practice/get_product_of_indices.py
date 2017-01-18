"""
example, given:
[1, 7, 3, 4]
[28, 12, 04, 01]
[1, 1, 7, 21]
your function would return:
[84, 12, 28, 21]
by calculating:
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
"""


class GetProduct(object):
    def __init__(self, input_arr):
        self._input_arr = input_arr

    def run(self):
        l = len(self._input_arr)
        ret_arr = [None]*l
        for i in range(l):
            index = i
            remain_arr = self._input_arr[0:i:]+self._input_arr[i+1:l]
            prod = 1
            for j in range(l-1):
                prod = prod*remain_arr[j]
            ret_arr[index] = prod
        return ret_arr

g = GetProduct([1, 7, 3, 4])
print g.run()