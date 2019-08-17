class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.total = sum(w)
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self):
        """
        :rtype: int
        """
        ind = random.randint(0, self.total - 1)
        # for i in range(len(self.w)):
        #     if ind <= self.w[i]:
        #         return i
        l, r = 0, len(self.w)
        while l + 1 < r:
            mid = (l + r) / 2
            if ind <= self.w[mid]:
                r = mid
            else:
                l = mid
        if ind <= self.w[l]:
            return l
        return r




        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()