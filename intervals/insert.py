# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150


intervals = [[1,3],[6,9]]
newInterval = [2,5]

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged