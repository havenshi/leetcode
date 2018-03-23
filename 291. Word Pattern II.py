# Time:  O(n * C(n - 1, c - 1)), n is length of str, c is unique count of pattern,
#                                there are H(n - c, c - 1) = C(n - 1, c - 1) possible splits of string,
#                                and each one costs O(n) to check if it matches the word pattern.
# Space: O(n + c)

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Examples:
#
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.
import copy
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, dictionary1 = {}, dictionary2 = {})

    def dfs(self, pattern, str, dictionary1, dictionary2):
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False
        k = pattern[0]
        for vlength in range(1, len(str)+1):
            v = str[:vlength]
            if (not k in dictionary1) and (not v in dictionary2):
                copydictionary1 = copy.deepcopy(dictionary1)
                copydictionary2= copy.deepcopy(dictionary2)
                copydictionary1[k] = v
                copydictionary2[v] = k
                if self.dfs(pattern[1:], str[vlength:], copydictionary1, copydictionary2):
                    return True
                else:
                    continue
            elif v in dictionary2 and dictionary2[v] == k:
                if self.dfs(pattern[1:], str[vlength:], dictionary1, dictionary2):
                    return True
                else:
                    continue
            elif not v in dictionary2 or dictionary2[v] != k:
                continue
        return False

if __name__  == '__main__':
    print Solution().wordPatternMatch("abba","dogcatcatdog")
    print Solution().wordPatternMatch("abab", "redblueredblue")
    print Solution().wordPatternMatch("aaaa", "asdasdasdasd")
    print Solution().wordPatternMatch("aabb", "xyzabcxzyabc")