class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        stack = [1]
        while stack:
            y = stack.pop()
            result.append(y)
            if y + 1 <= n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n:
                stack.append(y * 10)
        return result

        # dfs
    #     self.res = []
    #     self.dfs(1, n)
    #     return self.res
    #
    # def dfs(self, i, n):
    #     if i > n:
    #         return
    #     self.res.append(i)
    #
    #     self.dfs(i * 10, n)
    #     if i % 10 != 9:
    #         self.dfs(i + 1, n)
