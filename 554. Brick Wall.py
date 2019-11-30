class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(len(wall)):
            for j in range(len(wall[i])-1):
                if j == 0:
                    d[wall[i][j]] = d.get(wall[i][j], 0) + 1
                else:
                    wall[i][j] += wall[i][j-1]
                    d[wall[i][j]] = d.get(wall[i][j], 0) + 1
        print wall
        print d
        if d:
            return len(wall) - max([x for x in d.values()])
        else:
            return len(wall)