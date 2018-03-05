# 转换为BST，此题关键是处理相同值的个数
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        bst = BinarySearchTree()
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans

class TreeNode(object):
    def __init__(self, val):
        self.leftCnt = 0 # 记录所有左边序列中比它小的值的个数
        self.val = val
        self.cnt = 1 # 初始化为1，记录与自己相同的值的个数
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        root = self.root
        count = 0
        while root:
            if val < root.val:
                root.leftCnt += 1 # 比root小，所以root.leftCnt加1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                count += root.leftCnt + root.cnt # root.leftCnt不变，因为该元素加在所有元素之后。但该元素自己的cnt应该加上所有比它小的/与自己相同的个数
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                count += root.leftCnt
                root.cnt += 1 # 相同值出现的情况下，只有旧值的cnt需要+1
                break
        return count