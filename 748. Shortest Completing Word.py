import collections
import copy


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        dictionary = collections.Counter([x for x in licensePlate.lower() if x.isalpha()])
        ans = None
        count = float('inf')
        for word in words:
            newdict = copy.deepcopy(dictionary)
            newcount = 0
            for i in range(len(word)):
                if word[i] in newdict and newdict[word[i]] != 0:
                    newcount += i
                    newdict[word[i]] -= 1
            if newcount < count and all([x == 0 for x in map(newdict.get, newdict)]):
                ans = word
                count = newcount
        return ans
        # "1s3 456",["looks", "pest", "stew", "show"], why return "pest"?
if __name__ == '__main__':
    print Solution().shortestCompletingWord("1s3 PSt",["step","steps","stripe","stepple"])