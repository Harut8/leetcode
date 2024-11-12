# https://leetcode.com/problems/combination-sum-ii/

candidates = [10,1,2,7,6,1,5]
target = 8

def combinationSum(candidates, target):
    res = []
    candidates.sort()
    def backtrack(current_sub, start, rem):
        if rem == 0:
            res.append(current_sub[:])
            return
        if rem < 0:
            return
        for i in range(start, len(candidates)):
            # same as com_sum but need to check for duplicates after sorting
            if i > start and candidates[i] == candidates[i-1]:
                continue
            current_sub.append(candidates[i])
            backtrack(current_sub, i+1, rem - candidates[i])
            current_sub.pop()
    backtrack([], 0, target)
    return res
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(candidates, target))