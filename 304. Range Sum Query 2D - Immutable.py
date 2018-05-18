# Time:  ctor:   O(m * n),
#        lookup: O(1)
# Space: O(m * n)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m,n = len(matrix),len(matrix[0])
        self.mat = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            tmp = 0
            for j in range(n):
                if i == 0 and j == 0:
                    self.mat[i+1][j+1] = matrix[i][j]
                elif i == 0 and j != 0:
                    self.mat[i+1][j+1] = self.mat[i+1][j]+matrix[i][j]
                else:
                    self.mat[i+1][j+1] = self.mat[i][j+1]+matrix[i][j]+tmp
                tmp += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.mat[row2+1][col2+1] - self.mat[row1][col2+1] - self.mat[row2+1][col1] + self.mat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)