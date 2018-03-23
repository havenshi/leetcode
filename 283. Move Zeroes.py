# Time:  O(n)
# Space: O(1)
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    # if len(nums) == 1:
    #     return
    # left = 0
    # while left < len(nums):
    #     if nums[left] != 0:
    #         left += 1
    #         continue
    #     right = left + 1
    #     while right < len(nums):
    #         if nums[right] != 0:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             break
    #         right += 1
    #     left += 1
    # return nums

print moveZeroes([1,0])