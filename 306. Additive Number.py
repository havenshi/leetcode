# Time:  O(n^3)
# Space: O(n)

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                s1, s2 = num[0:i], num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue

                expected = str(int(s1) + int(s2))
                cur = s1 + s2 + expected
                while len(cur) < len(num):
                    s1, s2, expected = s2, expected, str(int(s2) + int(expected))
                    cur += expected
                if cur == num:
                    return True
        return False