# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dictionary = {}
        return self.withroot(root)

    def withroot(self, root):  # 一定通过root点。注意不要withroot和withoutroot两个方法互相调用，会出错。
        if not root:
            return 0

        if root in self.dictionary:
            return self.dictionary[root]

        res1 = root.val  # 含root的情况
        if root.left:
            res1 += self.withroot(root.left.left) + self.withroot(root.left.right)
        if root.right:
            res1 += self.withroot(root.right.left) + self.withroot(root.right.right)

        res2 = self.withroot(root.left) + self.withroot(root.right)  # 不含root的情况

        self.dictionary[root] = max(res1, res2) # 为什么max加在helper函数里比较好？因为这样可以保证如果不含root，left+right的最大值情况依然不含left或right，超过1个house未被打劫

        return max(res1, res2)