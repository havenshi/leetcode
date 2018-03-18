# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 栈内保留递增的序列
        n = len(heights)
        maxArea = 0
        stackHeight = []
        stackIndex = []
        for i in range(n):
            if stackHeight == [] or heights[i] >= stackHeight[-1]: # 比左边的值大则入栈
                stackHeight.append(heights[i])
                stackIndex.append(i)
            elif heights[i] < stackHeight[-1]:# 比左边的值小则把站内所有较大的数都pop出
                lastIndex = 0
                while stackHeight and heights[i] < stackHeight[-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i - lastIndex) # 并且把较大的数至i位之前组成的area算出来
                    maxArea = max(maxArea, tempArea)
                stackHeight.append(heights[i]) # 入栈
                stackIndex.append(lastIndex) # 注意！是lastIndex而非i入栈，因为较小的数入栈时，长度要算上之前所有比它大的数的index，这样距离才正确
        while stackHeight: # 此时剩下的是自左向右变高的数列
            tempArea = stackHeight.pop() * (len(heights) - stackIndex.pop())
            maxArea = max(maxArea, tempArea)
        return maxArea

if __name__ == "__main__":
    answer=Solution()
    print answer.largestRectangleArea([2,1,5,6,6,2,3])