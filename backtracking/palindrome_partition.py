# https://leetcode.com/problems/palindrome-partitioning/
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(w):
            return w[::-1] == w
        res = []
        def backtrack(idx, subsets):
            if idx == len(s):
                res.append(subsets[:])
            for i in range(idx, len(s)):
                _word = s[idx: i + 1]
                if is_palindrome(_word):
                    subsets.append(_word)
                    backtrack(i+1,subsets)
                    subsets.pop()
        backtrack(0, [])
        return res

