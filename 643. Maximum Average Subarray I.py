class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if k > n:
            return 0
        total = sum(nums[:k])
        res = sum(nums[:k])
        for i in range(1, n-k+1):
            total = total-nums[i-1]+nums[i+k-1]
            res = max(res, total)
        return res*100/(k*100.00)