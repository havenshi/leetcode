# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 右>中>左遍历，赋新值
        stack= []
        value = 0
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += value
                value = cur.val
                cur = cur.left
        return root

        # too slow
    #     if not root:
    #         return None
    #
    #     root.right = self.convertBST(root.right)
    #
    #     node = root.right
    #     value = 0
    #     while node:
    #         value = node.val
    #         node = node.left
    #
    #     root.val += value
    #
    #     root.left = self.convertBST(root.left)
    #     self.add(root.left, root.val)
    #
    #     return root
    #
    # def add(self, root, value):
    #     if not root:
    #         return
    #     root.val += value
    #     self.add(root.left, value)
    #     self.add(root.right, value)