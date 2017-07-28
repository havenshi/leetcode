class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == "":
            return []
        self.result = []
        self.dfs(s, tmp=[])
        return self.result

    def dfs(self, s, tmp):
        if s == '':
            self.result.append(tmp)
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], tmp + [s[:i]])

    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    answer = Solution()
    print answer.partition("aab")

