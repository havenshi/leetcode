# have to step (m-1) on horizontal axis, step (n-1) on vertical axis.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.unique(m,n,path={})   # must set path outside. can't set path inside a function, or it will initiate every time.

    def unique(self,m,n,path):
        if m == 1 or n == 1:
            return 1
        else:
            if (m-1,n) in path:
                ver = path[(m-1,n)]
            else:
                ver = self.unique(m - 1, n, path)
            if (m,n-1) in path:
                hor = path[(m,n-1)]
            else:
                hor = self.unique(m, n - 1, path)
            step = ver + hor
            path[m,n] = step
            return step


if __name__ == "__main__":
    answer=Solution()
    print answer.uniquePaths(33,12)




class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1] for i in range(m)]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(0, n):
                list[0][i] = 1
            for i in range(0, m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1]


# 或者用C(n,k)，n为m+n-2，k为m-1
reduce((lambda x, y: x * y), range(1,5))