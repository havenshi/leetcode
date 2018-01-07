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
        i, j = 0, n-1
        while i <= m-1 and j >= 0:
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
        #
        # up, bottom = 0, m - 1
        # while up + 1 < bottom:
        #     mid = up + (bottom - up) / 2
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] < target:
        #         up = mid
        #     else:
        #         bottom = mid
        # if matrix[up][0] == target or matrix[bottom][0] == target:
        #     return True
        # elif matrix[up][0] < target and matrix[bottom][0] > target:
        #     col = up
        # elif matrix[bottom][0] < target:
        #     col = bottom
        # else:
        #     return False
        #
        # left, right = 0, n - 1
        # while left + 1 < right:
        #     mid = left + (right - left) / 2
        #     if matrix[col][mid] == target:
        #         return True
        #     elif matrix[col][mid] < target:
        #         left = mid
        #     else:
        #         right = mid
        # if matrix[col][left] == target or matrix[col][right] == target:
        #     return True
        # else:
        #     return False