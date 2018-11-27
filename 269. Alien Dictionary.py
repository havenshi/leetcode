# -*- coding: utf-8 -*-
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

# DFS
import sets
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = sets.Set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        # nodes = Set(['r', 'e', 't', 'w', 'f'])
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and \
                            words[i - 1][:len(words[i])] == words[i]:
                return ""
            self.findEdges(words[i - 1], words[i], ancestors)
        # ancestors = {'r': ['e'], 'e': ['w'], 't': ['r'], 'w': [], 'f': ['t']}

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""

        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break

    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False

if __name__ == "__main__":
    print Solution().alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])