"""
Replace every element with the least greater element on its right
Given an array of integers, replace every element with the least greater element on its right side in the array.
If there are no greater element on right side, replace it with -1.
Input: [8, 58, 71, 18, 31, 32, 63, 92,
         43, 3, 91, 93, 25, 80, 28]
Output: [18, 63, 80, 25, 32, 43, 80, 93,
         80, 25, 93, -1, 28, -1, -1]
"""

def replace_elements(ip_arr):
    result = [None]*len(ip_arr)
    for index_1, value_1 in enumerate(ip_arr):
        new_arr = [v for i,v in enumerate(ip_arr[index_1+1:]) if v > value_1]
        if new_arr:
            result[index_1] = min(new_arr)
        else:
            result[index_1] = -1
    return result

print replace_elements([8, 58, 71, 18, 31, 32, 63, 92,
         43, 3, 91, 93, 25, 80, 28])