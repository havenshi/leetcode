# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
#
# Example 1:
#
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].

# 动态规划（Dynamic Programming）
#
# 数组dp[i]存储当T[0 .. i]在S中找到子序列匹配时，对应的最大起点下标
#
# 初始令dp[0 .. len(T) - 1] = -1

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ''
        ls, lt = len(S), len(T)
        dp = [-1] * lt
        for x in range(ls):
            for y in range(lt - 1, -1, -1):
                if T[y] == S[x]:
                    dp[y] = dp[y - 1] if y else x
                    if y == lt - 1 and dp[-1] > -1:
                        nlen = x - dp[-1] + 1
                        if not ans or nlen < len(ans):
                            ans = S[dp[-1] : x+1]
        return ans