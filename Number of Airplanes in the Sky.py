class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def sorter(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        timepoints = []
        for airplane in airplanes:
            timepoints.append((airplane.start, 1))
            timepoints.append((airplane.end, -1))

        print timepoints

        timepoints = sorted(timepoints, cmp=sorter)

        print timepoints # [(1, 1), (2, 1), (3, -1), (4, 1), (5, 1), (7, -1), (8, -1), (10, -1)]
        sum, most = 0, 0
        for t, delta in timepoints:
            sum += delta
            most = max(most, sum)

        return most

if __name__=='__main__':
    answer = Solution()
    print answer.countOfAirplanes([Interval(1,10),Interval(2,3),Interval(5,8),Interval(4,7)])