class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n1 + 1) for i in range(n2 + 1)]

        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return n1 + n2 - 2 * dp[-1][-1]