class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return
        if k == 1:
            return [[n]]
        array = [x for x in range(1, 10)]
        self.res = []
        for i in range(len(array)):
            if (array[i] + array[i] + (k - 1)) * k / 2 <= n:
                self.dfs([array[i]], array[i + 1:], k, n)
        return self.res

    def dfs(self, before, after, num, target):
        if sum(before) == target and len(before) == num:
            self.res.append(before)
            return
        if sum(before) < target and len(before) < num:
            for i in range(len(after)):
                self.dfs(before + [after[i]], after[i + 1:], num, target)