# -*- coding: utf-8 -*-
# Given a non-empty string, encode the string such that its encoded length is the shortest.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
#
# Note:
#
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
# Example 1:
#
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
# Example 2:
#
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:
#
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
# Example 4:
#
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:
#
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".

# 利用字典dp记录字符串的最优编码串
#
# 枚举分隔点p， 将字符串拆解为left, right左右两部分
#
# 尝试将left调用solve函数进行编码压缩，并对right递归调用encode函数进行搜索
#
# 将left和right组合的最短字符串返回，并更新dp

class Solution(object):
    def __init__(self):
        self.dp = dict()

    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1: return s
        if s in self.dp: return self.dp[s]
        ans = s
        for p in range(1, size + 1):
            left, right = s[:p], s[p:]
            t = self.solve(left) + self.encode(right)
            if len(t) < len(ans): ans = t
        self.dp[s] = ans
        return ans

    def solve(self, s):
        ans = s
        size = len(s)
        for x in range(1, size / 2 + 1):
            if size % x or s[:x] * (size / x) != s: continue
            y = str(size / x) + '[' + self.encode(s[:x]) + ']'
            if len(y) < len(ans): ans = y
        return ans

# 好难。。。