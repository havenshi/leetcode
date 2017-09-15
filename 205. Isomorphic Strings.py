class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        hashmap1 = {}
        hashmap2 = {}
        for i in range(len(s)):
            if s[i] not in hashmap1 and t[i] not in hashmap2:
                hashmap1[s[i]] = t[i]
                hashmap2[t[i]] = s[i]
            if t[i] not in hashmap2 or hashmap2[t[i]] != s[i]:
                return False
        return True

if __name__ == '__main__':
    print Solution().isIsomorphic('ab','aa')