class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        index = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                # 常规的交换是可以的
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
                i += 1
        return index

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
        return j+1

if __name__ == "__main__":
    answer=Solution()
    print answer.removeElement([3,2,2,2,3],3)
