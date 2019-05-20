class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[x] 表示删除不大于x的所有数字的最大得分。
        # cnt[x] 存储数字x的个数。
        if not nums: return 0

        cnt = collections.Counter(nums)
        dp = [0 for i in range(max(nums) + 1)]
        dp[1] = 1 * cnt[1]
        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * cnt[i])
        return dp[-1]