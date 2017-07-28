class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        dic = {}
        res = []
        for i in range(n-10+1):
            substr = s[i:i+10]
            dic[substr] = dic.get(substr, 0) + 1
        for key, val in dic.items():
            if val > 1:
                res.append(key)
        return res

if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")