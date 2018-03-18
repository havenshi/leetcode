# Time:  O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    #     return self.depth(root, layer=0)
    #
    # def depth(self, root, layer):
    #     if root == None:
    #         return layer
    #     layer += 1
    #     return max(self.depth(root.left, layer), self.depth(root.right, layer))