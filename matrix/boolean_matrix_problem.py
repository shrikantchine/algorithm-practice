def boolean_matrix(matrix):
    locations = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                locations.extend(find_locations(matrix, row, col))
    
    for loc in locations: 
        matrix[loc[0]][loc[1]] = 1

    for i in matrix:
        print(i)


def find_locations(matrix, row, col):
    locations = []
    x = row-1
    while x >= 0:
        locations.append((x, col))
        x -= 1
    y = col-1
    while y >= 0:
        locations.append((row, y))
        y -= 1
    x = row+1
    while x < len(matrix):
        locations.append((x, col))
        x += 1
    y = col +1
    while y < len(matrix[0]):
        locations.append((row, y))
        y += 1
    return locations


matrix = [[1, 0], 
          [0, 0]]

boolean_matrix(matrix)

matrix = [[0, 0, 0], [0, 0, 1]]
boolean_matrix(matrix)

matrix = [[1, 0, 0], 
          [1, 0, 0], 
          [1, 0, 0], 
          [0, 0, 0]]

boolean_matrix(matrix)