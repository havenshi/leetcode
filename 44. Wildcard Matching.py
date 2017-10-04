class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':  # if '*', can omit the last (p[i-1] + '*')
                if i>=1:
                    dp[0][i]=dp[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='?': # if '?', omit s[i] and '?'.
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*': # if '*', omit '*' or omit s[i]
                    dp[i][j]=dp[i][j-1] or dp[i-1][j]
                else: # if s[i] == p[j]
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]

if __name__ == '__main__':
    print Solution().isMatch("aab", "c*a*b")