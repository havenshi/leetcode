# -*- coding:utf8 -*-
# 基数排序
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        count = 0
        maxnum = max(nums)
        while maxnum > 0:
            count += 1
            maxnum /= 10
        for k in range(count): # 最大数有多少位就有多少轮
            s = [[] for _ in range(10)]
            for i in nums:
                s[i / (10 ** k) % 10].append(i) # 在第k位的数字是多少，放到对应的桶中
                # 第一轮对个位桶排序[[], [], [], [3], [], [5, 15], [], [], [8], [9]]
                # 第二轮对十位桶排序[[3, 5, 8, 9], [15], [], [], [], [], [], [], [], []]
            nums = [item for line in s for item in line] # s矩阵中的数字遍历一遍，根据k位大小逐渐排序
        start = 0
        end = 1
        gap = nums[end] - nums[start]
        while end < n:
            gap = max(gap, nums[end] - nums[start])
            start += 1
            end += 1
        return gap
if __name__ == "__main__":
    print Solution().maximumGap([5,9,8,3,15])