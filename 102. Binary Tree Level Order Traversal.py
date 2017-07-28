import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = [root]
        while q:
            newq = []
            newr = []
            for node in q:
                newr.append(node.val)
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            res.append(newr)
            q = newq
        return res