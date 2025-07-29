# https://leetcode.com/problems/valid-sudoku/
import collections

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def valid_sudoku(_board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for i in range(9):
        for j in range(9):
            if _board[i][j] == '.':
                continue
            if (_board[i][j] in rows[i] or
                    _board[i][j] in cols[j] or
                    _board[i][j] in squares[(i // 3, j // 3)]):
                return False
            rows[i].add(_board[i][j])
            cols[j].add(_board[i][j])
            squares[(i // 3, j // 3)].add(_board[i][j])

    return True


print(valid_sudoku(board))
