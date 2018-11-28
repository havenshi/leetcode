# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.

# BFS + Map
#
# 利用BFS可以求出某个岛屿的所有点坐标，用top, left表示这些坐标的最上和最左。
#
# 将所有坐标(x, y) 变换为 (x - top, y - left)，即可实现平移变换。

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    islands.add(self.bfs(grid, x, y))
        return len(islands)

    def bfs(self, grid, x, y):
        w, h = len(grid), len(grid[0])
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        queue = [(x, y)]
        grid[x][y] = 0
        ans = []
        while queue:
            x, y = queue.pop(0)
            ans.append((x, y))
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if grid[nx][ny]:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
        top = min(x for x, y in ans)
        left = min(y for x, y in ans)
        return tuple((x - top) * h + y - left for x,  y in sorted(ans))