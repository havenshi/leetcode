class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low

        # slow = 0
        # fast = 0
        #
        # while True:
        #     slow = nums[slow]  # move 1 step
        #     fast = nums[nums[fast]]  # move 2 steps
        #
        #     if slow == fast:
        #         break
        #
        # # Start up another pointer from the end of the array and march it forward
        # # until it hits the pointer inside the array.
        # finder = 0
        # while True:
        #     slow = nums[slow]
        #     finder = nums[finder]
        #
        #     # If the two hit, the intersection index is the duplicate element.
        #     if slow == finder:
        #         return slow