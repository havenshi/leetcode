# Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
#
# Note:
#
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.
#
# 这道题是之前那道Maximum Average Subarray I的拓展，那道题说是要找长度为k的子数组的最大平均值，而这道题要找长度大于等于k的子数组的最大平均值。
# 加了个大于k的条件，那么情况就复杂很多了，之前只要遍历所有长度为k的子数组就行了，现在还要包括所有长度大于k的子数组。
# 我们首先来看brute force的方法，就是遍历所有的长度大于等于k的子数组，并计算平均值并更新结果res。那么我们先建立累加和数组sums，
# 结果res初始化为前k个数字的平均值，然后让i从k+1个数字开始遍历，那么此时的sums[i]就是前k+1个数组组成的子数组之和，
# 我们用其平均数来更新结果res，然后要做的就是从开头开始去掉数字，直到子数组剩余k个数字为止，然后用其平均值来更新解结果res，
# 通过这种方法，我们就遍历了所有长度大于等于k的子数组。这里需要注意的一点是，更新结果res的步骤不能写成res = min(res, t / (i + 1))
# 这种形式，会TLE，必须要在if中判断 t > res * (i + 1) 才能accept，写成t / (i + 1) > res 也不行，必须要用乘法，这也说明了计算机不喜欢算除法吧

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # method1, bruteforce, O(n2)
        # n = len(nums)
        # array = [0]*n
        # array[0] = nums[0]
        # res = 0
        # for i in range(1, k):
        #     array[i] = array[i-1]+nums[i]
        #     res = max(res, array[i]/(i+1))
        #
        # for i in range(k, n):
        #     array[i] = array[i - 1] + nums[i]
        #     for j in range(i-k+1):
        #         tmp = sums[i] -  sums[j]
        #         if (tmp > res * (i - j)):
        #             res = tmp / (i - j)
        #
        # return res


        # 这道题的思想就是二分猜测，首先需要预测的这个平均值肯定是介于最大值和最小值之间的，所以就以二分法的思想，不停的猜测就可以了，这个就是核心思想，进行二分法的需要操作log(max - min)次。
        #
        # 我们不停的猜测那个mid值（max和min的平均值）在给定的序列中能否满足，也就是说是否存在一个大于等于k的区间的平均值大于等于mid值，如果是，我们就可以把下限值min变成mid，反之改变max，就这样做，直到猜测范围小于0.00001

        #
        # 另外一个难点在于如何在线性的时间内，判别nums当中是否存在这样的一段，使得平均值大于等于mid。做法也很简单：
        # 顺序遍历数组nums（这里需要统一减去mid），统计两个值这里第一个值是sums，从位置0到当前位置j的和。另外一个是从0到某个位置i的和的最小值min_sum（其中i小于j，且i和j的长度大于等于k）。也就是等价于找一段和大于0的子区间，注意不是找最大，所以不用太严格。