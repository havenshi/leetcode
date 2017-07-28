class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后进行一次交易所获得的最大利润。
        # 则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动态规划了。
        n = len(prices)
        if n <= 1:
            return 0
        p1 = [0] * n
        p2 = [0] * n

        minv = prices[0]
        for i in range(1, n):
            minv = min(minv, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - minv)

        maxv = prices[-1]
        for i in range(n - 2, -1, -1):
            maxv = max(maxv, prices[i])
            p2[i] = max(p2[i + 1], maxv - prices[i])

        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        print p1, p2
        return res