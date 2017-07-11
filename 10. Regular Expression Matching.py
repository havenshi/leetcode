class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if len(p) == 0:
        #     return len(s) == 0
        # elif len(p) == 1 or (len(p) > 1 and p[1] != '*'):  # must judge p[0]
        #     if len(s) == 0 or (len(s) > 0 and s[0] != p[0] and p[0] != '.'): # cannot replace s[0]
        #         return False
        #     return self.isMatch(s[1:], p[1:])
        # else:  # p[1] == '*'
        #     i = 0
        #     while i < len(s) and (i < 0 or s[i] == p[0] or (s[i] != p[0] and p[0] == '.')):# i < 0 can omit (p[0] + '*'). s[i] == p[0], judge the left str
        #         if self.isMatch(s[i+1:], p[2:]): # p move (p[0] + '*') two steps
        #             return True
        #         i += 1                           # or keep (p[0] + '*'), only move s one step
        #     return False


        # DP
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':  # if '*', can omit the last (p[i-1] + '*')
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.': # if '.', omit s[i] and '.'.
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*': # if '*', omit '*' or omit (p[j-1] + '*') or omit s[i] when (s[i]==p[j-1] or p[j-1]=='.')
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else: # if s[i] == p[j]
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
if __name__ == '__main__':
    print Solution().isMatch("aab", "aa*")