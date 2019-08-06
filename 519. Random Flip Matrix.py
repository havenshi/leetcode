class Solution(object):
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.m = n_rows
        self.n = n_cols
        self.total = n_rows * n_cols
        self.visits = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        pos = random.randint(0, self.total - 1)
        while pos in self.visits:
            pos = random.randint(0, self.total - 1)
        self.visits.add(pos)
        return [pos / self.n, pos % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.visits = set()



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(n_rows, n_cols)
        # param_1 = obj.flip()
        # obj.reset()