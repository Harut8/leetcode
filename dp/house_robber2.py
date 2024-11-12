# https://leetcode.com/problems/house-robber-ii/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_sum(_nums):
            if not _nums:
                return 0
            if len(_nums) == 1:
                return _nums[0]
            dp = [0] * len(_nums)
            dp[0] = _nums[0]
            dp[1] = max(_nums[0], _nums[1])
            for i in range(2, len(_nums)):
                dp[i] = max(dp[i-1], dp[i-2]+_nums[i])
            return dp[-1]
        return max(find_sum(nums[:-1]), find_sum(nums[1:]))
