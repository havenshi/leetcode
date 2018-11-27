class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        self.f = range(n)

        for x in range(n):
            for y in range(x + 1, n):
                if M[x][y]:
                    self.f[self.find(x)] = self.find(y)
        return sum(self.f[x] == x for x in range(n))

    def find(self, x):
        while self.f[x] != x:
            x = self.f[x]
        return x


#DFS
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count, n = 0, len(M)
        self.visited = set()

        for x in range(n):
            if x not in self.visited:
                count += 1
                self.dfs(M, x)
        return count

    def dfs(self, M, x):
        for y in range(len(M)):
            if M[x][y] and y not in self.visited:
                self.visited.add(y)
                self.dfs(M, y)


#BFS
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count, n = 0, len(M)
        self.visited = set()

        for x in range(n):
            if x not in self.visited:
                count += 1
                self.bfs(M, x)
        return count

    def bfs(self, M, x):
        q = [x]
        while q:
            cur = q.pop(0)
            for y in range(len(M)):
                if M[cur][y] and y not in self.visited:
                    self.visited.add(y)
                    q.append(y)