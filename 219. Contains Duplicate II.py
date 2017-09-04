class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashing = {}
        for i,v in enumerate(nums):
            if v in hashing and abs(i - hashing[v]) <= k:
                return True
            hashing[v] = i
        return False