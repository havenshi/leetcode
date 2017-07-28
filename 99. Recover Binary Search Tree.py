# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        listi = []
        listp = []
        self.inorder(root, listi, listp)
        listi.sort()
        for i in range(len(listi)):
            listp[i].val = listi[i]

    def inorder(self, root, listi, listp):
        if root:
            self.inorder(root.left, listi, listp)
            listi.append(root.val)
            listp.append(root)
            self.inorder(root.right, listi, listp)