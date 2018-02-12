# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findBottomLeftValueHelper(root, curr_depth, max_depth, bottom_left_value):
            if not root:
                return max_depth, bottom_left_value
            if not root.left and not root.right and curr_depth + 1 > max_depth:
                return curr_depth + 1, root.val
            max_depth, bottom_left_value = findBottomLeftValueHelper(root.left, curr_depth + 1, max_depth,
                                                                     bottom_left_value)
            max_depth, bottom_left_value = findBottomLeftValueHelper(root.right, curr_depth + 1, max_depth,
                                                                     bottom_left_value)
            return max_depth, bottom_left_value

        result, max_depth = 0, 0
        return findBottomLeftValueHelper(root, 0, max_depth, result)[1]

    # TLE
    #     if not root:
    #         return None
    #
    #     return self.helper(root, 1, root.val)[1]
    #
    # def helper(self, root, layer, value):
    #     if not root.left and not root.right:
    #         return layer, value
    #     elif root.left and root.right:
    #         maxlayer = max(self.helper(root.left, layer + 1, root.left.val)[0],
    #                        self.helper(root.right, layer + 1, root.right.val)[0])
    #         if maxlayer == self.helper(root.left, layer + 1, root.left.val)[0]:
    #             return self.helper(root.left, layer + 1, root.left.val)
    #         else:
    #             return self.helper(root.right, layer + 1, root.right.val)
    #     elif root.left:
    #         return self.helper(root.left, layer + 1, root.left.val)
    #     else:
    #         return self.helper(root.right, layer + 1, root.right.val)