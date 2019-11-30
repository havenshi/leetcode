import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.Counter(nums)
        res = 0
        for x in d:
            if k > 0 and x + k in d or (k == 0 and d[x] > 1):
                res += 1
        return res
