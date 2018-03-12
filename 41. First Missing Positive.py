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


        # swap, 自己的方法，较慢

        n = len(nums)
        if not n:
            return 1
        great = max(nums)
        small = min(nums)
        array = [None] * (great - small + 1)
        array[:n] = nums
        dictionary = {}
        for i, v in enumerate(nums):
            dictionary[v] = i
        for i in range(len(array)):
            if array[i] != i + small:  # 通过swap把value都放在正确的位置上
                if i + small in dictionary:  # correct value is in nums; if None, pass
                    correct_ind = dictionary[i + small]
                    dictionary[array[i]] = correct_ind
                    array[i], array[correct_ind] = i + small, array[i]

        if array[0] > 1:
            return 1
        for i in range(1, len(array)):
            if array[i] == None or array[i] != i + small:  # None or 重复的情况，重复则肯定value跟position有一组对不上
                if i + small >= 1:
                    return i + small
        return array[-1] + 1