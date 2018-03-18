# -*- coding: utf-8 -*-
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Time:  O(2^n)
        # Space: O(1)
        #         n=3时，正确的GrayCode应该是
        #         000
        #         001
        #         011
        #         010
        #         110
        #         111
        #         101
        #         100

        #         n=k时的Gray Code，相当于0加上n=k-1时的Gray Code，以及1加上n=k-1时的Gray Code逆序

        if n == 0:
            return [0]
        res = ['0', '1']
        while n > 1:
            res = ['0' + x for x in res] + ['1' + x for x in res[::-1]]
            n -= 1
        return [int(x, 2) for x in res]


        # if n == 0:
        #     return [0]
        #
        # result = self.grayCode(n - 1)
        # seq = list(result)
        # for i in reversed(result):
        #     seq.append((1 << (n - 1)) | i)  # 只要对应的二个二进位有一个为1时，结果位就为1。
        #
        # return seq

        # 格雷码的生成
        res = []
        size = 1 << n
        for i in range(size):
            res.append((i >> 1) ^ i) # 当两对应的二进位相异时，结果为1
        return res

if __name__ == '__main__':
    answer = Solution()
    print answer.grayCode(3)