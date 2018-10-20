# Time:  O((|E| + |V|) * log|V|) = O(|E| * log|V|),
# Space: O(|E| + |V|) = O(|E|)

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dict = collections.defaultdict(list)
        for u, v, w in flights:
            dict[u].append((v, w))

        best = collections.defaultdict(
            lambda: collections.defaultdict(lambda: float("inf")))  # best[dst][stops]=minprice
        min_heap = [(0, src, K + 1)]  # price, src, stops. since dst will not be count as stops, so use K+1
        while min_heap:  # why heap? find min price faster
            result, u, k = heapq.heappop(min_heap)
            if k < 0 or best[u][k] < result:
                continue
            if u == dst:
                return result
            for v, w in dict[u]:
                if result + w < best[v][k - 1]:  # k-1 is stops limitation, how many stops left we can use
                    best[v][k - 1] = result + w
                    heapq.heappush(min_heap, (result + w, v, k - 1))
        return -1
