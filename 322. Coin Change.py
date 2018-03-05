class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # method1 因为横坐标amount所有可能性，所以TLE
        # if amount == 0:
        #     return 0
        # coins.sort()
        # dp = [0]*(amount+1)
        # for a in range(1, amount+1): # 注意如果coin为横坐标，遍历横坐标说明每个coin只能用一次，错误，故amount为横坐标
        #     newdp = dp[:]
        #     for coin in [x for x in coins if x <= a]:
        #         if dp[a-coin] or a-coin==0: # 注意如果没有i-coin==0的条件，则dp[0]=0都会漏掉
        #             if newdp[a] == 0:
        #                 newdp[a] = 1+dp[a-coin]
        #             else:
        #                 newdp[a] = min(newdp[a], 1+dp[a-coin])
        #     dp = newdp
        # return dp[-1] if dp[-1]!=0 else -1

        # method2 为什么不超时？因为dp[x + c]由dp[x]推导出，因此省了很多中间值
        # bfs，因为一找到就停止，所以比dp更快
        # 将问题转化为求X轴0点到坐标点amount的最短距离
        import collections
        queue = collections.deque([0])
        steps = {0:0}
        while queue:
            cur = queue.popleft()
            level = steps[cur]
            if cur == amount: # 如果达到了该距离，返回步长
                return level
            for coin in coins:
                if cur + coin > amount:
                    continue
                if (cur + coin) not in steps:
                    queue.append(cur + coin)
                    steps[cur + coin] = level + 1
        return -1