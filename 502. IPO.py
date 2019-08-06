class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        heap = []
        for i in range(len(Profits)):
            heap.append((-Profits[i], Capital[i]))
        heapq.heapify(heap)
        i = 0
        P = 0
        while i < k and heap:
            tmp = []
            flag = True
            while flag and heap:
                cur = heapq.heappop(heap)
                # print W, cur[0],cur[1]
                if W >= cur[1]:
                    P += -cur[0]
                    W -= cur[1]
                    W += -cur[0]
                    i += 1
                    flag = False
                else:
                    tmp.append(cur)
            if flag and not heap: # if not able to find a cur forever, then stop
                break
            for t in tmp: # push the curs(capital not meet requirement) in tmp back in to heap
                heapq.heappush(heap, (t[0], t[1]))
            # print i, heap, W
        return P