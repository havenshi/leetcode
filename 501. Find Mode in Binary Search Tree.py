# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        d = collections.Counter(self.inOrder(root))
        return [key for m in [max(d.values())] for key, val in d.items() if val == m]

    def inOrder(self, root):
        res = []
        q = []
        while root or q:
            if root:
                q.append(root)
                root = root.left
            elif q:
                root = q.pop()
                res.append(root.val)
                root = root.right
        return res
