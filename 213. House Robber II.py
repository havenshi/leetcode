class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp1 = self.helper(nums[:-1]) + [0]  # if rob the first, cannot rob the last
        dp2 = [0] + self.helper(nums[1:])  # if not rob the first, can rob the last
        return max(dp1[-2], dp2[-1])

    def helper(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp