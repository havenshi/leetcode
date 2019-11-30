class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return "".join(
            [s[i * k: (i + 1) * k] if i % 2 != 0 else s[i * k: (i + 1) * k][::-1] for i in range(len(s) / k + 1)])
