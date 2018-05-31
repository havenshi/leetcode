class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]  # false * rownum
        col = [False for i in range(colnum)]  # false * colnum
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:   # set true to the corresponding row, col position.
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

if __name__ == "__main__":
    answer=Solution()
    print answer.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])


# 这题如果直接一次遍历，就会出现一个0的周围1->0，然后下次遍历到这个新形成的0又会改变它周围的，之际上不用变。
# 可以把新形成的0标记为2这样避免错误的变化。最后再重新遍历整个矩阵2->0。