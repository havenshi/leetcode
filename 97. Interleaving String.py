class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # dp[i][j]表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1] # s3完全由s1组成
        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s3[i - 1] == s2[i - 1] # s3完全由s2组成
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) # s3的最后一位与s1或s2的最后一位相同
        return dp[len(s1)][len(s2)]