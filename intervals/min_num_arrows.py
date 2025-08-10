# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 0
        end = float('-inf')
        for balloon in points:
            if balloon[0] > end:
                arrows += 1
                end = balloon[1]
        return arrows