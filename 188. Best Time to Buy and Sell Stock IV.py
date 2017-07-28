# -*- coding:utf8 -*-
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if 2 * k > size:  # 操作所需元素超过了size，就可以无视k次的限制
            if len(prices) < 2:
                return 0
            current = prices[0]
            profit = 0
            for i in range(1, size):
                if prices[i] > current:
                    profit += (prices[i] - current)
                current = prices[i]
            return profit

        max_buy = [float("-inf") for _ in range(k + 1)]
        max_sell = [0 for _ in range(k + 1)]

        for i in range(size):
            for j in range(1, min(k, i / 2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])  # 上次sell之后的总利润 - 这次买的price
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])  # 这次买之后的总利润 + 这次卖的price

        return max_sell[k]

if __name__ == "__main__":
    print Solution().maxProfit(3, [2,4,2,4,2,4])