# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # （左子树中的最大路径和，右子树中的最大路径和，
        # 以及左子树中以root.left为起点的最大路径（需要大于零）+右子树中以root.right为起点的最大路径（需要大于零）+root.val），
        # 这三者中的最大值就是最大的路径和

        if root == None:
            return 0
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if root == None:
            return 0
        tmp = root.val
        lmax = 0
        rmax = 0
        if root.left:
            lmax = self.helper(root.left)
            if lmax > 0:
                tmp += lmax
        if root.right:
            rmax = self.helper(root.right)
            if rmax > 0:
                tmp += rmax
        self.res = max(tmp, self.res)
        return max(root.val, root.val + lmax, root.val + rmax)
