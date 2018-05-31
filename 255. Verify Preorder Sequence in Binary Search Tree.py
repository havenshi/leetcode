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



# Q：如何验证中序序列？
# A：中序序列是有序的，只要验证其是否升序的就行了。
#
# Q：如何验证后序序列？
# A：后序序列的顺序是left - right - root，而先序的顺序是root - left - right。从数组的后面向前面遍历，因为root在数组后面了。
# 而且因为从后往前看是先遇到right再遇到left，所以我们要记录的是限定的最大值，而不再是最小值，栈pop的条件也变成pop所有比当前数大得数。
# 栈的增长方向也是从高向低了。