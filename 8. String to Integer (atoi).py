class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0

        MaxInt = (1 << 31) - 1
        res = 0
        sign = 1
        i = 0
        if str[0] == "+":
            i += 1
        if str[0] == "-":
            sign = -1
            i += 1
        while i < len(str):
            if str[i] < '0' or str[i] > '9': break
            res = res * 10 + int(str[i])
            if res >= MaxInt: break
            i += 1

        res *= sign
        if res >= MaxInt:
            return MaxInt
        if res < MaxInt * -1:
            return MaxInt * - 1 - 1
        return res

if __name__ == "__main__":
    answer = Solution()
    print answer.myAtoi("-123")