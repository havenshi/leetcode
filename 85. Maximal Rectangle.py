# Time:  O(n^2)
# Space: O(n)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        a = [0 for _ in range(n)]
        maxRec = 0
        for i in range(m):  # 遍历每一行，如果某列的底数为1，仄将该列值累加1转化为矩形
            for j in range(n):
                if matrix[i][j] == '1':
                    a[j] += 1
                else:
                    a[j] = 0
            maxRec = max(maxRec, self.largestRectangleArea(a))  # 对于每行行程的矩形图，求最大面积，就是84题
        return maxRec

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        maxArea = 0
        stackHeight = []
        stackIndex = []
        for i in range(n):
            if stackHeight == [] or heights[i] >= stackHeight[-1]:  # 比左边的值大则入栈
                stackHeight.append(heights[i])
                stackIndex.append(i)
            elif heights[i] < stackHeight[-1]:  # 比左边的值小则把站内所有较大的数都pop出
                lastIndex = 0
                while stackHeight and heights[i] < stackHeight[-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i - lastIndex)  # 并且把较大的数至i位之前组成的area算出来
                    maxArea = max(maxArea, tempArea)
                stackHeight.append(heights[i])  # 入栈
                stackIndex.append(lastIndex)  # 注意！是lastIndex而非i入栈，因为较小的数入栈时，长度要算上之前所有比它大的数的index，这样距离才正确
        while stackHeight:  # 此时剩下的是自左向右变高的数列
            tempArea = stackHeight.pop() * (len(heights) - stackIndex.pop())
            maxArea = max(maxArea, tempArea)
        return maxArea


        # dp
        if not matrix:
            return 0

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in xrange(n)]
        H = [0 for _ in xrange(n)]
        R = [n for _ in xrange(n)]

        for i in xrange(m):
            left = 0
            for j in xrange(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1

            right = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j

        return result


        # method3 自己的dp方法 有点慢。。。
        # 用三个dp矩阵，分别存储一直到左边、上边的最长长条和以该点为右下角的rectangle

        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        matrix = [[int(x) for x in row] for row in matrix]

        dp_hor = [[0] * n for x in range(m)]
        for i in range(m):
            dp_hor[i][0] = matrix[i][0]
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp_hor[i][j] = dp_hor[i][j - 1] + 1

        dp_ver = [[0] * n for x in range(m)]
        for j in range(n):
            dp_ver[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    dp_ver[i][j] = dp_ver[i - 1][j] + 1

        dp = [[0] * n for x in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if m == 0:
                        dp[0][j] = [dp_hor[0][j], 1]
                    elif n == 0:
                        dp[i][0] = [1, dp_ver[i][0]]
                    else:
                        tmp = 1
                        dp[i][j] = [1, 1]
                        if dp[i - 1][j - 1] and dp_hor[i][j] and dp_ver[i][j]:
                            # rectangle的情况下肯定好些
                            tmpv = min(dp_hor[i][j], dp[i - 1][j - 1][0] + 1)
                            tmph = min(dp_ver[i][j], dp[i - 1][j - 1][1] + 1)
                            tmp = tmpv * tmph
                            dp[i][j] = [tmpv, tmph]
                        if dp_hor[i][j] > tmp:
                            tmp = dp_hor[i][j]
                            dp[i][j] = [dp_hor[i][j], 1]
                        if dp_ver[i][j] > tmp:
                            tmp = dp_ver[i][j]
                            dp[i][j] = [1, dp_ver[i][j]]
                        res = max(res, tmp)
        return res