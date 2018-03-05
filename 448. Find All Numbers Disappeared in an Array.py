class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将元素对应的位置标记，即如果访问过仄一直取负
        for num in nums:
            index = abs(num)-1
            nums[index] = -abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

        # method2 将元素交换至正确的位置
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            else:
                j = nums[i] - 1
                while nums[j] != j + 1 and nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j = nums[i] - 1
        return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]