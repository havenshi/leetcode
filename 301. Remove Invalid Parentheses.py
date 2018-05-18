# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.visited = set([s])
        return self.dfs(s)

    def dfs(self, s):  # 尝试从输入字符串中移除括号，若得到的新字符串的失配括号比原字符串少，则继续搜索；否则剪枝。
        mi = self.calc(s)
        if mi == 0:
            return [s]
        ans = []
        for x in range(len(s)):
            if s[x] in ('(', ')'):
                ns = s[:x] + s[x + 1:]
                if ns not in self.visited and self.calc(ns) < mi:
                    self.visited.add(ns)
                    ans.extend(self.dfs(ns))
        return ans

    def calc(self, s):  # 变量a统计失配的左括号数目，变量b统计失配的右括号数目
        a = b = 0
        for c in s:
            a += {'(': 1, ')': -1}.get(c, 0)
            b += a < 0
            a = max(a, 0)
        return a + b

