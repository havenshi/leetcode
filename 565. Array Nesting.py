class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        self.memo = {}
        for i in range(len(nums)):
            res = max(res, self.dfs(nums, i, set(), res))
        return res

    def dfs(self, nums, i, visited, res):
        if i in self.memo:
            return self.memo[i]

        if nums[i] in visited:
            return max(res, len(visited))

        visited.add(nums[i])

        nextVisit = nums[i]
        res = self.dfs(nums, nextVisit, visited, res)
        self.memo[i] = res

        return res