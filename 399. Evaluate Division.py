class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s, t), v in zip(equations, values):
            g[s][t] = v
            g[t][s] = 1.0 / v
        for k in g:
            g[k][k] = 1.0
            for s in g:
                for t in g:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in queries:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans