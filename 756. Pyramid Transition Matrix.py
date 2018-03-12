class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        import collections
        self.dictionary = collections.defaultdict(list)
        for a in allowed:
            self.dictionary[a[:2]].append(a[2])
        return self.dfs(bottom, 0, '')

    def dfs(self, bottom, i, newbottom):
        if len(bottom) == 1:
            return True
        if i == len(bottom) - 1:
            return self.dfs(newbottom, 0, '')
        newb_list = self.dictionary[bottom[i:i + 2]]
        for newb in newb_list:
            if self.dfs(bottom, i + 1, newbottom + newb):
                return True
        return False