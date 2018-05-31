class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.unique(m,n,obstacleGrid,path={})

    def unique(self,m,n,obstacleGrid,path):
        if m == 1 and n == 1 and obstacleGrid[m-1][n-1] == 0:  # base statement
            return 1
        elif m >= 1 and n >=1 and obstacleGrid[m-1][n-1] == 1:   # pay attention to -1
            path[m, n] = 0
            return 0
        elif m == 0 or n == 0:   # range
            return 0
        else:
            if (m-1,n) in path:
                ver = path[(m-1,n)]
            else:
                ver = self.unique(m - 1, n, obstacleGrid, path)
            if (m,n-1) in path:
                hor = path[(m,n-1)]
            else:
                hor = self.unique(m, n - 1, obstacleGrid, path)
            step = ver + hor
            path[m,n] = step
            return step


if __name__ == "__main__":
    answer=Solution()
    print answer.uniquePathsWithObstacles([
[0,0]
])



class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                res[i][0] == 0
                break
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                res[0][i] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]