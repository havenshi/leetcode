# Time:  O(n!)
# Space: O(n)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        array = [-1 for i in range(n)]
        self.res = []
        for i in range(n):
            self.dfs([i] + array[1:], 1)

        result = []
        for item in self.res:
            board = [['.'] * n for _ in range(n)]
            for i in range(n):
                board[i][item[i]] = 'Q'
            tmp = []
            for i in range(n):
                tmp.append(''.join(board[i]))
            result.append(tmp)
        return result

    def dfs(self, array, count):
        n = len(array)
        if count == n:
            self.res.append(array[:])
            return True
        flag = False
        for i in range(n):
            array[count] = i
            if self.isValid(array, i, count) and self.dfs(array, count + 1):
                flag = True
                # set 'flag value' rather than return True directly. Or if several i satisfy, 'for' loop  will end at the first time of True. It can miss some possibility.
            array[count] = -1
        return flag

    def isValid(self, array, x, count):
        for i in range(count):
            if array[i] == x or abs(count - i) == abs(x - array[i]):
                return False
        return True

if __name__ == "__main__":
    print Solution().solveNQueens(4)

