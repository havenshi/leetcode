class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
    #     # dfs1
    #     if not board:
    #         return
    #     for i in range(1, len(board) - 1):  # begin from top left 1, bottom right -1
    #         for j in range(1, len(board[0]) - 1):
    #             if self.dfs(board, i, j):
    #                 board[i][j] = 'X'
    #     return board
    #
    # def dfs(self, board, i, j):
    #     if i > len(board) - 1 or i < 0 or j > len(board[0]) - 1 or j < 0:
    #         return False
    #     if board[i][j] == 'X':
    #         return True
    #     board[i][j] = 'X'  # set the begin to 'X' temporarily
    #     res = self.dfs(board, i + 1, j) and self.dfs(board, i, j + 1) and self.dfs(board, i - 1, j) and self.dfs(board,
    #                                                                                                              i,
    #                                                                                                              j - 1)
    #     board[i][j] = 'O'  # return it back
    #     return res
    #
    #     # dfs2
    #     m = len(board)
    #     if m == 0:
    #         return
    #     n = len(board[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 or i == m - 1:
    #                 self.bfs(board, i, j)
    #             else:
    #                 if j == 0 or j == n - 1:
    #                     self.bfs(board, i, j)
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == 'O':
    #                 board[i] = board[i][:j] + 'X' + board[i][j + 1:]
    #             elif board[i][j] == 'D':
    #                 board[i] = board[i][:j] + 'O' + board[i][j + 1:]
    #
    # def bfs(self, board, i, j):
    #     if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
    #         return
    #     elif board[i][j] == 'X' or board[i][j] == 'D':
    #         return
    #     elif board[i][j] == 'O':
    #         board[i] = board[i][:j] + 'D' + board[i][j + 1:]
    #         self.bfs(board, i + 1, j)
    #         self.bfs(board, i - 1, j)
    #         self.bfs(board, i, j + 1)
    #         self.bfs(board, i, j - 1)

        # bfs
        queue = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1 and board[i][
                    j] == 'O':  # find the 'O' on the edge
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            if i in range(len(board)) and j in range(len(board[0])) and board[i][j] == "O":
                board[i][j] = 'D'  # change the value of edge 'O' to 'D'
                queue.append((i - 1, j))  # append 4 dot of the 'O' into queue
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))
        # 'O' on the edge will change to 'D', 'O' in the middle will never change (since its 4 dot will never access to edge)

        # traversal the board again, 'D'->'O', 'O'->'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"

if __name__ == '__main__':
    answer = Solution()
    print answer.solve([["X","O","X","X"],
                        ["O","X","O","X"],
                        ["X","O","X","O"],
                        ["O","X","O","X"]])

