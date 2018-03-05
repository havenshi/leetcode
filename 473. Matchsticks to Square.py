# -*- coding: utf-8 -*-

import copy


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums) % 4: return False
        target = sum(nums) / 4
        if all([True if num <= target else False for num in nums]) == False:  # 检查是否有火柴大于边长
            return False

        # 不能用dp = [0] * (target+1), dp[0] = 1，因为如果每个数值很大，dp的column有很多很多，TLE
        # 尝试找出可能的若干个数的组合的sum
        dp = {each_dp: 0 for each_dp in self.dfs(nums, target)}
        dp[0] = 1

        newdp = dp
        for num in nums:
            dp = newdp  # 挪到loop最前面，因为后面要判断最后一次newdp的最后一位有无变动
            newdp = copy.deepcopy(dp)
            sort_dp = sorted(dp)
            for each_dp in sort_dp:
                if each_dp >= num:
                    newdp[each_dp] = newdp.get(each_dp, 0) + dp.get(each_dp - num, 0)  # 注意不能直接变动dp，要用newdp记录

        flag = (newdp.get(target, 0) != dp.get(target, 0))  # 如果最后一次newdp的最后一位变动了，说明最后的数字可以加进去
        return newdp.get(target, 0) >= 4 and flag  # 为啥不是==4，因为如果数字重复，但是组合还是可以有很多种

    def dfs(self, nums, target):
        target = sum(nums) / 4
        nums.sort()
        self.res = []
        for i in range(len(nums)):
            self.helper(nums[i + 1:], nums[i], target)
        return self.res  # 因为需要转化为hash，所以不用排序

    def helper(self, nums, total, target):
        if total <= target and total not in self.res:
            self.res.append(total)
        elif total > target:
            return

        if not nums:
            return

        for i in range(len(nums)):
            self.helper(nums[i + 1:], total + nums[i], target)


        # method 2 错误的
        # if sum(nums) % 4: return False
        # target = sum(nums) / 4
        # if all([True if num <= target else False for num in nums]) == False:  # 检查是否有火柴大于边长
        #     return False
        #
        # dp = [0] * (target + 1)
        # dp[0] = 1
        #
        # for num in nums:
        #     newdp = dp[:]
        #     for i in range(num, target + 1):
        #         newdp[i] += dp[i - num]  # 注意不能直接变动dp，要用newdp记录
        #     dp = newdp
        #     print dp
        # return dp[-1] >= 4  # 为啥不是==4，因为如果数字重复，但是组合还是可以有很多种

        # method 3 错误的
    #     nums = sorted(nums)[::-1]
    #     if len(nums) < 4:
    #         return False
    #     if sum(nums) % 4 != 0:
    #         return False
    #     side = sum(nums) / 4
    #     self.setside(nums, side)
    #     # for i in range(3):
    #     #     self.removeside(nums,side) # remove 3 sides
    #     #     print nums
    #     # if sum(nums) == side:
    #     #     return True
    #     # else:
    #     #     return False
    #
    # def setside(self,nums,side):
    #     n = len(nums)
    #     res = [[False for j in range(side + 1)] for i in range(n + 1)]
    #     for i in range(1, n + 1):
    #         for j in range(1, side + 1):
    #             res[i][j] = res[i - 1][j] # 1.copy the last line
    #             if j == nums[i - 1]:
    #                 res[i][j] = nums[i - 1] # 2.put single item in the right position
    #             if nums[i - 1] + res[i - 1][j - nums[i-1]] <= side:# 3.i-1 is current item of nums. [i-1] upper row, [j-nums[i-1]] the column which delete current item.
    #                 res[i][j] = nums[i-1] + res[i-1][j-nums[i-1]]
    #     return res
    #
    #             # if res[i][j] == side: # the first side appears, then stop
    #             #     while i >= 1 and j >= 0: # if greater than, remove item from nums list, if not, move to upper line
    #             #         if j >= nums[i - 1] and (res[i-1][j-nums[i-1]]+nums[i-1]) > res[i - 1][j]:
    #             #             j -= nums[i - 1]
    #             #             nums.remove(nums[i - 1])
    #             #         i -= 1

if __name__ == "__main__":
    answer=Solution()
    print answer.makesquare([1,1,2,2,2])


