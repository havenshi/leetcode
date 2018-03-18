# -*- coding: utf-8 -*-
# Time:  O(k * n^k)
# 搜索的时间复杂度是O(解的个数 * 每个解生成的复杂度)
# 假设长度为n的数组全都是1，比如{1, 1, 1, 1,...}，target是k
# 那么一共有n^k个不同的解（假设每位的1都不同，则第一位可能有n种可能，第二位有n种可能，以此类推）
# 每种解的最大耗时为k（就是循环到底）
# 因此时间复杂度的upper bound情况是O(kn^k)
# Space: O(k)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    # method 1
        candidates.sort()
        Solution.res = []
        self.DFS(candidates, target, [])
        return Solution.res

    def DFS(self, candidates, target, valuelist):
        if target == 0:
            Solution.res.append(valuelist)
            return
        for i in range(len(candidates)):  # 从前往后遍历，可以模拟不需要前几位元素的情况
            if target < candidates[i]:  # recursion时，仍然从序列的第i位开始，因为每个元素可以重复使用
                return
            self.DFS(candidates[i:], target - candidates[i], valuelist + [candidates[i]])

    # method 2
    #     self.result = []
    #     candidates.sort()
    #     for i in range(len(candidates)):
    #         self.recursive_comb([candidates[i]], candidates[i:], target)
    #     return self.result
    #
    #
    # def recursive_comb(self, temp_array, rest_array, target):
    #     if sum(temp_array) == target:
    #         if temp_array not in self.result:
    #             self.result.append(temp_array)
    #     else:
    #         for i in range(len(rest_array)):
    #             temp_array2 = temp_array[:]
    #             temp_array2.append(rest_array[i])
    #             if sum(temp_array2) <= target:
    #                 self.recursive_comb(temp_array2, rest_array[i:], target)


if __name__ == "__main__":
    answer=Solution()
    print answer.combinationSum([2, 3, 6, 7], 7)
