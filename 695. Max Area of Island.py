# Time: O(mn)
# Space: O(1)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.helper(grid, m, n, i, j))
        return res

    def helper(self, grid, m, n, i, j):
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.helper(grid, m, n, i + 1, j) + self.helper(grid, m, n, i, j + 1) + self.helper(grid, m, n,i - 1,j) + self.helper(grid, m, n, i, j - 1)
        return 0




        # class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m = len(grid)
#         if not m: return 0
#         n = len(grid[0])
#         self.res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     self.helper(grid, m, n, i, j, 0)
#         return self.res
#
#     def helper(self, grid, m, n, i, j, tmp):
#         if i < 0 or i >= m or j < 0 or j >= n:
#             return tmp
#         elif grid[i][j] == 1:
#             grid[i][j] = "#"
#             tmp += 1
#             newtmp = self.helper(grid, m, n, i + 1, j, tmp)
#             tmp = newtmp
#             newtmp = self.helper(grid, m, n, i, j + 1, tmp)
#             tmp = newtmp
#             newtmp = self.helper(grid, m, n, i - 1, j, tmp)
#             tmp = newtmp
#             newtmp = self.helper(grid, m, n, i, j - 1, tmp)
#             tmp = newtmp
#
#             self.res = max(self.res, tmp)
#             return tmp
#         return tmp