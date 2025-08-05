# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    op = 0
    while l < r:
        sm = nums[r] + nums[l]
        if sm == k:
            op += 1
            r -= 1
            l += 1
        elif sm < k:
            l += 1
        else:
            r -= 1
    return op