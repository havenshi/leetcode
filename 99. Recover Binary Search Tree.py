# Time:  O(n)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    # 只有一组逆序，如124356的43，把p=3，q=4，那么最后交换p和q即可。
    # 如果有两个逆序，如163452的63和52，当我们发现第一个逆序63时，令p=6，q=3，然后发现第二个逆序52时，令q=2，最后交换p和q。
    def FindTwoNodes(self, root):
        if not root:
            return
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                if self.n1 == None: # 第一组逆序的时候，更改n1值
                    self.n1 = self.prev
                self.n2 = root # 只要有逆序，更改n2值
            self.prev = root
            self.FindTwoNodes(root.right)

    # method 2 O(n) space
    #     listi = [] # 存储被破坏的二叉查找树的节点值
    #     listp = [] # 存储二叉查找树的节点的指针
    #     # 将list排序，再使用listp里面存储的节点指针赋值
    #     self.inorder(root, listi, listp)
    #     listi.sort()
    #     for i in range(len(listi)):
    #         listp[i].val = listi[i]
    #
    # def inorder(self, root, listi, listp):
    #     if root:
    #         self.inorder(root.left, listi, listp)
    #         listi.append(root.val)
    #         listp.append(root)
    #         self.inorder(root.right, listi, listp)