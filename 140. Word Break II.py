class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 在dfs之前，dp先判定s是否可以被分割，如果不能被分割，剪枝
        self.result = []
        self.dfs(s, wordDict, tmp=[])
        return self.result

    def dfs(self, s, wordDict, tmp):
        if self.check(s, wordDict):
            if not s:
                self.result.append(' '.join(tmp))
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, tmp + [s[:i]])

    def check(self, s, wordDict):
        if s == '':
            return True
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict and dp[j + 1] == True:
                    dp[i] = True
        return dp[0]
