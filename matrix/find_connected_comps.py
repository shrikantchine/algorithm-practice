def find_connected_components(matrix):
    visited = [[False for _ in matrix] for _ in matrix[0]]
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                visited[row][col] = True
            if not visited[row][col] and matrix[row][col] == 1:
                dfs(matrix, row, col, visited)
                count += 1
    return count

def dfs(matrix, row, col, visited):
    visited[row][col] = True
    visitables = find_visitables(matrix, row, col)
    for location in visitables:
        if not visited[location[0]][location[1]] and matrix[location[0]][location[1]] == 1:
            dfs(matrix, location[0], location[1], visited)

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

matrix = [ [0, 1, 1, 0], 
           [1, 0, 0, 1], 
           [1, 1, 0, 0], 
           [1, 1, 1, 1]]

print(find_connected_components(matrix))