# Time:  O(n * 2^n)
# Space: O(1)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # method1
        # res = [[]]
        # for num in nums:
        #     tmpr = res[:]
        #     for item in tmpr:
        #         newitem = item + [num]
        #         res.append(newitem)
        # return res

        # method2 bfs
        from collections import deque
        res = [[]]
        for num in nums:
            queue = deque(res[:])
            while queue:
                q = queue.popleft()
                newitem = q + [num]
                res.append(newitem)
        return res

        # method3 dfs
    #     nums.sort()
    #     self.res = []
    #     self.dfs(nums, [], 0)
    #     return self.res
    #
    # def dfs(self, nums, tmp, layer):
    #     if layer == len(nums):
    #         self.res.append(tmp)
    #         return
    #     self.dfs(nums, tmp + [nums[layer]], layer + 1)
    #     self.dfs(nums, tmp, layer + 1)

if __name__ == '__main__':
    print Solution().subsets([1,2,3])

    #     total = [[]]
    #     for i in range(1, len(nums) + 1):
    #         total += self.subsets_each(nums, i)
    #     return total
    #
    # def subsets_each(self, arry, n):
    #     result = []
    #     if n == 1:
    #         for i in range(len(arry)):
    #             result.append([arry[i]])
    #     else:
    #         for item in self.subsets_each(arry, n - 1):
    #             end = arry.index(item[-1])
    #             for i in arry[end + 1:]:
    #                 result.append(item + [i])
    #     return result

    # jiuzhang
    # def search(self, nums, S, index):
    #     if index == len(nums):
    #         self.results.append(S)
    #         return
    #
    #     self.search(nums, S + [nums[index]], index + 1)
    #     self.search(nums, S, index + 1)
    #
    # def subsets(self, nums):
    #     self.results = []
    #     self.search(sorted(nums), [], 0)
    #     return self.results