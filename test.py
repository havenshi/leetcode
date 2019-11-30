
def solution(numRows, numColumns, lot):
    if numRows == 0 or numColumns == 0:
        return -1

    matrix = [row[:] for row in lot]

    q = [((0, 0), 0)]
    matrix[0][0] = 0
    while q:
        (x, y), step = q.pop(0)
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x + dx < numRows and 0 <= y + dy < numColumns:
                if matrix[x + dx][y + dy] == 9:
                    return step + 1
                elif matrix[x + dx][y + dy] == 1:
                    matrix[x + dx][y + dy] = 0
                    q.append(((x + dx, y + dy), step + 1))
    return -1



if __name__ == '__main__':
    # treasure_map = [[1,0,0],
    #                 [1,0,0],
    #                 [1,9,1]]
    treasure_map = [[1,1,1,1],
                    [0,1,1,1],
                    [0,1,0,1],
                    [1,1,9,1],
                    [0,0,1,1]]
    print(solution(5,4,treasure_map))