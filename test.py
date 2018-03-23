# Time:  O(n)
# Space: O(1)
def zigzag(matrix):
    m = len(matrix)
    row, col = 0, 0
    ans = []
    while row < m:
        while col < len(matrix[row]):
            if col < len(matrix[row]):
                ans.append(matrix[row][col])
            col += 1
        col = 0
        row += 1
    return ans

print zigzag([[1,2,3],
               [4,5,6,7],
               [8,9]])