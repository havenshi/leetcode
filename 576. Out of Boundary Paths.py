class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        mod = 10 ** 9 + 7
        cache = collections.defaultdict(int)

        def helper(i, j, N):
            # 记忆化思想
            if (i, j, N) in cache:
                return cache[(i, j, N)]
            # i,j在网格内情况
            if 0 <= i < m and 0 <= j < n:
                if N == 0:
                    cache[(i, j, N)] = 0
                    return cache[(i, j, N)]

                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    cache[(i, j, N)] += helper(x, y, N - 1)
                return cache[(i, j, N)] % mod
            # 网格外情况
            else:
                cache[(i, j, N)] = 1
                return cache[(i, j, N)]

        return helper(i, j, N) % mod


# 错误解法，ij可以回头，所以visits使用不对
# 直接去掉visits会LTE
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.ans = 0
        visits = set()
        self.dfs(m, n, N, i, j, visits)
        return self.ans

    def dfs(self, m, n, N, i, j, visits):
        if N < 0 or (i, j) in visits:
            return
        if i < 0 or i >= m or j < 0 or j >= n:
            self.ans += 1
            return
        visits.add((i, j))
        for ii, jj in zip((-1, 0, 1, 0), (0, -1, 0, 1)):
            ni, nj = i + ii, j + jj
            self.dfs(m, n, N - 1, ni, nj, visits)
        visits.remove((i, j))
