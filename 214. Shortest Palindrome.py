# Time:n^2, TLE
# Space:1
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        mid = (length-1)/2 # 如长度为4，取位置1；如长度为5；取位置2
        while mid >= 0:
            pre_len = len(s[:mid])
            if s[:mid] == s[mid+1:mid+1+pre_len][::-1]:
                return s[mid+1+pre_len:][::-1]+s
            elif mid >= 1 and s[mid] == s[mid-1] and s[:mid-1] == s[mid+1:mid+1+pre_len-1][::-1]:
                return s[mid+1+pre_len-1:][::-1]+s
            mid -= 1
        return s[1:][::-1]+s




# Time:O(m+n)，kmp解法
# Space:O(1)
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 只关心p数组的最后一个值p[-1]，因为它表明了rev_s与s相互匹配的最大前缀长度。
        # 最后只需要将rev_s的前k个字符与原始串s拼接即可，其中k是s的长度len(s)与p[-1]之差。
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[: len(s) - p[-1]] + s