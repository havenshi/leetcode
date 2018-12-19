# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# Input:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
# Output:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

# Time(O^3)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(A)==0 or len(B)==0:
            return 0

        m, n = len(A), len(B[0])
        res = [ [0]*n for i in range(m) ]

        for i in range(m):
            i_zero = True
            for ind in range(n):
                if A[i][ind]!=0:
                    i_zero = False
                    break

            for j in range(n):
                if i_zero==True:
                    res[i][j] = 0
                    continue

                for mul_ind in range(len(A[0])):
                    res[i][j] += A[i][mul_ind] * B[mul_ind][j]

        return res
