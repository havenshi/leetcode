# -*- coding:utf-8 -*-
# Time:  O(n)
# Space: O(1)
# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        res = 0
        # left用于记录合法的左边界位置，last用于记录字符上一次出现的位置
        left = 0
        last = {}
        for i in range(len(s)):
            # 如字符在last中出现过，则除去上次的字符，即slice window 变更left至上一次s[i]出现位置之后，使得子串合法
            # 删字符时，应该删光最后出现位置在最左的字符（如“abac”应删所有b即ab而不是所有a即aba），可保证被全部删除后所减小的长度越少
            if len(last) == 2 and s[i] not in last:
                minlast = min(last.values()) # 选择last中value最小的
                minkey = min(last, key=last.get) # 找到该value的key
                left = minlast + 1 # 从该key向右移动
                del last[minkey] # 删除该字符
            last[s[i]] = i
            res = max(res, i - left + 1)
        return res

        # if len(s) == 0:
        #     return 0
        # curlen = 1
        # maxlen = 1
        # flag = 0
        # for i in range(1, len(s)):
        #     news = "".join(set(s[flag:i+1]))
        #     if len(news) <= 2:
        #         curlen += 1
        #         maxlen = max(maxlen, curlen)
        #     else:
        #         curlen = 1
        #         flag = i
        # return maxlen

if __name__ == '__main__':
    answer = Solution()
    print answer.lengthOfLongestSubstringTwoDistinct('cecba')

