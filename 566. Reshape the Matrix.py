class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        flt = []
        for num in nums:
            flt.extend(num)

        res = [[0] * c for _ in range(r)]
        for i in range(c * r):
            res[i / c][i % c] = flt[i]
        return res
