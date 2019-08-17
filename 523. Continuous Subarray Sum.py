class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = 0
        visits = {0: -1}
        for i, num in enumerate(nums):
            total += num
            mod = total % k if k else total
            if mod not in visits:
                visits[mod] = i
            elif i - visits[mod] > 1: # subarray exist twice
                return True
        return False