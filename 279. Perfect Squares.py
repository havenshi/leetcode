# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
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
