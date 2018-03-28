class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # method1 time limit exceeded
    #     m = len(grid)
    #     n = len(grid[0])
    #     return self.unique(m, n, grid, path={})
    #
    # def unique(self, m, n, grid, path):
    #     if m == 1 and n == 1:
    #         path[(m, n)] = grid[m - 1][n - 1]
    #         return grid[m - 1][n - 1]
    #     else:
    #         step = sum(sum(i) for i in grid)  # sum elements in matrix
    #         if m > 1 and n > 1:
    #             if (m - 1, n) in path:
    #                 ver = path[(m - 1, n)] + grid[m - 1][n - 1]
    #             else:
    #                 ver = self.unique(m - 1, n, grid, path) + grid[m - 1][n - 1]
    #             if (m, n - 1) in path:
    #                 hor = path[(m, n - 1)] + grid[m - 1][n - 1]
    #             else:
    #                 hor = self.unique(m, n - 1, grid, path) + grid[m - 1][n - 1]
    #             step = min(ver, hor)
    #         elif m == 1 and n > 1:
    #             if (m, n - 1) in path:
    #                 step = path[(m, n - 1)] + grid[m - 1][n - 1]
    #             else:
    #                 step = self.unique(m, n - 1, grid, path) + grid[m - 1][n - 1]
    #         elif n == 1 and m > 1:
    #             if (m - 1, n) in path:
    #                 step = path[(m - 1, n)] + grid[m - 1][n - 1]
    #             else:
    #                 step = self.unique(m - 1, n, grid, path) + grid[m - 1][n - 1]
    #         path[m, n] = step
    #         return step

        # method2
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[0][j] = dp[0][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
if __name__ == "__main__":
    answer=Solution()
    print answer.minPathSum([
[1,2],[4,5]
])
