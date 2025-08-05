# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75


def findMaxAverage(nums: list[int], k: int) -> float:
    i = 0
    mx = float("-inf")
    curr = 0
    while i <= len(nums) - 1:
        curr += nums[i]
        if i >= k - 1:
            mx = max(mx, curr / k)
            curr -= nums[i - k + 1]
        i += 1
    return mx
