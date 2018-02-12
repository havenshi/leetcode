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
    #     if not root: return 0
    #     left, right, val = root.left, root.right, root.val
    #     return max(self.longestPath(left, val) + self.longestPath(right, val), self.longestUnivaluePath(left),
    #                self.longestUnivaluePath(right))
    #
    # def longestPath(self, root, val):
    #     if not root or root.val != val: return 0
    #     return 1 + max(self.longestPath(root.left, val), self.longestPath(root.right, val))

        if not root: return 0
        self.ans = 0
        self.helper(root, root.val)
        return self.ans

    def helper(self, root, val):
        if not root: return 0
        cur = 1
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left, root.left.val)
            if root.left.val == val:
                left += 1
        if root.right:
            right = self.helper(root.right, root.right.val)
            if root.right.val == val:
                right += 1

        cur = max(1, left, right)

        self.ans = max(self.ans, cur - 1, left + right - 2, left - 1, right - 1)

        return cur