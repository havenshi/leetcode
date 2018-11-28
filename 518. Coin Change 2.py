class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] += dp[x - c]
        return dp[amount]