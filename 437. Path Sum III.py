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
        :rtype: int
        """
        if not root:
            return 0
        res = self.helper(root, sum)  # 包含root
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

    def helper(self, root, sum):  # 必须以该root为起点，是连续的
        if not root:
            return 0

        ans = 0
        if root.val == sum:
            ans += 1
        ans += self.helper(root.left, sum - root.val)
        ans += self.helper(root.right, sum - root.val)

        return ans