class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0

        peakMap = [[float('inf')] * n for _ in range(m)]

        q = []
        for x in range(m):
            for y in range(n):
                if x in (0, m - 1) or y in (0, n - 1):
                    peakMap[x][y] = heightMap[x][y]
                    q.append((x, y))
        print peakMap
if __name__ == "__main__":
    print Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])



