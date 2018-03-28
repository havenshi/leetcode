# Time:  O(n*log(m))
# Space: O(m)
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        count = 0
        res = None
        m, n = len(matrix), len(matrix[0])
        heap = []
        for x in range(m):
            heap.append((matrix[x][0], x, 0))
        heapq.heapify(heap)
        while count < k:
            cur = heapq.heappop(heap)
            res = cur[0]
            count += 1
            i,j = cur[1],cur[2]
            if j+1 < len(matrix[i]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return res