class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        count = 0
        flag = 0
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                flag += 1
                if flag >= 2:
                    continue
                else:
                    nums[count] = nums[i]
                    count += 1
            else:
                flag = 0
                nums[count] = nums[i]
                count += 1
        return count

        # if len(nums) <= 1:
        #     return nums
        # newnums = [nums[0]]
        # comp = nums[0]
        # count = 1
        # for item in nums[1:]:
        #     if item == comp:
        #         count += 1
        #         if count > 2:
        #             continue
        #         else:
        #             newnums.append(item)
        #     else:
        #         comp = item
        #         count = 1
        #         newnums.append(item)
        # return newnums

        # method 2
        # i = 0
        # for n in nums:
        #     if i < 2 or n > nums[i - 2]:
        #         nums[i] = n
        #         i += 1
        # return i
if __name__ == "__main__":
    answer=Solution()
    print answer.removeDuplicates([1,1,1,2,2,3])