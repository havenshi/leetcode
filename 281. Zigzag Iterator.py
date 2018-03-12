# -*- coding: utf-8 -*-
# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# For example, given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:
#
# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].

# Time:  O(n)
# Space: O(k)

import collections
class ZigzagIterator(object):
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.vec2d = 0, 0, vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.row += 1
        return self.vec2d[self.row - 1][self.col]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.col < len(self.vec2d[self.row]) and self.row >= len(self.vec2d):
            self.row, self.col = 0, self.col + 1
        return self.col < len(self.vec2d[self.row])

    # def __init__(self, v1, v2):
    #     """
    #     Initialize your q structure here.
    #     :type v1: List[int]
    #     :type v2: List[int]
    #     """
    #     self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])
    #
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     len, iter = self.q.popleft()
    #     if len > 1:
    #         self.q.append((len-1, iter))
    #     return next(iter)
    #
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     return bool(self.q)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


# 普通的遍历
def zigzag(matrix):
    m = len(matrix)
    n = max(len(row) for row in matrix)
    row, col = 0, 0
    step = 1
    ans = []
    while col < n:
        while 0 <= row < m:
            if col < len(matrix[row]):
                ans.append(matrix[row][col])
            row += step
        step *= (-1)
        row += step
        col += 1
    return ans

print zigzag([[1,2,3],
               [4,5,6,7],
               [8,9]])