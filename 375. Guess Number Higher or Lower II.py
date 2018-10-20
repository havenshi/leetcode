# Time:O(n^3)
# Space:O(n^2)
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n-gap+1):
                hi = lo + gap
                # split to lo~x-1, x, x+1~hi
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi])for x in range(lo, hi))#???
        return dp[1][n]