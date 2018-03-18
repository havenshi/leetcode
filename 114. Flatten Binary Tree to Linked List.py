# Time:  O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 首先将左右子树分别平化为链表，这两条链表的顺序分别为左子树的先序遍历和右子树的先序遍历
        # 然后将左子树链表插入到根节点和右子树链表之间
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        p = root
        if not p.left:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None

        # if root == None:
        #     return
        # result = []
        # queue = [root]
        # while queue:
        #     node = queue.pop()
        #     result.append(node.val)
        #     if node.right:
        #         queue.append(node.right)
        #     if node.left:
        #         queue.append(node.left)
        #
        # pre = root
        # i = 1
        # while i < len(result):
        #     root.left = None
        #     root.right = TreeNode(result[i])
        #     root = root.right
        #     i += 1
        # root = pre

