# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
#
# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].
#
# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#
#           1
#          /
#         2
# 2. Now removing the leaf [2] would result in this tree:
#
#           1
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []
# Returns [4, 5, 3], [2], [1].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mp = {}
        maxLayer = self.dfs(root, mp)
        ans = []
        for i in range(maxLayer + 1):
            ans.append(mp[i])
        return ans

    def dfs(self, node, mp):
        if not node: return -1
        leftLayer, rightLayer = -1, -1
        if node.left:
            leftLayer = self.dfs(node.left, mp)
        if node.right:
            rightLayer = self.dfs(node.right, mp)
        curLayer = max(leftLayer, rightLayer) + 1
        if curLayer not in mp:
            mp[curLayer] = []
        mp[curLayer].append(node.val)
        return curLayer