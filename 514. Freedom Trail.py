class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        # 状态转移方程：
        # dp[k][i] = min(dp[k][i], dp[k - 1][j] + min(abs(i - j), len(ring) - abs(i - j)))
        # 其中k表示当前字符在key中的下标，i表示当前字符在ring中的下标，j表示上一个字符在ring中的下标。
        rlist = collections.defaultdict(list)
        for i, r in enumerate(ring):
            rlist[r].append(i)
        rsize = len(ring)
        dp0 = {0 : 0}
        for c in key:
            dp = {}
            for i in rlist[c]:
                dp[i] = 0x7FFFFFFF
                for j in dp0:
                    dp[i] = min(dp[i], dp0[j] + min(abs(i - j), rsize - abs(i - j)))
            dp0 = dp
        return min(dp.values()) + len(key)