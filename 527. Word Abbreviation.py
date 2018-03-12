# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.
#
# Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.
# Example:
#
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# Note:
#
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.

# hashmap + recursion
class Solution(object):
    def abbr(self, word, size):
        if len(word) - size <= 3: return word
        return word[:size + 1] + str(len(word) - size - 2) + word[-1]

    def solve(self, dict, size):
        dlist = collections.defaultdict(list)
        for word in dict:
            dlist[self.abbr(word, size)].append(word)
        for abbr, wlist in dlist.iteritems():
            if len(wlist) == 1:
                self.dmap[wlist[0]] = abbr
            else:
                self.solve(wlist, size + 1)

    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        self.dmap = {}
        self.solve(dict, 0)
        return map(self.dmap.get, dict)