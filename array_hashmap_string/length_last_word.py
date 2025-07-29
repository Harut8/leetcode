# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # skip trailing
        i = len(s) - 1
        l = 0
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            l += 1
            i -= 1
        return l
