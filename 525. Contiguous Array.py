class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        d = {0:-1}
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            if count in d:
                res = max(res, i-d[count])
            else:
                d[count] = i
        return res