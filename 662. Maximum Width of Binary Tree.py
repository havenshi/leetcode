# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 1)]
        ans = 0
        while q:
            width = q[-1][-1] - q[0][-1] + 1
            ans = max(ans, width)
            q0 = []
            for n, i in q:
                if n.left: q0.append((n.left, i * 2))
                if n.right: q0.append((n.right, i * 2 + 1))
            q = q0
        return ans