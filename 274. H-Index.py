class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(n)
        N = len(citations)
        cnts = [0] * (N + 1)
        for c in citations:
            cnts[[c, N][c > N]] += 1
        # cnts记录引用次数在0 ~ N（N篇以上的记为N）的文章个数, cnts = [1, 1, 0, 1, 0, 2]

        sums = 0
        for h in range(N, 0, -1):  # reverse tranversal
            if sums + cnts[h] >= h:
                return h
            sums += cnts[h]
        return 0


        # O(nlogn)
        # i: 0 1 2 3 4
        # c: 6 5 3 1 0
        for i, c in enumerate(sorted(citations, reverse = True)):
            if i >= c:
                return i # now i = 3, which is actually the numbers of c = 3
        return len(citations) # when c is much greater, like [100]