# https://leetcode.com/problems/n-queens/
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        board = [["." for _ in range(n)] for _ in range(n)]
        def is_safe(row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            # main diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False
            # secondary diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == "Q":
                    return False
            return True
        def backtrack(row):
            if row == n:  # all queens have been used
                solutions.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack(0)
        return solutions

