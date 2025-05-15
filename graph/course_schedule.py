# https://leetcode.com/problems/course-schedule/
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visited = set()
        rec_stack = set()
        def dfs(course):
            if course in visited:
                return False
            if course in rec_stack:
                return True
            rec_stack.add(course)
            for ng in graph[course]:
                if dfs(ng):
                    return True
            visited.add(course)

            rec_stack.remove(course)
            return False
        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return False
        return True

