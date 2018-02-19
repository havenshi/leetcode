# Complete the function below.
# this is dfs and combination
# we can use from scipy.special import comb in other IDE, but it's not a basic module so we can't use here
import operator


def dfs(grid, i, j):
    if i > len(grid) - 1 or i < 0 or j > len(grid[0]) - 1 or j < 0:
        return
    if grid[i][j] == 'N':
        return
    grid[i][j] == 'N'
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)


def combination(count, i):
    return reduce(operator.mul, range(count - i + 1, count + 1)) / reduce(operator.mul, range(1, i + 1))


def Group(grid):
    ans = 0
    if not len(grid):
        ans = 0
    else:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'Y':
                    dfs(grid, i, j)
                    ans += 1

    count = 0
    for i in range(ans / 2 * 2 + 1):
        count += combination(count, i)
    return count