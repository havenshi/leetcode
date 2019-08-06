class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.oneRow(word):
                res.append(word)
        return res

    def oneRow(self, word):
        row1 = [x for x in "qwertyuiop"]
        row2 = [x for x in "asdfghjkl"]
        row3 = [x for x in "zxcvbnm"]
        ind = 0
        for w in word:
            if w.lower() in row1:
                newInd = 1
            elif w.lower() in row2:
                newInd = 2
            elif w.lower() in row3:
                newInd = 3
            if ind and ind != newInd:
                return False
            else:
                ind = newInd
        return True