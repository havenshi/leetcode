class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line, length = [], 0
        results = []
        for w in words:
            if length + len(w) + len(line) <= maxWidth:
                length += len(w)
                line.append(w)
            else:
                results.append(self._format(line, maxWidth))
                length = len(w)
                line = [w]
        if len(line):
            results.append(self._formatLast(line, maxWidth))
        return results

    def _format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        s, gaps = line[0], len(line) - 1
        for index, w in enumerate(line[1:]): # (maxWidth - length)个space如何分配
            if index < (maxWidth - length) % gaps: # (maxWidth - length) % gaps 是平均分配后还剩多少个空格
                s = s + " " + " " * ((maxWidth - length) / gaps) + w # index较小的时候再加一个空格，可以保证empty slots on left be assigned more spaces than right
                                                                     # 0-(remain-1)正好为remain的个数
            else:
                s = s + " " * ((maxWidth - length) / gaps) + w # gaps = n-1, (maxWidth - length) / gaps 是空格平均分配在(n-1)个元素后面
        return s

    def _formatLast(self, line, maxWidth):
        s = ' '.join(line)
        return s + " " * (maxWidth - len(s))