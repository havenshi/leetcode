import textwrap

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        map = {}
        n = len(words)
        m = len(words[0])
        res = []
        for item in words:
            if item not in map:
                map[item] = 1
            else:
                map[item] += 1
        for i in range(len(s)-m*n+1):
            new_map = {}
            j = 0
            while j < n:
                word = s[i+j*m:i+j*m+m]
                if word not in map:
                    break
                if word not in new_map:
                    new_map[word] = 1
                else:
                    new_map[word] += 1
                if new_map[word] > map[word]:
                    break
                j += 1
            if new_map == map:
                res.append(i)
        return res
    # TLE
    #     if not words:
    #         return []
    #     n = len(words)
    #     m = len(words[0])
    #     res = []
    #     for i in range(len(s)):
    #         tmp = s[i:i + n * m]
    #         new_tmp = textwrap.wrap(tmp, m)
    #         if self.match(new_tmp, words):
    #             res.append(i)
    #     return res
    #
    # def match(self, list1, list2):
    #     map = {}
    #     for item in list1:
    #         if item not in map:
    #             map[item] = 1
    #         else:
    #             map[item] += 1
    #     for item in list2:
    #         if item not in map:
    #             return False
    #         else:
    #             map[item] -= 1
    #     if map.values() != [0] * len(map):
    #         return False
    #     return True

if __name__ == '__main__':
    print Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])