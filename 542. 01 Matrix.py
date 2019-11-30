# bfs
# why wrong answer?
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if not m: return None
        n = len(matrix[0])
        new_matrix = [[float('Inf') if matrix[i][j] == 1 else 0 for j in range(n)] for i in range(m)]

        visits = []
        q = []
        for i in range(m):
            for j in range(n):
                if new_matrix[i][j] == 0:
                    q.append((i, j))
        step = 0
        while q:
            step += 1
            new_q = []
            for (i, j) in q:
                if (i, j) in visits:
                    continue
                coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for coord in coords:
                    newI, newJ = i + coord[0], j + coord[1]
                    if newI in range(0, m) and newJ in range(0, n) and new_matrix[newI][newJ] == float('Inf'):
                        visits.append((newI, newJ))
                        new_matrix[newI][newJ] = step
                        new_q.append((newI, newJ))
            q = new_q

        return new_matrix


# dfs TLE
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if not m: return None
        n = len(matrix[0])
        new_matrix = [[float('Inf') if matrix[i][j] == 1 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if new_matrix[i][j] == 0:
                    self.dfs(new_matrix, i, j, m, n, 1)
        return new_matrix

    def dfs(self, new_matrix, i, j, m, n, distance):
        coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for coord in coords:
            newI, newJ = i + coord[0], j + coord[1]
            if newI in range(0, m) and newJ in range(0, n) and new_matrix[newI][newJ] > distance:
                new_matrix[newI][newJ] = distance
                self.dfs(new_matrix, newI, newJ, m, n, distance + 1)