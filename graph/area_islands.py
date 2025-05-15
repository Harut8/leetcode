# https://leetcode.com/problems/max-area-of-island/submissions/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col):
            grid[row][col] = 0
            area = 1
            for dx, dy in (
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0)
            ):
                _new_row = row + dx
                _new_col = col + dy
                if 0<=_new_row<_rows and 0<=_new_col<_cols and grid[_new_row][_new_col] == 1:
                    area += dfs(_new_row, _new_col)
            return area
        _rows = len(grid)
        _cols = len(grid[0])
        _area = 0
        for row in range(_rows):
            for col in range(_cols):
                if grid[row][col] == 1:
                    _area = max(_area, dfs(row, col))
        return _area
