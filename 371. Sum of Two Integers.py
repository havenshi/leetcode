# Time:  O(1)
# Space: O(1)
# 不懂。。。
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_BIT = 2 ** 32
        MAX_BIT_COMPLIMENT = -2 ** 32

        while b != 0:

            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT

            carry = a & b
            # print carry

            a = a ^ b
            # print a

            b = carry << 1
            # print b

        return a