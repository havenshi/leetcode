# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time O(n2)
        # dp，动态转移方程dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]
        # size = len(nums)
        # dp = [1] * size
        # for x in range(size):
        #     for y in range(x):
        #         if nums[x] > nums[y]:
        #             dp[x] = max(dp[x], dp[y] + 1)
        # return max(dp) if dp else 0

        # 二分法，遍历nums数组，二分查找每一个数在单调序列dp中的位置，然后替换之。
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp): # 如果这个数的位置≥dp的长度，需要加上
                dp.append(nums[x])
            else:              # 否则说明这个数应该在dp中，则其值一定比它在dp中的原有数值要小，替换
                dp[low] = nums[x]
            print low,dp
        return len(dp)

if __name__ == "__main__":
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

        # # TLE
        # n = len(nums)
        # if not n:
        #     return 0
        #
        # dp = [[None] * (n) for i in range(n + 1)]
        # #  设bj为长度为j的递增子序列的末尾最小值
        # for j in range(n):
        #     dp[0][j] = 0
        #
        # count = 0
        # for i in range(1, n + 1):
        #     for j in range(i - 1, n):
        #         if i == 1:
        #             if j == 0:
        #                 dp[i][j] = nums[j]
        #             else:
        #                 dp[i][j] = min(dp[i][j - 1], nums[j])
        #         else:
        #             if dp[i - 1][j] != None and nums[j] > dp[i - 1][j]:
        #                 if dp[i][j - 1] != None:  # if left is None, cannot compare
        #                     dp[i][j] = min(dp[i][j - 1], nums[j])
        #                 else:
        #                     dp[i][j] = nums[j]
        #             else:
        #                 for x in range(j - 1, i - 2, -1):
        #                     if dp[i][x] != None:
        #                         dp[i][j] = dp[i][x]
        #
        #     if sum(1 for j in range(n) if dp[i][j] == None) != n:
        #         count += 1
        # return count