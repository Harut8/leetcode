# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def longestOnes(nums: list[int], k: int) -> int:
    l = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        while k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

print(longestOnes(nums, k))