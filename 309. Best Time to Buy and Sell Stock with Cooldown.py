# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # sells[i]表示在第i天卖出股票所能获得的最大累积收益
        # buys[i]表示在第i天买入股票所能获得的最大累积收益
        #
        # 初始化令sells[0] = 0，buys[0] = -prices[0]
        #
        # 第i天交易时获得的累计收益只与第i - 1天与第i - 2天有关
        #
        # 记第i天与第i - 1天的价格差：delta = price[i] - price[i - 1]
        #
        # 状态转移方程为：
        # sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta)
        # buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)
        # 上述方程的含义为：
        # 第i天卖出的最大累积收益 = max(第i - 1天买入~第i天卖出的最大累积收益, 第i - 1天卖出后反悔~改为第i天卖出的最大累积收益)
        # 第i天买入的最大累积收益 = max(第i - 2天卖出~第i天买入的最大累积收益, 第i - 1天买入后反悔~改为第i天买入的最大累积收益)

        size = len(prices)
        if not size:
            return 0
        buys = [None] * size
        sells = [None] * size
        sells[0], buys[0] = 0, -prices[0]
        for x in range(1, size):
            delta = prices[x] - prices[x - 1]
            sells[x] = max(buys[x - 1] + prices[x], sells[x - 1] + delta)
            buys[x] = max(buys[x - 1] - delta, sells[x - 2] - prices[x] if x > 1 else None)
        return max(sells)

        # if not prices:
        #     return 0
        # n = len(prices)
        # sell = prices[n-1]
        # sell_index = n-1
        # profit = [0] * n
        # s = [0] * n # 记录产生profit的该buy点是在哪天sell的
        # for i in range(n-2, -1, -1):
        #     if prices[i] <= sell:
        #         tmp = sell-prices[i] # 新的profit
        #         profit[i] = tmp
        #         s[i] = sell_index # 原本在这天sell_index卖，更新s值
        #         if profit[sell_index] > 0: # 对应的sell_index天不卖，连起来的情况
        #             profit[i] = tmp+profit[sell_index]
        #             s[i] = s[sell_index] # 记得更新s
        #         newbuy_index = sell_index+2 # cooldown
        #         for j in range(newbuy_index, n):
        #             if profit[i] < tmp+profit[j]:
        #                 profit[i] = tmp+profit[j] # 此时不用更新s
        #         sell = prices[i]
        #         sell_index = i
        #     else:
        #         # 为啥[6,1,3,2,4,7]是6？应该是5啊
        #         # 该行导致错误，因为3的时候profit只能记录一定在3卖的情况（即profit为3），而无法记录跳过3的情况（即profit为5）
        #         profit[i] = max(profit[i+2:]) # 虽然该点只能卖不产生新profit，但可以更新为后面所有profit的最大值
        #         sell = prices[i]
        #         sell_index = i
        # print profit
        # return max(profit)

