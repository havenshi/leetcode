class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):  # 越晚begin则可能的subseq越短，所以从后往前遍历
            dp[i][i] = 1
            for l in range(1, n - i):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # emmmm

        return dp[0][n - 1]