class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分治法，O(n^3)
        # 以最后被爆破的气球m为界限，把数组分为左右两个子区域
        # 状态转移方程：
        # dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])

        n = len(nums)
        dp = [[0] * (n + 2) for x in range(n + 2)]
        # for i in range(1, n+1):
        #     dp[i][i] = nums[i-1]
        # for i in range(1, n):
        #     dp[i][i+1] = nums[i-1]*nums[i]+max(nums[i-1],nums[i])
        nums = [1] + nums + [1]

        for k in range(n):  # left和right之间的跨度，总长度为1~n。为什么先从跨度开始遍历呢？这样可以保证dp值最先从left和right重叠或相邻的位置开始
            for l in range(1, n - k + 1):  # 即left为0~n-k
                r = l + k
                for m in range(l, r + 1):  # 用m隔开两段，包含与lr点重合的情况
                    dp[l][r] = max(dp[l][r], dp[l][m - 1] + nums[l - 1] * nums[m] * nums[r + 1] + dp[m + 1][r])

        return dp[1][n]

        # 直接用dfs+memorization会爆
    #     import collections
    #     if len(nums) == 0:
    #         return 0
    #     self.dictionary = collections.defaultdict(int)
    #     return self.dfs([1] + nums + [1])
    #
    # def dfs(self, nums):
    #     if str(nums) in self.dictionary:
    #         return self.dictionary[str(nums)]
    #
    #     if len(nums) == 3:
    #         self.dictionary[str(nums)] = reduce(lambda x, y: x * y, nums)
    #         return reduce(lambda x, y: x * y, nums)
    #     res = 0
    #     for i in range(1, len(nums) - 1):
    #         res = max(res, nums[i - 1] * nums[i] * nums[i + 1] + self.dfs(nums[:i] + nums[i + 1:]))
    #     self.dictionary[str(nums)] = res
    #     return res