def longest_path(matrix):
    max_len = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            max_len = max(max_len, dfs(matrix, row, col))
    return max_len

def dfs(matrix, row, col):
    curr = matrix[row][col]
    visitables = find_visitables(matrix, row, col)
    max_len = 1
    for loc in visitables:
        if matrix[loc[0]][loc[1]] - curr == 1:
            max_len = max(dfs(matrix, loc[0], loc[1])+1, max_len)
    return max_len
            

def find_visitables(matrix, row, col):
    visitables = []
    if row-1 >= 0:
        visitables.append((row-1, col))
    if row+1 < len(matrix):
        visitables.append((row+1, col))
    if col-1 >= 0:
        visitables.append((row, col-1))
    if col+1 < len(matrix[0]):
        visitables.append((row, col+1))
    return visitables

matrix = [[1, 2, 9],
          [5, 3, 8],
          [4, 6, 7]]

print(longest_path(matrix))