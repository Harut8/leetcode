# https://leetcode.com/problems/h-index/submissions/1714654295/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True) # histogram solution algorithm (increase line that divides the histogram until h is found)
        h = 0
        while h < len(citations) and citations[h] >= h + 1:
            h+= 1
        return h
