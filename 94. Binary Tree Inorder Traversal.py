# Time:  O(n)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iteration_inorder(root)

    def iteration_inorder(self, root):
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def recursion_inorder(self, root):
        if not root:
            return []
        return self.recursion_inorder(root.left) + [root.val] + self.recursion_inorder(root.right)


# Morris Traversal
# 1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
#
# 2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
#    a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
#    b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
#
# 3. 重复以上1、2直到当前节点为空。
#
# Pro: O(1)空间
# Con: 改变了树的结构