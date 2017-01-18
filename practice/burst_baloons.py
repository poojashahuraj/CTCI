class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]

        def dynamic_prg(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            for x in xrange(i, j + 1):
                dp[i][j] = max(dp[i][j],dynamic_prg(i, x - 1) +
                               nums[i - 1] * nums[x] * nums[j + 1]+
                               dynamic_prg(x + 1, j))
            return dp[i][j]
        return dynamic_prg(1,n)

s = Solution()
print s.maxCoins(nums=[3, 1, 5, 8])