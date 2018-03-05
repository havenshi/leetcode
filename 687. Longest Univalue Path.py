# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # method1，只有一个helper函数，还是很慢
    #     if not root: return 0
    #     left, right, val = root.left, root.right, root.val
    #     return max(self.longestPath(left, val) + self.longestPath(right, val), self.longestUnivaluePath(left),
    #                self.longestUnivaluePath(right))
    #
    # def longestPath(self, root, val): # 计算从root的，最长的半边路径长度
    #     if not root or root.val != val: return 0
    #     return 1 + max(self.longestPath(root.left, val), self.longestPath(root.right, val))

        # method2，好慢。。。
    #     if not root: return 0
    #     ans = self.helper(root, root.val) - 1
    #     ans = max(ans, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
    #     return ans
    #
    # def helper(self, root, val):  # 计算经过root的，所有值全部相同的路径长度
    #     if not root: return 0
    #     if root.val != val:
    #         return 0
    #     return 1 + self.helper2(root.left, val) + self.helper2(root.right, val)
    #
    # def helper2(self, root, val):  # 计算从root的，最长的半边路径长度
    #     if not root: return 0
    #     if root.val != val:
    #         return 0
    #     return 1 + max(self.helper2(root.left, val), self.helper2(root.right, val))

        # method3 加入了self.longest不断更新，稍快一点
        self.longest = 0
        self.longestPath(root)
        return self.longest

    def longestPath(self, root):  # 计算从root的，最长的半边路径的edge个数
        if not root:
            return 0
        left = self.longestPath(root.left)
        right = self.longestPath(root.right)
        leftMost = 0
        rightMost = 0
        if root.left and root.left.val == root.val:
            leftMost = left + 1
        if root.right and root.right.val == root.val:
            rightMost = right + 1
        self.longest = max(self.longest, leftMost + rightMost)
        return max(leftMost, rightMost)