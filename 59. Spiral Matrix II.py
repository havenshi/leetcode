class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n == 0: return res
        l = [i for i in range(1, n ** 2 + 1)]
        res = [[0 for j in range(n)] for i in range(n)]
        up, left = 0, 0
        bottom, right = n - 1, n - 1
        index = 0
        while index < n ** 2:
            for j in range(left, right + 1):
                res[up][j] = l[index]
                index += 1
            up += 1

            for i in range(up, bottom + 1):
                res[i][right] = l[index]
                index += 1
            right -= 1

            for j in range(right, left - 1, -1):
                res[bottom][j] = l[index]
                index += 1
            bottom -= 1

            for i in range(bottom, up - 1, -1):
                res[i][left] = l[index]
                index += 1
            left += 1
        return res



        begin = 0
        nn=n*n
        nums=[]
        for i in range(nn,0,-1):
            nums.append(i)          # create a num list to use
        matrix=[[0 for x in range(n)] for y in range(n)]     # create an empty matrix. Attention! Don't use [[0]*n]*n!

        if n==0:
            return []
        else:
            return self.rotate(matrix,begin,n-1,nums)                     #-------|
                                                                          #|       |
    def rotate(self,cube,start,end,numslist):  # traversal each peering   #|-------|
                                               # base state
        if start<=end:       # don't forget this condition!
            if start==end:   # if the central is remain
                cube[start][start] = numslist.pop()
            else:
                for y in range(start,end+1):       # if last row, traversal the column
                    cube[start][y]=numslist.pop()
                for x in range(start+1,end+1):     # if 2nd column, traversal the row
                    cube[x][end]=numslist.pop()
                for y in range(end-1,start-1,-1):  # if 3rd row, traversal the column
                    cube[end][y]=numslist.pop()
                for x in range(end-1,start+1-1,-1):# if 4th column, traversal the row
                    cube[x][start]=numslist.pop()
                self.rotate(cube, start+1, end-1, numslist)  # peering next inside layer

        return cube


        # if n == 0: return []
        # matrix = [[0]*n for _ in range(n)]
        # up = 0
        # down = len(matrix)-1
        # left = 0
        # right = len(matrix[0])-1
        # direct = 0  # 0: go right   1: go down  2: go left  3: go up
        # count = 0
        # while True:
        #     if direct == 0:
        #         for i in range(left, right+1):
        #             count += 1
        #             matrix[up][i] = count
        #         up += 1
        #     if direct == 1:
        #         for i in range(up, down+1):
        #             count += 1
        #             matrix[i][right] = count
        #         right -= 1
        #     if direct == 2:
        #         for i in range(right, left-1, -1):
        #             count += 1
        #             matrix[down][i] = count
        #         down -= 1
        #     if direct == 3:
        #         for i in range(down, up-1, -1):
        #             count += 1
        #             matrix[i][left] = count
        #         left += 1
        #     if count == n*n: return matrix
        #     direct = (direct+1) % 4

if __name__ == "__main__":
    answer=Solution()
    print answer.generateMatrix(3)
