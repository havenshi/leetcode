class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        array = []
        for num in nums:
            if not array or num > array[-1][-1] + 1:
                array.append([num])
            else:
                array[-1][1:] = num,

        return ['->'.join(map(str, x)) for x in array]