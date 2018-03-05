class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        self.recursive_comb([], nums, len(nums))
        return self.res

    def recursive_comb(self, temp_array, rest_array, target):
        if target == 0:
            if temp_array not in self.res:
                self.res.append(temp_array)
        else:
            for item in list(set(rest_array)):
                i = rest_array.index(item)
                temp_array2 = temp_array[:]
                temp_array2.append(rest_array[i])
                self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target - 1)

        # length = len(num)
        # if length <= 1: return [num]
        # num.sort()
        # res = []
        # previousNum = None
        # for i in range(length):
        #     if num[i] == previousNum: continue
        #     for j in self.permuteUnique(num[:i] + num[i+1:]):
        #         res.append([num[i]] + j)
        #     previousNum = num[i]
        # return res

if __name__ == "__main__":
    answer=Solution()
    print answer.permute([1,2])
