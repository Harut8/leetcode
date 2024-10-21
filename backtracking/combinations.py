# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, curr_sub):
            if len(curr_sub) == k:
                res.append(curr_sub[:])
                return
            for i in range(start, n + 1):
                curr_sub.append(i)
                backtrack(i+1, curr_sub)
                curr_sub.pop()
        backtrack(1, [])
        return res

"""
"""