# https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        start = 0
        res = []
        for end in range(1, len(nums)):
            if nums[end] != nums[end - 1] + 1:
                res.append(f"{nums[start]}->{nums[end - 1]}" if start != end - 1 else f"{nums[start]}")
                start = end
        res.append(f"{nums[start]}->{nums[end]}" if start != end else f"{nums[start]}")
        return res
