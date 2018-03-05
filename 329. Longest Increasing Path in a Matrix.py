class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 枚举起点，从每一个单元格出发，递归寻找其最长递增路径。
        # 利用辅助数组dp记录已经搜索过的单元格，dp[x][y]存储从单元格(x, y)出发的最长递增路径长度。
        self.m = len(matrix)
        if self.m == 0: return 0
        self.n = len(matrix[0])
        self.dp = [[0] * self.n for i in range(self.m)]

        for x in range(self.m):
            for y in range(self.n):
                self.dfs(x, y, matrix)
        return max([max(row) for row in self.dp])

    def dfs(self, x, y, matrix):
        if not self.dp[x][y]:
            self.dp[x][y] = 1
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n and matrix[nx][ny] > matrix[x][y]:
                if not self.dp[nx][ny]:
                    self.dfs(nx, ny, matrix)
                self.dp[x][y] = max(self.dp[x][y], self.dp[nx][ny] + 1)
