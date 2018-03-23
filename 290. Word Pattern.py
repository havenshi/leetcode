# Time:  O(n)
# Space: O(n)
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # method 2 very slow
        keys = list(pattern)
        values = str.split(' ')
        if len(keys) != len(values):
            return False

        dictionary1 = {}
        dictionary2 = {}
        for k, v in zip(keys, values):
            if (not k in dictionary1) and (not v in dictionary2):
                dictionary1[k] = v
                dictionary2[v] = k
            elif not v in dictionary2 or dictionary2[v] != k:
                return False

        return True


if __name__  == '__main__':
    print Solution().wordPattern("abba","dog dog dog dog")