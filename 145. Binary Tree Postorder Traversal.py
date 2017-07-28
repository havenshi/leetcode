# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iteration_postorder(root)

    def iteration_postorder(self, root):
        stack = []
        res = []
        while root or stack:
            if root:
                res.insert(0, root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return res

    def recursion_postorder(self, root):
        if not root:
            return []
        return self.recursion_postorder(root.left) + self.recursion_postorder(root.right) + [root.val]