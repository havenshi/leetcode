class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num

        # return (num - 1) % 9 + 1 if num > 0 else 0