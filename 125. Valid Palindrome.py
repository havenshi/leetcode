class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        res = []  # 不能用''，因为python内部字符+很慢
        for item in s:
            if item.lower() >= 'a' and item.lower() <= 'z' or item >= '0' and item <= '9':
                    res.append(item.lower())
        for i in range(len(res)):
            if res[i] != res[len(res) - 1 - i]:
                return False
        return True