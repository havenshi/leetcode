class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1



if __name__ == "__main__":
    answer=Solution()
    print answer.search([15,16,19,20,25,1,3,4,5,7,10,14],25)