class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # paragraph = paragraph.translate(None, string.punctuation)
        paragraph = ' '.join(paragraph.split(','))

        exclude = set(string.punctuation)
        paragraph = ''.join(ch.lower() for ch in paragraph if ch not in exclude)
        newp = paragraph.split()

        dict = collections.Counter(newp)
        count = 0
        res = None
        for k, v in dict.items():
            if k not in banned and count < v:
                count = v
                res = k
        return res