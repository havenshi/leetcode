# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(n)
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    # dfs
    def cloneGraph(self, node):
        if node == None:
            return None
        return self.dfs(node, {})

    def dfs(self, node, map):
        if node in map:
            return map[node]
        copynode = UndirectedGraphNode(node.label)
        map[node] = copynode   # map来存储原图中的节点和新图中的节点的一一映射
        for neighbor in node.neighbors:
            copynode.neighbors.append(self.dfs(neighbor, map))
        return copynode

    # bfs
        if node == None:
            return None
        queue = []
        map = {}
        copynode = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = copynode
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copyneighbor = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copyneighbor)
                    map[neighbor] = copyneighbor
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    copyneighbor = map[neighbor]
                    map[curr].neighbors.append(copyneighbor)
        return copynode