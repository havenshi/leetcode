class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashmap = {}
        while n not in hashmap and n != 1:
            hashmap[n] = 1
            total = 0
            while n > 0:
                total += (n%10) ** 2
                n /= 10
            n = total
        return n == 1