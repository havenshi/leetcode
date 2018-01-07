class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = range(n + 1)  # [0,1...12]
        square_root = int(n ** 0.5)
        for i in range(2, square_root + 1):  # rows from 2 to square_root, i*2 is 4 to 9
            for j in range(i ** 2, n + 1):
                tmp = dp[j - i ** 2] + 1  # 12 is min of dp[12-9]+1 or dp[12-4]+1
                dp[j] = min(dp[j], tmp)
        return dp[-1]
