def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = 0, len(nums) - 1
    if start == end:
        return start
    if start + 1 == end:
        return nums.index(max(nums[start], nums[end]))

    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            end = mid
        elif nums[mid] < nums[mid + 1]:
            start = mid
    print start,end
    return nums.index(max(nums[start], nums[end]))
print findPeakElement([2,1,2])