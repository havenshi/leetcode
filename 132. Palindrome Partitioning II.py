class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s)+1)] # 从第i个字符到最后一个字符，最少的分割次数下，有多少个回文字符串，即分割次数+1
        p = [[False for i in range(len(s))] for j in range(len(s))] # 从字符i到j是否为一个回文字符串
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]): # s[i:j+1]为回文字
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1