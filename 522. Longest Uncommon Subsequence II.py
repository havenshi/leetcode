class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs = sorted(strs, key=len, reverse=True)
        for i, w1 in enumerate(strs):
            if all(not self.subseq(w1, w2) for j, w2 in enumerate(strs) if i != j):
                return len(w1)
        return -1

    def subseq(self, w1, w2):
        # check if w1 is a subsequence of w2
        i = 0
        for c in w2:
            if i < len(w1) and w1[i] == c:
                i += 1
        return i == len(w1)
