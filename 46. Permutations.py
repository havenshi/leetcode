# Time:  O(n * n!)
# Space: O(n)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.recursive_comb([], nums, len(nums))
        return self.result

    def recursive_comb(self, temp_array, rest_array, target):
        if target == 0:
            self.result.append(temp_array)
            return
        for i in range(len(rest_array)):
            temp_array2 = temp_array[:]
            temp_array2.append(rest_array[i])
            self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target - 1)

        # method2 快一些
        # if len(nums) <= 1:
        #     return [nums]
        # res = []
        # for i,num in enumerate(nums):
        #     for y in self.permute(nums[:i]+nums[i+1:]):
        #         res.append([num]+y)
        # return res

if __name__ == "__main__":
    answer=Solution()
    print answer.permute([1,2,3])
