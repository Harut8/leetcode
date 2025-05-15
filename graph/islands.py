# https://leetcode.com/problems/number-of-islands/submissions/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row, col):
            grid[row][col] = '0'
            for dx, dy in (
                    (0, 1),
                    (0, -1),
                    (-1,0),
                    (1,0)
            ):
                new_row = row+dx
                new_col = col+dy
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)
        _count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    _count += 1

        return _count
