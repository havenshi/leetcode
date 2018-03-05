# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None
        if root == p or root == q: # p or q is root
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: # find p, q in the same layer
            return root
        if left != None:
            return left
        if right != None:
            return right


        # method2 不知为何不对。。。
# import copy
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution(object):
#     def dfs(self, stack, node, target):
#         if stack[-1].val == target.val:
#             self.path = stack
#             return
#         if node.left:
#             copystack = copy.deepcopy(stack)
#             copystack.append(node.left)
#             self.dfs(copystack, node.left, target)
#         if node.right:
#             copystack = copy.deepcopy(stack)
#             copystack.append(node.right)
#             self.dfs(copystack, node.right, target)
#
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if root == None:
#             return None
#
#         self.path = None
#         node = copy.deepcopy(root)
#         self.dfs([node], node, p)
#         path1 = self.path[:]
#
#         self.path = None
#         node = copy.deepcopy(root)
#         self.dfs([node], node, q)
#         path2 = self.path[:]
#
#         length = min(len(path1), len(path2))
#         i = 0
#         while True:
#             if path1[i] != path2[i] or i == length:
#                 return path1[i - 1]
#             else:
#                 i += 1