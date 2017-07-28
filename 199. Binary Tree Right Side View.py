# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0) # for i in range(original queue), pop(0), pop all node of same layer
                if i == 0:  # get the most right val of same layer
                    ans.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return ans
