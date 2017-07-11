class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.result = []
        nums.sort()
        for item in list(set(nums)):
            i = nums.index(item)
            length = len(nums)
            self.recursive_comb([nums[i]], nums[:i] + nums[i + 1:], length)
        return self.result

    def recursive_comb(self, temp_array, rest_array, target):
        if len(temp_array) == target:
            if temp_array not in self.result:
                self.result.append(temp_array)
        else:
            for item in list(set(rest_array)):
                i = rest_array.index(item)
                temp_array2 = temp_array[:]
                temp_array2.append(rest_array[i])
                self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target)

        # length = len(num)
        # if length == 0: return []
        # if length == 1: return [num]
        # num.sort()
        # res = []
        # previousNum = None
        # for i in range(length):
        #     if num[i] == previousNum: continue
        #     previousNum = num[i]
        #     for j in self.permuteUnique(num[:i] + num[i+1:]):
        #         res.append([num[i]] + j)
        # return res

if __name__ == "__main__":
    answer=Solution()
    print answer.permute([1,2])
