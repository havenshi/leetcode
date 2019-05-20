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



# Time: O(nlogk)
# Space: O(n)
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = collections.Counter(words)
        h = [(-frequency, item) for item, frequency in cnt.items()]
        heapq.heapify(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res