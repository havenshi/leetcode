class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        sum = 0
        s = s[::-1]
        while s != "":
            if s[:2][::-1] in numerals:
                sum += values[numerals.index(s[:2][::-1])]
                s = s[2:]
            elif s[:1] in numerals:
                sum += values[numerals.index(s[:1])]
                s = s[1:]
        return sum

# 用dictionary才快
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        res = 0
        i = len(s)-1
        while i >= 0:
            if i-1>=0 and s[i-1:i+1] in dictionary:
                res += dictionary[s[i-1:i+1]]
                i -= 2
            else:
                res += dictionary[s[i]]
                i -= 1
        return res
if __name__ == "__main__":
    answer=Solution()
    print answer.romanToInt("MCMXCVI")

