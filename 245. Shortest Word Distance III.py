# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = "makes", word2 = "coding", return 1.
# Given word1 = "makes", word2 = "makes", return 3.
#
# Note:
# You may assume word1 and word2 are both in the list.


# Time:  O(n)
# Space: O(1)

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        res = float("inf")
        index1, index2 = None, None
        for i in range(len(words)):
            if words[i] == word1:
                if word1 == word2 and index1 is not None: # if same, only update index1, new index - old index
                    res = min(res, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                if index1 != index2:
                    res = min(res, abs(index1 - index2))
        return res

if __name__ == '__main__':
    print Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    print Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
