# Time: O(n^2*k), n the total number of words, k the average length of each word
# Space: O(1)
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and self.valid(words[i], words[j]):
                    res.append([i, j])
        return res

    def valid(self, word1, word2):
        w = word1 + word2
        n = len(w)
        for i in range(n / 2):
            if w[i] != w[n - 1 - i]:
                return False
        return True

# Method 2, HashTable
# Time: O(n*k)
# Space: O(n*k)

# 思路: 将所有的单词逆序加入hash表中, 然后再遍历一遍数组, 然后会有两种情况

# 1. 将单词的前一部分如果可以在hash表中找到匹配说明这部分是可以回文的, 如果这个单词剩下的部分也是回文, 那么这两个单词就可以配成回文. 例如aabbcc和bbaa, 其中bbaa在hash表中是以逆序存在的, 即aabb, 那么当我们遍历到aabbcc的时候其前半部分aabb可以在hash表中查到, 并且剩余部分cc是回文, 因此他们可以构成回文


# 2. 如果单词的后一部分可以在hash表中查到, 并且其前一部分是回文, 他们也可以构成匹配. 例如aabb和ccbbaa, 其中aabb在hash表中是以bbaa存在的. 当我们遍历到ccbbaa的时候, 其后一部分bbaa可以在hash表中查到存在, 并且其前一部分cc是回文, 因此他们也可以构成回文.

