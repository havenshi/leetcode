class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m, n = len(M), len(M[0])
        ans = 0
        hori = [[0] * n for x in range(m)]
        for i in range(m):
            hori[i][0] = M[i][0]
        diag = [M[0]] + [[0] * n for x in range(m-1)]
        for i in range(m):
            for j in range(1, n):
                hori[i][j] = M[i][j] * (hori[i][j-1] + 1)
                if i > 0 and j > 0:
                    diag[i][j] = M[i][j] * (diag[i-1][j-1] + 1)
                ans = max(ans, hori[i][j], diag[i][j])

        vert = [M[0]] + [[0] * n for x in range(m-1)]
        anti = [M[0]] + [[0] * n for x in range(m-1)]
        for j in range(n-1, -1, -1):
            for i in range(1, m):
                vert[i][j] = M[i][j] * (vert[i - 1][j] + 1)
                if i > 0 and j < n-1:
                    anti[i][j] = M[i][j] * (anti[i - 1][j + 1] + 1)
                ans = max(ans, vert[i][j], anti[i][j])

        return ans

if __name__ == '__main__':
    print Solution().longestLine([[0,1,1,0],
                                   [1,1,1,1],
                                   [0,0,0,1]])