# https://leetcode.com/problems/word-search/
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def dfs(board, word, i, j, k):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] != word[k]:
        return False
    if k == len(word) - 1:
        return True
    board[i][j] = "#"
    res = dfs(board, word, i+1, j, k+1) or dfs(board, word, i-1, j, k+1) or dfs(board, word, i, j+1, k+1) or dfs(board, word, i, j-1, k+1)
    board[i][j] = word[k]
    return res

def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True
    return False