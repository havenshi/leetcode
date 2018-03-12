class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # dfs + hash
        import collections
        self.dictionary = collections.defaultdict(list)
        for i in range(len(equations)):
            self.dictionary[equations[i][0]].append([equations[i][1],values[i]])
            self.dictionary[equations[i][1]].append([equations[i][0], 1.0/values[i]])
        ans = []
        for q1, q2 in queries:
            ans.append(self.dfs(q1, q2, [q1], 1))
        return ans

    def dfs(self, q1, q2, visits, prev_value):
        if q1 not in self.dictionary or q2 not in self.dictionary:
            return -1
        if q2 == q1:
            return prev_value
        for qchild in self.dictionary[q1]:
            if q2 == qchild[0]:
                return prev_value*qchild[1]
            if qchild[0] not in visits and self.dfs(qchild[0], q2, visits+[qchild[0]], prev_value*qchild[1]) != -1:
                return self.dfs(qchild[0], q2, visits+[qchild[0]], prev_value*qchild[1])
        return -1


        # O(n3), very slow
        # g = collections.defaultdict(lambda: collections.defaultdict(int))
        # for (s, t), v in zip(equations, values):
        #     g[s][t] = v
        #     g[t][s] = 1.0 / v
        # for k in g:
        #     g[k][k] = 1.0
        #     for s in g:
        #         for t in g:
        #             if g[s][k] and g[k][t]:
        #                 g[s][t] = g[s][k] * g[k][t]
        # ans = []
        # for s, t in queries:
        #     ans.append(g[s][t] if g[s][t] else -1.0)
        # return ans

if __name__ == '__main__':
    print Solution().calcEquation([ ["a","b"],["b","c"] ], [2.0,3.0], [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ])

