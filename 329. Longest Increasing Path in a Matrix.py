class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 枚举起点，从每一个单元格出发，递归寻找其最长递增路径。
        # 利用辅助数组dp记录已经搜索过的单元格，dp[x][y]存储从单元格(x, y)出发的最长递增路径长度。
        h = len(matrix)
        if h == 0: return 0
        w = len(matrix[0])

        def dfs(x, y):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] > matrix[x][y]:
                    if not dp[nx][ny]:
                        dp[nx][ny] = dfs(nx, ny)
                    dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
            dp[x][y] = max(dp[x][y], 1)
            return dp[x][y]

        dp = [[0] * w for x in range(h)]
        for x in range(h):
            for y in range(w):
                if not dp[x][y]:
                    dp[x][y] = dfs(x, y)
        return max([max(x) for x in dp])