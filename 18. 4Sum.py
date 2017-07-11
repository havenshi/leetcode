class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                total = target-nums[i]-nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == total:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left]+nums[right] < total:
                        left += 1
                    else:
                        right -= 1
        return res

if __name__ == "__main__":
    answer=Solution()
    print answer.fourSum([1,1,-1,-1],0)
