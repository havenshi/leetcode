# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.res = []
        self.dfs(root, tmp=[], target=sum)
        return self.res

    def dfs(self, root, tmp, target):
        if not root:
            return

        newtmp = tmp[:]
        newtmp.append(root.val)
        if sum(newtmp) == target and not root.left and not root.right:
            self.res.append(newtmp)
        self.dfs(root.left, newtmp, target)
        self.dfs(root.right, newtmp, target)


    # method 2
    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: List[List[int]]
    #     """
    #     if not root:
    #         return []
    #     self.result = []
    #     nodes = [root]
    #     value = root.val
    #     self.helper(nodes, value, sum)
    #     return self.result
    #
    # def helper(self, nodes, value, sum):
    #     node = nodes[-1]
    #     if value == sum and not node.left and not node.right:
    #         self.result.append(nodes)
    #     if node.left:
    #         self.helper(nodes + [node.left], value + node.left.val, sum)
    #     if node.right:
    #         self.helper(nodes + [node.right], value + node.right.val, sum)