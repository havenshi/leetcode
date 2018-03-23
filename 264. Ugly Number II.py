# Time:  O(n)
# Space: O(1)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        i2 = i3 = i5 = 0
        i = 1
        while i < n:
            m2, m3, m5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            dp[i] = min(m2, m3, m5)
            if dp[i] == m2:
                i2 += 1
            if dp[i] == m3:
                i3 += 1
            if dp[i] == m5:
                i5 += 1
            i += 1
        return dp[-1]