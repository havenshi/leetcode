"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, 1)

    def dfs(self, root, tmp):
        if not root:
            return tmp
        clength = tmp  # max of root and all children
        for c in root.children:
            clength = max(clength, self.dfs(c, tmp + 1))
        return clength
