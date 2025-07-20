# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = current = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            total = max(total, current)
        return total

"""
AMEN QAYLOV MENQ KAROX ENQ KAM MECACNEL KAM POQRACNEL ARJEQY
ETE PORACNUM ENQ APA KARELI E VERCNEL AYN SKIZB
AMEN QAYLIN KATARUM ENQ VOROSHUM
SKSEL NOR SUBARRAY TE GUMAREL EXACI VRA
"""