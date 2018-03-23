# -*- coding:utf8 -*-
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Follow up:
# Could you do it using only constant space complexity?

# Time:  O(n)
# Space: O(h)

class Solution:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low = float('-inf')
        stack = []
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
            # 如果发现右子树，则把所有比它小的（包括parent）都pop出来，并更新low值直到low值是它的parent值
                low = stack[-1]
                stack.pop()
            stack.append(p) # node到最左的左子树，全部加入stack
        return True

if __name__ == '__main__':
    print Solution().verifyPreorder([5,2,1,3,6])