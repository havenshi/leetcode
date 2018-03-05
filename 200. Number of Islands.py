class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        newgrid = [list(x) for x in grid]
        ans = 0
        if not len(newgrid):
            return ans
        m = len(newgrid)
        n = len(newgrid[0])
        for i in range(m):
            for j in range(n):
                if newgrid[i][j] == '1':
                    self.dfs(newgrid, i, j)
                    ans += 1
        return ans

    def dfs(self, map, x, y):
        if x > len(map) - 1 or x < 0 or y > len(map[0]) - 1 or y < 0:
            return
        if map[x][y] == '0':
            return
        map[x][y] = '0'
        self.dfs(map, x + 1, y)
        self.dfs(map, x, y + 1)
        self.dfs(map, x - 1, y)
        self.dfs(map, x, y - 1)

    # method 2 union find
        grid = [map(lambda x: int(x), row) for row in grid]
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        root = [0] + [0] * ((m * n) / 2 + 1)  # record index(original count) and value(current count after many changes)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not ((i > 0 and grid[i - 1][j]) or (j > 0 and grid[i][j - 1])):
                        count += 1
                        root[count] = count
                        grid[i][j] = count
                    else:
                        if i > 0 and grid[i - 1][j] and j > 0 and grid[i][j - 1]:
                            grid[i][j] = grid[i - 1][j]
                            root = [grid[i][j] if x == grid[i][j - 1] else x for x in root]
                            # replace left value with upper value
                        elif i > 0 and grid[i - 1][j]:
                            grid[i][j] = root[grid[i - 1][j]]
                        elif j > 0 and grid[i][j - 1]:
                            grid[i][j] = root[grid[i][j - 1]]
                            # print i,j,root
        return sum([1 for i in range(len(root)) if i == root[i]]) - 1


if __name__ == '__main__':
    print Solution().numIslands(["11110","11010","11000","00000"])

