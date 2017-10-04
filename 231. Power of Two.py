class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans << 1
        return False