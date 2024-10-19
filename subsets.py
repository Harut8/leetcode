#mhttps://leetcode.com/problems/subsets/

def subsets(nums):
    res = []
    def backtrack(sub, idx):
        res.append(sub.copy())
        for i in range(idx, len(nums)):
            j = nums[i]
            sub.append(j)
            backtrack(sub, i + 1)
            sub.pop()

    backtrack([], 0)
    return res

print(subsets([1,2,3]))