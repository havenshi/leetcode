class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        for i in range(len(t)):
            if index == len(s):
                break
            if t[i] == s[index]:
                index += 1

        return True if index == len(s) else False