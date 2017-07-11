class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        i = 0
        while i < n:  # 桶排列，把所有元素(值为x)放在对应的x-1位上
            # 当x位置不对，也不等于应该在的x-1位上的另一个值，且不超过数列长度n且为正数。则交换，用while确保x在正确位置上。
            while nums[i] != i+1 and nums[i] <= n and nums[i] > 0 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
            i += 1
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1