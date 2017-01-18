"""
Find the middle value of the array a.
If a[0] < a[mid], then all values in the first half of the array are sorted.
If a[mid] < a[last], then all values in the second half of the array are sorted.
Take the sorted half, and check whether your value lies within it (compare to the maximum idx in that half).
If so, just binary search that half.
If it doesn't, it must be in the unsorted half.
Take that half and repeat this process, determining which half of that half is sorted, etc.
e.g. [4,5,6,7,0,1,2]
search for 0
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev = list(set(sorted(nums)))
        print rev
        if len(rev) < 3:
            return rev[0]
        else:
            return rev[len(rev)-2]
s = Solution()
print s.thirdMax([2,2,3,1])
print s.thirdMax([3,2,1])
print s.thirdMax([1,2])