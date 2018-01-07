class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        f = range(N)

        def find(x):
            while f[x] != x: x = f[x]
            return x

        for x in range(N):
            for y in range(x + 1, N):
                if M[x][y]: f[find(x)] = find(y)
        return sum(f[x] == x for x in range(N))
        
        # if not M:
        #     return 0
        # n = len(M)
        # matrix = [[0] * n for i in range(n)]
        # array = [0] * (n * n)
        # count = 0
        # for i in range(n):
        #     for j in range(n):
        #         if M[i][j] == 1:
        #             if i == 0 and j == 0:
        #                 matrix[i][j] = 1
        #                 count += 1
        #                 array[count - 1] = count
        #             elif i == 0:
        #                 if matrix[i][j - 1]:
        #                     matrix[i][j] = matrix[i][j - 1]
        #                 else:
        #                     count += 1
        #                     matrix[i][j] = count
        #                     array[count - 1] = count
        #             elif j == 0:
        #                 if matrix[i - 1][j]:
        #                     matrix[i][j] = matrix[i - 1][j]
        #                 else:
        #                     count += 1
        #                     matrix[i][j] = count
        #                     array[count - 1] = count
        #             else:
        #                 if matrix[i - 1][j] and matrix[i][j - 1]:
        #                     if matrix[i - 1][j] == matrix[i][j - 1]:
        #                         matrix[i][j] = matrix[i - 1][j]
        #                     else:
        #                         matrix[i][j] = matrix[i][j - 1]
        #                         array = map(lambda x: x if x != matrix[i - 1][j] else matrix[i][j - 1], array)
        #                         # replace upper value with left value
        #                 elif matrix[i - 1][j]:
        #                     matrix[i][j] = matrix[i - 1][j]
        #                 elif matrix[i][j - 1]:
        #                     matrix[i][j] = matrix[i][j - 1]
        #                 else:
        #                     count += 1
        #                     matrix[i][j] = count
        #                     array[count - 1] = count
        #         else:
        #             matrix[i][j] = 0
        #
        # return sum([1 for i in range(len(array)) if i + 1 == array[i]])