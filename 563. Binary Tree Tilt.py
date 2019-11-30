# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diff = 0
        def getTotal(root):
            if not root:
                return 0
            left, right = getTotal(root.left), getTotal(root.right)
            self.diff += abs(left - right)
            return root.val + left + right
        getTotal(root)
        return self.diff
