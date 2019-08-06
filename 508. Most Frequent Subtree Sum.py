# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = {}
        self.dfs(root)
        mostFreq = 0
        ans = []
        for key in self.d:
            if self.d[key] > mostFreq:
                mostFreq = self.d[key]
                ans = [key]
            elif self.d[key] == mostFreq:
                ans.append(key)
        return ans

    def dfs(self, root):
        if not root:
            return 0
        tmp = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.d[tmp] = self.d.get(tmp, 0) + 1
        return tmp