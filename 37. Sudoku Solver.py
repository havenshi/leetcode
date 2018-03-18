# Time:  ((9!)^9)
# Space: (1)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValidSudoku(i, j, board) and self.dfs(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True

    def isValidSudoku(self, i, j, board):
        for x in range(9):
            if board[i][j] == board[i][x] and j != x or board[i][j] == board[x][j] and i != x:
                return False
        for x in range(3):
            for y in range(3):
                xx = i / 3 * 3 + x
                yy = j / 3 * 3 + y
                if board[i][j] == board[xx][yy] and not (i == xx and j == yy):
                    return False
        return True