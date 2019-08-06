class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        res = 0
        mid = int(num ** 0.5)
        for i in range(1, mid + 1):
            if num % i == 0 and mid ** 2 != num:
                res += i
                res += num / i
            elif num % i == 0 and mid ** 2 == num:
                res += num ** 0.5
        return res == 2 * num
