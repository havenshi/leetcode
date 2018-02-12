# -*- coding: utf-8 -*-
# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
#
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# 首先构建一个单词前缀prefix->单词word的字典mdict
#
# 深度优先搜索search(word, line)，其中word是当前单词，line是行数
#
# 利用变量matrix记录当前已经生成的单词
#
# 前缀prefix = matrix[0..line][line]，如果prefix对应单词不存在，则可以剪枝
#
# 否则枚举mdict[prefix]，并递归搜索

import collections
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        m = len(words)
        n = len(words[0]) if m else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        matrix = []
        ans = []
        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1)
            matrix.pop()
        for word in words:
            search(word, 1)
        return ans