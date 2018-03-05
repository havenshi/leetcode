def dist(matrix):
    array = []
    n = len(matrix[0])
    for i in range(n):
        tmp = [matrix[j][i] for j in range(len(matrix))]
        if tmp not in array:
            array.append(tmp)
    return array
matrix = [[1,1,1],[-1,-3,-3],[-1,-1,-1]]
print dist(matrix)