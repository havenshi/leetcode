class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import copy
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1
        res = []
        step = len(words[0])
        total_step = step * len(words)
        for i in range(len(s)):
            tmp = copy.deepcopy(hashmap)
            if self.helper(s[i:i + total_step], tmp, step):
                res.append(i)
        return res

    def helper(self, string, hashmap, step):
        start = 0
        while start <= len(string) - step:
            if string[start:start + step] in hashmap and hashmap[string[start:start + step]] > 0:
                hashmap[string[start:start + step]] -= 1
            else:
                return False
            start += step
        if sum(hashmap.values()) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().findSubstring("barfoothefoobarman",["foo","bar"])
