# Time:  O(n)
# Space: O(h), h is height of binary tree
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


    # method 2 更快一些
    #     if root == None:
    #         return False
    #     return self.dfs(root, root.val, sum)
    #
    # def dfs(self, root, tmp, sum):
    #     if tmp == sum and not root.left and not root.right:
    #         return True
    #     if not root:
    #         return False
    #     if root.left:
    #         if self.dfs(root.left, tmp+root.left.val, sum):
    #             return True
    #     if root.right:
    #         if self.dfs(root.right, tmp+root.right.val, sum):
    #             return True
    #     return False