# -*- coding: utf-8 -*-
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) <= 1:
        #     return -1
        #
        #     # same as linked list cycle
        #     # the duplicate number must be the entry point of the circle when visiting the array from nums[0]
        # slow = nums[0]
        # fast = nums[nums[0]]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        # # when slow == fast, let slow be the nums[0]
        # slow = 0
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow

        # 用二分法先选取n/2，按照抽屉原理，整个数组中如果小于等于n/2的数的数量大于n/2，说明1到n/2这个区间是肯定有重复数字的。
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            print low,high,mid
            cnt = sum(x <= mid for x in nums)
            print cnt
            if cnt > mid: # 如果mid=2，且前所有数值中有超过一半的数为≤2，说明前半段有重复
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    answer=Solution()
    print answer.findDuplicate([0,2,1,3,1])