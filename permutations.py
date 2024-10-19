# https://leetcode.com/problems/permutations/


def perm(nums):
    res = []
    def backtrack(current_perm):
        if len(current_perm) == len(nums):
            res.append(current_perm.copy())
            return
        for num in nums:
            if num not in current_perm:
                current_perm.append(num)
                backtrack(current_perm)
                current_perm.pop()
    backtrack([])
    return res