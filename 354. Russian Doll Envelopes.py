class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # 如果在x维度上升序排列，而在x相同的情况下，在y维度上降序排列，那么上例的排序结果就是：[[2,3], [5,4], [6,7], [6,4]]。我们发现，只要在y维度上找到最长递增子序列，就对应了本题的答案。

        envelopes.sort(cmp=self.sort)

        # 没写完，后面的方法同300题

    def sort(self, x, y):
        if x[0] != y[0]:
            return x[0] - y[0]
        else:
            return y[1] - x[1]