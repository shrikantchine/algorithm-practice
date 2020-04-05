def rotate(matrix, i, j, N):
    t_matrix = zip(*matrix)
    for i, row in enumerate(t_matrix):
        matrix[i] = list(reversed(row))

    for i in matrix:
        print(i)


matrix = [ [1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 15, 16, 16]]

rotate(matrix, 0, 0, 4)