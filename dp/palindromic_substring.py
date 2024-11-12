# https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expand(lft, rgt):
            count = 0
            while lft >=0 and rgt < len(s) and s[lft] == s[rgt]:
                count += 1
                lft -= 1
                rgt += 1
            return count
        cnt = 0
        for i in range(len(s)):
            answ1 = expand(i, i + 1)
            answ2 = expand(i, i)
            cnt += answ1 + answ2
        return cnt


