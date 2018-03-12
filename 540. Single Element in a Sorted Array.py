class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash O(n)+空间，位操作O(n)
        # 奇偶二分
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n-1
        while l + 1 < r:
            mid = l + (r-l)/2
            count = mid+1

            if count%2:
                if nums[mid]==nums[mid+1]: # 可能mid把a和a截断，但single数还是应该在右边段
                    l = mid
                else:
                    r = mid
            else:
                if nums[mid]==nums[mid+1]:
                    r = mid
                else:
                    l = mid

        return nums[l] if nums.count(nums[l])==1 else nums[r]