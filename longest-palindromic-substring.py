# https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def longestPalindrome(self, s):
        def expand(lft, rgt):
            while lft >= 0 and rgt < len(s) and s[lft] == s[rgt]:
                lft -= 1
                rgt += 1
            return rgt - lft - 1

        start, end = 0, 0
        for i in range(len(s)):
            ln1 = expand(i, i)
            ln2 = expand(i, i + 1)
            max_len = max(ln1, ln2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
