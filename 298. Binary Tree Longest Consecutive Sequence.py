# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# For example,
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        self.longestConsecutiveHelper(root)
        return self.max_len

    def longestConsecutiveHelper(self, root):  # 从root开始的深度
        if not root:
            return 0

        left_len = self.longestConsecutiveHelper(root.left)  # 从左子树开始的深度
        right_len = self.longestConsecutiveHelper(root.right)  # 从右子树开始的深度

        cur_len = 1
        if root.left and root.left.val == root.val + 1:
            cur_len = max(cur_len, left_len + 1)
        if root.right and root.right.val == root.val + 1:
            cur_len = max(cur_len, right_len + 1)
        # cur_len为从root开始的最大深度

        self.max_len = max(self.max_len, cur_len, left_len, right_len)

        return cur_len