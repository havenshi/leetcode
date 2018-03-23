# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# For example:
# Given binary tree,
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# return 4.

# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    # 对于当前遍历到的节点，如果对其左右子节点分别递归调用函数，返回均为true的话，那么说明当前节点的值和左右子树的值都相同，
    # 那么又多了一棵树，所以结果自增1，然后返回当前节点值和给定值(其父节点值)是否相同，从而回归上一层递归调用
    def countUnivalSubtrees(self, root):
        self.res = 0
        self.dfs(root, -1)
        return self.res

    def dfs(self, root, val):
        if not root:
            return True
        if not self.dfs(root.left, root.val) or not self.dfs(root.right, root.val):
            return False
        else:
            self.res += 1
            return root.val == val