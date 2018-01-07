class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = 0
        while m != n:  # m与n的公共“左边首部（left header）
            m >>= 1
            n >>= 1
            p += 1  # 记录位移了多少次
        return m << p
