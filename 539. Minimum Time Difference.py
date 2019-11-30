class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        minutes.sort()

        return min( (y - x) % (24 * 60)
                    for x, y in zip(minutes, minutes[1:] + minutes[:1]) )