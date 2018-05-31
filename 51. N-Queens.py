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





# 跟37Sudoku Solver一模一样的解法，但是好慢好慢。。。
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.'] * n for _ in range(n)]
        self.res = []
        self.helper(board, 0, n)
        return self.res

    def helper(self, board, row, n):
        if row == n:
            tmp = []
            for i in range(n):
                tmp.append(''.join(board[i]))
            self.res.append(tmp)
            return True

        flag = False
        for col in range(n):
            if board[row][col] == '.':
                board[row][col] = 'Q'
                if self.check(board, row, col, n) and self.helper(board, row + 1, n):
                    flag = True  # 此处不能直接return True，要把所有情况考虑进去
                board[row][col] = '.'
        return flag

    def check(self, board, row, col, n):
        for x in range(n):
            if (x != row and board[x][col] == 'Q') or (x != col and board[row][x] == 'Q'):
                return False
        for x in range(n):
            for y in range(n):
                if x != row and y != col and board[x][y] == 'Q' and abs(x - row) == abs(y - col):  # 检查对角线和逆对角线
                    return False
        return True




# 这个方法更快，Time:O(n^2)
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: #这三个array分别检查纵坐标，对角线和逆对角线。因为是每行每行dfs所以行肯定不同不用检查
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q]) # 只需记录每行Q的纵坐标
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]