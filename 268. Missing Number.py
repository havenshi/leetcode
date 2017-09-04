class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1 bit map
        n = len(nums)
        res = 0
        for i in range(len(nums)):
            res ^= nums[i] ^ (i+1)
        return res

        # method 2 binary search
        nums.sort()
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == mid:
                left = mid
            else:
                right = mid
        if nums[left] == left and nums[right] == right:
            return nums[right] + 1
        elif nums[left] == left:
            return nums[right] - 1
        else:
            return nums[left] - 1

        # nums.sort()
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = left + (right - left) / 2
        #     if nums[mid] > mid:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return right + 1 if nums[right] == right else right