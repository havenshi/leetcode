# -*- coding: utf-8 -*-
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

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