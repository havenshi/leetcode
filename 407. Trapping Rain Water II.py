# -*- coding: utf-8 -*-
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
                if x in (0, m - 1) or y in (0, n - 1): # peakMap四周的值为对应heightMap的值，中间部分全部为inf
                    peakMap[x][y] = heightMap[x][y]
                    q.append((x, y)) # q记录四周点的位置

        while q:
            x, y = q.pop(0)
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if nx <= 0 or nx >= m - 1 or ny <= 0 or ny >= n - 1: continue
                limit = max(peakMap[x][y], heightMap[nx][ny])
                if peakMap[nx][ny] > limit: # 如果nxny该位置的值较xy值大，则nxny更新为较小值
                    peakMap[nx][ny] = limit
                    q.append((nx, ny))

        return sum(peakMap[x][y] - heightMap[x][y] for x in range(m) for y in range(n))

        # m = len(heightMap)
        # n = len(heightMap[0])
        #
        # dp_lr = []
        # for i in range(m):
        #     dp_left = [0] * n
        #     for x in range(1, n):
        #         dp_left[x] = max(heightMap[i][x-1], dp_left[x - 1])
        #     dp_right = [0] * n
        #     for x in range(n - 2, -1, -1):
        #         dp_right[x] = max(heightMap[i][x+1], dp_right[x + 1])
        #     dp_lr.append([min(dp_left[x], dp_right[x]) for x in range(n)])
        #
        # dp_ub = []
        # for j in range(n):
        #     dp_up = [0] * m
        #     for y in range(1, m):
        #         dp_up[y] = max(heightMap[y-1][j], dp_up[y - 1])
        #     dp_bottom = [0] * m
        #     for y in range(m - 2, -1, -1):
        #         dp_bottom[y] = max(heightMap[y+1][j], dp_bottom[y + 1])
        #     dp_ub.append([min(dp_up[y], dp_bottom[y]) for y in range(m)])
        #
        # print dp_lr
        # print dp_ub
        #
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         ceiling = min(dp_lr[i][j], dp_ub[j][i])
        #         if ceiling > heightMap[i][j]:
        #             res += ceiling - heightMap[i][j]
        # return res

if __name__ == '__main__':
    print Solution().trapRainWater([
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
])