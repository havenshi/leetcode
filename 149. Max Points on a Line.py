# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from fractions import Fraction

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n < 3:
            return n
        res = -1
        for i in range(n):
            slope = {'inf': 0}
            samePointsNum = 1
            for j in range(i+1, n):
                if points[i].x == points[j].x and points[i].y != points[j].y: # slope is inf
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = Fraction(points[i].y - points[j].y, points[i].x - points[j].x)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:  # i and j are same points
                    samePointsNum += 1
            res = max(res, max(slope.values()) + samePointsNum) # value is all possible slopes between i and multiple j, add number of same point as i
        return res