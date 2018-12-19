class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        ans = [float("inf")] * N

        lastC = float("-inf")
        for i in range(N):  # 先从左边遍历，不断更新C的最右位置
            if S[i] == C:
                lastC = i
            ans[i] = min(ans[i], i - lastC)

        lastC = float("inf")
        for i in range(N - 1, -1, -1):  # 再从右边遍历，不断更新C的最左位置
            if S[i] == C:
                lastC = i
            ans[i] = min(ans[i], lastC - i)
        return ans