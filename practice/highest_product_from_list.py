# coding=utf-8
"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
Does your function work with negative numbers? If list_of_ints is  [−10,−10,1,3,2] we should return
300 (which we get by taking (−10∗−10∗3).

Solution:
Easy way will be have three loops. with o(n^3) run time complexity.
"""


class HighestProduct(object):
    def __init__(self):
        pass

    def multiply_arr(self, ip_arr):
        # answer is here: https://www.interviewcake.com/question/python/highest-product-of-3
        max_prod_so_far = 1
        min_prod_so_far = 1
        max_prod = 1
        for i in ip_arr:
            if i > 0:
            # positive number
                max_prod_so_far = max_prod_so_far*i
                min_prod_so_far = min(min_prod_so_far*i, 1)
            elif i == 0:
                max_prod_so_far =1
                min_prod_so_far=1
            else:
                temp = max_prod_so_far
                max_prod_so_far = max(min_prod_so_far*i, 1)
                min_prod_so_far = temp*i
            if max_prod_so_far > max_prod:
                max_prod = max_prod_so_far
        return max_prod

m = HighestProduct()
print m.multiply_arr([-10, -10, -1, 3, -2])
