# -*- coding: utf-8 -*-
# Time:  O(1)
# Space: O(1)
'''
Flatten 2D Vector
=================
Implement an iterator to flatten a 2d vector.
For example,
Given 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,2,3,4,5,6].
'''

# 不直接转换为一维数组，而是维护两个变量x和y，我们将x和y初始化为0，对于hasNext函数，我们检查当前x是否小于总行数，
# y是否和当前行的列数相同，如果相同，说明要转到下一行，则x自增1，y初始化为0，若此时x还是小于总行数，说明下一个值可以被取出来，
# 那么在next函数就可以直接取出行为x，列为y的数字，并将y自增1
class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.vec2d = 0, 0, vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.col += 1
        return self.vec2d[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.vec2d) and \
                        self.col >= len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)


        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())


# 普通遍历
# Time:  O(n)
# Space: O(1)
# def zigzag(matrix):
#     m = len(matrix)
#     row, col = 0, 0
#     ans = []
#     while row < m:
#         while col < len(matrix[row]):
#             if col < len(matrix[row]):
#                 ans.append(matrix[row][col])
#             col += 1
#         col = 0
#         row += 1
#     return ans
#
# print zigzag([[1,2,3],
#                [4,5,6,7],
#                [8,9]])
# [1, 2, 3, 4, 5, 6]