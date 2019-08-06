# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.tvsTree = []
        self.dfs(root, 0)
        return [max(t) for t in self.tvsTree]

    def dfs(self, root, depth):
        if not root:
            return
        if depth >= len(self.tvsTree):
            self.tvsTree.append([])
        self.tvsTree[depth].append(root.val)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)