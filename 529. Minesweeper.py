class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j, m, n)
        return board

    def dfs(self, board, i, j, m, n):
        if board[i][j] != 'E':
            return  # 只有E未作过判断的情况下才继续运行，否则MBXD都表明已经遍历过

        cnt = 0
        for d in zip((-1, -1, -1, 0, 1, 0, 1, 1), (-1, 1, 0, -1, 0, 1, 1, -1)):
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'M':
                cnt += 1
        if cnt == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(cnt)
            return  # 只有B的情况才继续dfs，如果有数字返回仄无需继续

        for d in zip((-1, -1, -1, 0, 1, 0, 1, 1), (-1, 1, 0, -1, 0, 1, 1, -1)):
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n:
                self.dfs(board, ii, jj, m, n)