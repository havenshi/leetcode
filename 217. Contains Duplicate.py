class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashing = {}
        for i in nums:
            if i not in hashing:
                hashing[i] = 1
            else:
                return True
        return False