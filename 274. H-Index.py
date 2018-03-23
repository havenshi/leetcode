class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Time:  O(n)
        # Space: O(n)
        n = len(citations)
        cnts = [0] * (n + 1)
        for i in range(n):
            if citations[i] <= n:
                cnts[citations[i]] += 1
            else:
                cnts[n] += 1
        # cnts记录引用次数在0 ~ N（N篇以上的记为N）的文章个数, cnts = [1, 1, 0, 1, 0, 2]

        sums = 0
        for h in range(n, 0, -1):  # reverse tranversal
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