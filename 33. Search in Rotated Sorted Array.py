class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid =  left + (right-left)/2
            if target == nums[mid]: return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if target == nums[left]: return left
        if target == nums[right]: return right
        return -1


if __name__ == "__main__":
    answer=Solution()
    print answer.search([15,16,19,20,25,1,3,4,5,7,10,14],25)