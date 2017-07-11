class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [-1 for i in range(n)]
        self.res = 0
        for i in range(n):
            self.dfs([i] + array[1:], 1)
        return self.res

    def dfs(self, array, count):
        n = len(array)
        if count == n:
            self.res += 1
            return
        for i in range(n):
            copyarray = array[:count] + [i] + array[count + 1:]
            if self.isValid(copyarray, i, count):
                self.dfs(copyarray, count + 1)

    def isValid(self, array, x, count):
        for i in range(count):
            if array[i] == x or abs(count - i) == abs(x - array[i]):
                return False
        return True