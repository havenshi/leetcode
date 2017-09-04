class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                return i
        return i

        # binary search
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        elif nums[right] < target:
            return right + 1
        elif nums[left] < target:
            return right
        else:
            return left
if __name__ == "__main__":
    answer=Solution()
    print answer.searchInsert([1,3,5,6], 7)
