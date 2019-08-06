class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s = {n: i for i, n in enumerate(sorted(nums, reverse=True))}
        medals = ['Gold', 'Silver', 'Bronze']
        return [str(s[n]+1) if s[n] >= 3 else (medals[s[n]] + ' Medal') for n in nums]