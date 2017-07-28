class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lent = len(t)
        lens = len(s)
        dp = [[0] * (lent + 1) for _ in range(lens + 1)]
        for i in range(lens + 1):
            dp[i][0] = 1
        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[lens][lent]