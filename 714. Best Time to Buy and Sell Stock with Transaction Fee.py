class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        hold = [0] * len(prices)
        sold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            hold[i] = max(hold[i - 1], sold[i - 1] - prices[i])  # minimum to hold it, sold[i - 1] - prices[i]!
            sold[i] = max(sold[i - 1], hold[i - 1] - fee + prices[i])  # dp, sold is max profit, price-hold-fee
        return sold[-1]