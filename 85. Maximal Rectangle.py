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
            maxRec = max(maxRec, self.largestRectangleArea(a))  # 对于每行行程的矩形图，求最大面积
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