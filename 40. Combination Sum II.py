# -*- coding: utf-8 -*-
# Time:  O(k * C(n, k))
# Space: O(k)
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if valuelist not in Solution.res:  # 排除元素重复的情况
                Solution.res.append(valuelist)
            return
        for i in range(len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates[i+1:], target - candidates[i], valuelist + [candidates[i]])


    # method 2
    #     self.result = []
    #     candidates.sort()
    #     for i in range(len(candidates)):
    #         self.recursive_comb([candidates[i]], candidates[i + 1:], target)
    #     return self.result
    #
    #
    # def recursive_comb(self,temp_array, rest_array, target):
    #     if sum(temp_array) == target:
    #         if temp_array not in self.result:
    #             self.result.append(temp_array)
    #     else:
    #         for i in range(len(rest_array)):
    #             temp_array2 = temp_array[:]
    #             temp_array2.append(rest_array[i])
    #             if sum(temp_array2) <= target:
    #                 self.recursive_comb(temp_array2, rest_array[i + 1:], target)

if __name__ == "__main__":
    answer=Solution()
    print answer.combinationSum2([10,1,2,7,6,1,5], 8)
