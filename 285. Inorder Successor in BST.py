# -*- coding: utf-8 -*-
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor in the tree, return null.


# Inorder Successor is the leftmost element in the right subtree of 'a'

# Time:  O(h)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # If it has right subtree. 1、如果这个节点p有右孩子，那么p的后续节点为右子树的的最左值（即最后一个没有左孩子的节点）
        if p and p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # Search from root. 2、如果节点p没有右孩子，那就在二叉搜索树中搜索节点p，并在从上往下的查找过程中依次更新记录比p的val值大的节点。
        successor = None
        while root and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

