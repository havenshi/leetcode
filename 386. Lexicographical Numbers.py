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
            if y < n and y % 10 < 9:
                stack.append(y + 1)
            if y * 10 <= n:
                stack.append(y * 10)
        return result