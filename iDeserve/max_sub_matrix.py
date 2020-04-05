def find_max_sub_matrix(matrix):
    result_matrix = [[0 for _ in matrix[0]] for _ in matrix]
    max_size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    result_matrix[i][j] = matrix[i][j]
                else:
                    result_matrix[i][j] = min(result_matrix[i-1][j], result_matrix[i][j-1], result_matrix[i-1][j-1]) + 1
                max_size = max(max_size, result_matrix[i][j])
    print(max_size)



matrix = [[1, 1, 1, 1, 0], 
          [0, 1, 1, 1, 1], 
          [0, 1, 1, 1, 1], 
          [1, 0, 1, 1, 1], 
          [0, 1, 1, 1, 0]]

find_max_sub_matrix(matrix)