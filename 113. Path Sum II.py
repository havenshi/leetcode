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
        _result = []
        self.dfs(root, _result, tmp=[], target=sum)
        return _result

    def dfs(self, node, result, tmp, target):
        tmp.append(node.val)
        if not node.left and not node.right:
            if sum(tmp) == target:
                result.append(tmp)

        if node.left:
            copytmp = tmp[:]
            self.dfs(node.left, result, copytmp, target)

        if node.right:
            copytmp = tmp[:]
            self.dfs(node.right, result, copytmp, target)


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