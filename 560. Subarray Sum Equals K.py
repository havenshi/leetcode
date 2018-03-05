# O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary = {0: 1}  # 初始化，记录起点到i位置的sum以及出现的次数
        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res += dictionary.get((total - k), 0)  # 如果能找到sum-k，目前的位置又为sum，一定存在k
            dictionary[total] = dictionary.get(total, 0) + 1  # 注意之前可能已经有total的情况，所以dict的值需要加总

        return res

