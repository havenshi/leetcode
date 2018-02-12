# -*- coding: utf-8 -*-
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
#
# Example 1:
#
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
#
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# Note:
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].

# 时间复杂度O(n * m)，其中n为s的长度，m为dict中字符串长度之和

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        start = end = -1
        ans = ''
        for x, c in enumerate(s):
            nend = 0
            for d in dict: # 遍历dict，寻找与s[x:]匹配长度最长的子串，记其长度为nend
                if s[x:].startswith(d):
                    nend = max(nend, len(d))
            if nend: # 若nend > 0：
                if start == -1: start = x
                end = max(end, nend + x)
                # 之后继续遍历下面的x,c，因为如果下面还有匹配子串，则要把若干段子串统一加标记
            else:
                if x >= end: # 若 x >= end > 0：此时x在所有匹配子串之后
                    # 需要将<b> + s[start:end] + </b>累加至答案，并将start与end重置为-1!
                    ans += '<b>' + s[start:end] + '</b>'
                    start = end = -1
                if start == -1: ans += c # 若start == -1：将c累加至答案

        if start > -1: ans += '<b>' + s[start:end] + '</b>'
        return ans