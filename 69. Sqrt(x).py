class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sr = x
        while sr**2 > x:
            better = (sr+x/sr)/2
            sr = better
        return sr


        # method 2 binary
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return mid

if __name__ == "__main__":
    answer=Solution()
    print answer.mySqrt(2)
