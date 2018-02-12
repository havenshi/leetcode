class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()

        result = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
                continue
            else:
                end = points[i][1]
                result += 1
        return result