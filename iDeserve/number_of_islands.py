def find_islands(matrix):
    visited = [[False for _ in matrix[0]] for _ in matrix]
    count_of_ilands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited[i][j] = True
            elif matrix[i][j] == 1 and visited[i][j] == False:
                dfs(matrix, visited, i, j)
                count_of_ilands += 1
    print(count_of_ilands)


def dfs(matrix, visited, i, j):
    visited[i][j] = True
    if i-1 >= 0 and matrix[i-1][j-1] == 1 and visited[i-1][j] == False:
        dfs(matrix, visited, i-1, j)
    if j-1 >= 0 and matrix[i][j-1] == 1 and visited[i][j-1] == False:
        dfs(matrix, visited, i, j-1)
    if i+1 < len(matrix) and matrix[i+1][j] == 1 and visited[i+1][j] == False:
        dfs(matrix, visited, i+1, j)
    if j+1 < len(matrix[0]) and matrix[i][j+1] == 1 and visited[i][j+1] == False:
        dfs(matrix, visited, i, j+1)


matrix = [[1, 0, 1, 0, 1], 
          [1, 1, 0, 0, 0], 
          [0, 1, 0, 1, 1]]
find_islands(matrix)