# Time:  O(26 * n) = O(n)
# Space: O(26) = O(1)
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s, k, 0, len(s) - 1)

    def helper(self, s, k, start, end):
        count = [0] * 26
        for i in range(start, end + 1):
            count[ord(s[i]) - ord('a')] += 1
        res = 0
        i = start
        while i <= end:
            while i <= end and count[ord(s[i]) - ord('a')] < k:  # 找到满足>=k的起始点
                i += 1
            j = i
            while j <= end and count[ord(s[j]) - ord('a')] >= k:  # 如k则记为终点
                j += 1

            if i == start and j - 1 == end:  # 整段都符合要求，直接return
                return end - start + 1

            res = max(res, self.helper(s, k, i, j - 1))  # recursion分段更新res
            i = j + 1

        return res