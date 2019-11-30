class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.count('A') <= 1 and s.count('LLL') == 0