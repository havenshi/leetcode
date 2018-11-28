class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = sum(nums)
        total = 0
        for x, n in enumerate(nums):
            if sums - n == 2 * total: return x
            total += n
        return -1