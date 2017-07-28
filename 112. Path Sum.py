# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        result = []
        self.dfs(root, result, tmp=[])
        return sum in result

    def dfs(self, node, result, tmp):
        tmp.append(node.val)
        if not node.left and not node.right:
            result.append(sum(tmp))

        if node.left:
            copytmp = tmp[:]
            self.dfs(node.left, result, copytmp)

        if node.right:
            copytmp = tmp[:]
            self.dfs(node.right, result, copytmp)


    # method 2
    # def hasPathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: bool
    #     """
    #     if not root:
    #         return False
    #     nodes = [root]
    #     value = root.val
    #     return self.helper(nodes, value, sum)
    #
    # def helper(self, nodes, value, sum):
    #     node = nodes[-1]
    #     if value == sum and not node.left and not node.right:
    #         return True
    #     if node.left and self.helper(nodes + [node.left], value + node.left.val, sum):
    #         return True
    #     if node.right and self.helper(nodes + [node.right], value + node.right.val, sum):
    #         return True
    #     return False