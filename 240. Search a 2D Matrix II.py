class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        i, j = 0, n - 1
        while i <= m - 1 and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

        # binary search
        #
        # m = len(matrix)
        # if m == 0:
        #     return False
        # n = len(matrix[0])
        # if n == 0:
        #     return False
        # up, down = 0, m - 1
        #
        # while up <= down:
        #     left, right = 0, n - 1
        #     while left + 1 < right:
        #         mid = (left + right) / 2
        #         if matrix[up][mid] == target:
        #             return True
        #         elif matrix[up][mid] < target:
        #             left = mid
        #         else:
        #             right = mid
        #     if matrix[up][left] == target or matrix[up][right] == target:
        #         return True
        #     else:
        #         up += 1
        #
        # return False