# -*- coding:utf8 -*-
# Time:  O(n)
# Space: O(h)

class Solution2:
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