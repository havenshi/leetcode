class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1

            # same as linked list cycle
            # the duplicate number must be the entry point of the circle when visiting the array from nums[0]
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # when slow == fast, let slow be the nums[0]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # low, high = 1, len(nums) - 1
        # while low <= high:
        #     mid = (low + high) >> 1
        #     cnt = sum(x <= mid for x in nums)
        #     if cnt > mid:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return low
