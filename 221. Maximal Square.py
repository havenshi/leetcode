class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if not m:
            return 0
        if m == 1:
            return max(int(x) for x in matrix[0])
        n = len(matrix[0])

        matrix = [list(map(lambda x: int(x), row)) for row in matrix]
        result = max(int(x) for x in matrix[0])
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    result = max(result, matrix[i][j] ** 2)
                elif matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                    result = max(result, matrix[i][j] ** 2)
        return result
