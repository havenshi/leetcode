# Time:  O(n * 2^n)
# Space: O(1)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res = [[]]
        self.helper(nums, self.res, layer=0)
        return self.res

    def helper(self, nums, result, layer):
        if layer == len(nums):
            return
        tmp = result[:]
        for item in tmp:
            if (item + [nums[layer]]) not in result:
                result.append(item + [nums[layer]])
        self.helper(nums, result, layer + 1)

    #     nums.sort()
    #     total = [[]]
    #     for i in range(1, len(nums) + 1):
    #         total += self.subsets_each(nums, i)
    #     return total
    #
    # def subsets_each(self, array, target):
    #     self.result = []
    #     for i in range(len(array)):
    #         self.helper([array[i]], array[i + 1:], target)
    #     return self.result
    #
    # def helper(self, temp_array, rest_array, target):
    #     if len(temp_array) == target:
    #         if temp_array not in self.result:
    #             self.result.append(temp_array)
    #     else:
    #         for i in range(len(rest_array)):
    #             temp_array2 = temp_array[:]
    #             temp_array2.append(rest_array[i])
    #             self.helper(temp_array2, rest_array[i + 1:], target)

if __name__ == '__main__':
    print Solution().subsetsWithDup([1,2,2])