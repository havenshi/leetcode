class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) time
        n = len(nums)
        dp_before = [1] * n
        dp_after = [1] * n
        for i in range(1, n):
            dp_before[i] = dp_before[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            dp_after[i] = dp_after[i+1] * nums[i+1]
        for i in range(n):
            dp_before[i] *= dp_after[i]
        return dp_before

        # method2, O(n) time, O(1) space
        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     dp[i] = dp[i-1] * nums[i-1]
        # right = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     dp[i] *= right
        #     right *= nums[i]
        # return dp