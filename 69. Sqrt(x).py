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

        # Time:  O(logn)
        # Space: O(1)
        # method 2 binary
        low, high = 0, x
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return (low + high) / 2


        # method3 自己的方法
        low, high = 0, x
        while low + 1 < high:
            mid = (low + high) / 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid
            else:
                low = mid

        if low * low == x: return low
        if high * high == x: return high
        if low * low > x:
            return low - 1
        if low * low < x and high * high > x:
            return low
        if high * high < x:
            return high

if __name__ == "__main__":
    answer=Solution()
    print answer.mySqrt(2)
