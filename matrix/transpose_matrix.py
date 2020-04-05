def transpose1(m):
    t_matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    for i in t_matrix:
        print(i)



matrix = [ [1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 15, 16, 16]]

transpose1(matrix)