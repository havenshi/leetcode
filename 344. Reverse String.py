# Time:  O(n)
# Space: O(n)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start, end = 0, len(s) - 1
        for i in range((end - start) / 2 + 1):
            s[start + i], s[end - i] = s[end - i], s[start + i]
        return ''.join(s)
