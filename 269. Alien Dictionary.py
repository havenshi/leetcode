# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
#  You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new
# language. Derive the order of letters in this language.
#
# For example,
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# The correct order is: "wertf".
#
# Note:
#
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# 有向图的拓扑排序。进来的边为入度，出去的边为出度。生成图的结构，然后按照如下规则排序：
# 1. 找出当前入度为0的节点
# 2. 所有和该节点相连接的节点入度减1
# 3. go to #1
