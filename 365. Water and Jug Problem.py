def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return z == 0 or ((x + y >= z) and (z % gcd(x, y) == 0))