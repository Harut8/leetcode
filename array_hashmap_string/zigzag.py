# https://leetcode.com/problems/zigzag-conversion/submissions/1713190650/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        _total = [''] * numRows
        start = 0
        step = -1
        for char in s:
            _total[start] += char
            if start == numRows - 1 or start == 0:
                step *= -1
            start += step
        return "".join(_total)

