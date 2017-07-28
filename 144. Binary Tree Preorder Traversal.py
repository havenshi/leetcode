# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iteration_preorder(root)

    def iteration_preorder(self, root):
        stack = []
        res = []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res

    def recursion_preorder(self, root):
        if not root:
            return []
        return [root.val] + self.recursion_preorder(root.left) + self.recursion_preorder(root.right)