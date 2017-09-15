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

    def FindTwoNodes(self, root):
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None: self.n1 = self.prev
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