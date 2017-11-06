class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        freq_list = collections.Counter(s)

        for k, v in enumerate(s):
            if freq_list[v] == 1:
                return k
        return -1