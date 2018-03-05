class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        if not nums:
            return []
        count = collections.Counter(nums)

        array = [[] for x in range(len(nums) + 1)]
        for key, val in count.items():
            array[val].append(key)

        return reduce((lambda x, y: x + y), [x for x in array[::-1] if x])[:k]