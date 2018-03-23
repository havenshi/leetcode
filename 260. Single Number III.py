class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 用异或方法找到a1^a2，它们一定有至少一位不同
        # 我们取出其中任意一位为‘1’的位，为了方便起见，我们用 a &= -a 来取出最右端为‘1’的位，
        # 然后和原数组中的数字挨个相与，根据该位是否为1分成两个不同的组

        n = len(nums)
        a = nums[0]
        for i in range(1, n):
            a ^= nums[i]

        a &= -a
        res = [0, 0]
        for i in range(n):
            if nums[i] & a:
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]

        return res