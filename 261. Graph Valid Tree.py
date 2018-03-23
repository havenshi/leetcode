# -*- coding: utf-8 -*-
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
# Hint:
#
#   Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
#   According to the definition of tree on Wiki: 'a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.'
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# 先看当前节点是否被访问过，如果已经被访问过，说明环存在，直接返回false
# 再看v里面是否还有没被访问过的节点，如果有，则说明图不是完全连通的，返回false
# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
class Solution:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        # dfs
        import collections
        self.dict = collections.defaultdict(list)
        for edge in edges:
            self.dict[edge[0]].append(edge[1])
        self.v = [0]

        if not self.dfs(0, [0]):
            return False
        else:
            return len(self.v) == n

    def dfs(self, edge, visits):
        for neighbor in self.dict[edge]:
            if neighbor in visits:
                return False
            copyvisits = visits[:]
            copyvisits.append(neighbor)
            self.v.append(neighbor)
            if self.dfs(neighbor, copyvisits):
                continue
            else:
                return False
        return True


        # bfs
        import collections
        self.dict = collections.defaultdict(list)
        for edge in edges:
            self.dict[edge[0]].append(edge[1])
        self.v = [0]

        queue = collections.deque([0])
        while queue:
            edge = queue.popleft()
            for neighbor in self.dict[edge]:
                if neighbor in self.v:
                    return False
                queue.append(neighbor)
                self.v.append(neighbor)

        return len(self.v) == n


if __name__ == '__main__':
    print Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print Solution().validTree(5, [[0, 1], [1, 2], [3, 4]])