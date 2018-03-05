class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE
        # res = 0
        # start = -1
        #
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1]:  # 发现ith的数小于之前的，设为end，接下来寻找正确的位置start
        #         j = i
        #         while j > 0 and nums[j] < nums[j - 1]:
        #             nums[j], nums[j - 1] = nums[j - 1], nums[j]
        #             j -= 1
        #
        #         # 如果新的start比较小，更新start到最小值
        #         if start == -1 or start > j:
        #             start = j
        #         res = max(res, i - start + 1)
        #
        # return res

        # O(nlgn)
        snums = sorted(nums)
        left, right = 0, len(nums)-1
        while left < right and nums[left] == snums[left]:
            left += 1
        while left < right and nums[right] == snums[right]:
            right -= 1
        if left == right: return 0
        return right-left+1