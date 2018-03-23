# Time:  O(n)
# Space: O(h)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.res = []
        self.dfs(root, [str(root.val)])
        return self.res

    def dfs(self, root, tmp):
        if not root.left and not root.right:
            self.res.append('->'.join(tmp))
            return
        if root.left:
            copytmp = tmp[:]
            copytmp.append(str(root.left.val))
            self.dfs(root.left, copytmp)
        if root.right:
            copytmp = tmp[:]
            copytmp.append(str(root.right.val))
            self.dfs(root.right, copytmp)

if __name__ == "__main__":
    head = TreeNode(6)
    current = head
    current.right = TreeNode(10)
    current.left = TreeNode(4)
    current = current.left
    current.left = TreeNode(1)
    current.right = TreeNode(5)
    current = head
    current = current.right
    current.right = TreeNode(15)
    current.left = TreeNode(8)
    prev = current
    current = current.left
    current.left = TreeNode(7)
    current.right = TreeNode(9)
    current = prev
    current = current.right
    current.left = TreeNode(12)
    current.right = TreeNode(18)

    s = Solution()
    print s.binaryTreePaths(head)

