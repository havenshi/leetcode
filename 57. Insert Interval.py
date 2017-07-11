# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]
        if not newInterval: return intervals

        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for key, val in enumerate(intervals[1:]):
            if res[-1].end < val.start:
                res.append(val)
            else:
                res[-1].end = max(res[-1].end, val.end)
        return res