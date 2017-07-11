class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        count = 0
        for i in range(0, len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            else:
                nums[count] = nums[i]
                count += 1
        return count

        # 注意要把nums也改了，如[1,1,2,3]->[1,2,3,3]
        # if len(nums) <= 1:
        #     return 0 if len(nums) == 0 else 1
        # count = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[count] = nums[i] #有效的数放入nums前面部分，因为初始count已经为1，所以在count+1之前放。
        #         count += 1
        # return count

if __name__ == "__main__":
    answer=Solution()
    print answer.removeDuplicates([1,1,2])
