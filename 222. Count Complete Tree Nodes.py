# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # method 1 recursion
        if not root: return 0
        countl, countr = 1, 1
        leftnode, rightnode = root, root
        while leftnode.left:
            countl += 1
            leftnode = leftnode.left
        while rightnode.right:
            countr += 1
            rightnode = rightnode.right
        if countl == countr:  # when most left height = most right height, # = height ^ 2 - 1
            return pow(2, countl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)  # number of left and right plus root

        # binary search
