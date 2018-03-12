class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = max(nums)
        return nums.index(maxnum) if all([maxnum>=2*num for num in nums if num !=maxnum]) else -1