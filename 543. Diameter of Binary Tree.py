# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.depth(root.left)+self.depth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))