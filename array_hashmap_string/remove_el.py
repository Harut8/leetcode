# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def removeElement(nums: list[int], val: int) -> int:
    l = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l] = nums[i]
            l += 1
    return l
