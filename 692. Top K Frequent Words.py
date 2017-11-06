class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hash_table = {}
        for w in words:
            hash_table[w] = hash_table.get(w, 0) + 1
        print hash_table

        freqList = [[] for i in range(len(words) + 1)]
        for key in hash_table:
            freqList[hash_table[key]] += [key]
        # [[], [u'day'], [u'sunny'], [u'is'], [u'the'], [], [], [], [], [], []]

        ans = []
        for i in range(len(words), 0, -1):  # reverse sort by frequency
            ans += [j for j in sorted(freqList[i])]
        return ans[:k]
