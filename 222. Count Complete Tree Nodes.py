# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # method 1 recursion
        # Time:  O(n)
        # Space: O(1)
        if not root: return 0
        countl, countr = 1, 1
        leftnode, rightnode = root, root
        while leftnode.left:
            countl += 1
            leftnode = leftnode.left
        while rightnode.right:
            countr += 1
            rightnode = rightnode.right
        if countl == countr:  # when most left height = most right height, # = height ^ 2 - 1
            return pow(2, countl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)  # number of left and right plus root

        # binary search
        # 高度为h的完全二叉树，其节点个数等于高度为h - 1的满二叉树的节点个数 + 最后一层的节点个数。
        # 因此，只需要二分枚举第h层的节点个数即可。
        # 如四层高的二叉树，第四层编号为000 001 010 011 100 101 110 111,0和1分别代表left和right。
        # 即不断二分查找mid并转成二进制数字，按照该二进制数字的指令从root开始往下查找，查到了就left=mid+1，查的时候中间断了就right=mid-1
        # 二分法查找的时间复杂度为O(log(2^h))=O(hlog2)，但为了到达底层，中间需要经过最大h层节点，这样相当于O(h^2)的时间复杂度，即O(logn*logn)