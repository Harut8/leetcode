# https://leetcode.com/problems/non-overlapping-intervals/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count
