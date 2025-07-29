# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

nums = [2,3,1,1,4]

def jump(nums):
    jumps = 0
    end = 0
    max_reach = 0
    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == end:
            jumps += 1
            end = max_reach
    return jumps