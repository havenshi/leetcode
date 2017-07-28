class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = 0
        for item in s[::-1]:
            value = ord(item) - ord('A') + 1
            res += value * (26 ** count)
            count += 1
        return res

        # alpha = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        # array = list(s)
        # res = 0
        # for a in array:
        #     res = res * 26 + alpha.index(a) + 1
        # return res