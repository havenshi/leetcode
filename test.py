import operator


def dfs(grid_matrix, i, j):
    if i > len(grid_matrix) - 1 or i < 0 or j > len(grid_matrix[0]) - 1 or j < 0:
        return
    if grid_matrix[i][j] == 'N':
        return
    grid_matrix[i][j] = 'N'
    dfs(grid_matrix, i + 1, j)
    dfs(grid_matrix, i, j + 1)
    dfs(grid_matrix, i - 1, j)
    dfs(grid_matrix, i, j - 1)


def combination(count, i):
    return reduce(operator.mul, range(count - i + 1, count + 1)) / reduce(operator.mul, range(1, i + 1))


def Group(grid):
    ans = 0
    grid_matrix = [list(x) for x in grid]
    print grid_matrix
    if not len(grid_matrix):
        ans = 0
    else:
        m = len(grid_matrix)
        n = len(grid_matrix[0])
        for i in range(m):
            for j in range(n):
                if grid_matrix[i][j] == 'Y':
                    dfs(grid_matrix, i, j)
                    ans += 1

    count = 0
    for i in range(ans / 2 * 2 + 1):
        count += combination(count, i)
    return count

