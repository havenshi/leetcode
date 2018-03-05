# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        if s.val == t.val:
            if self.same(s.left, t.left) and self.same(s.right, t.right):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def same(self, a, b):
        if not a and not b:
            return True
        elif not a:
            return False
        elif not b:
            return False
        return a.val == b.val and self.same(a.left, b.left) and self.same(a.right, b.right)