'''
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.
'''

def flood_fill(matrix, x, y, color):
    flood_fill_helper(matrix, x, y, color, matrix[x][y])
    

def flood_fill_helper(matrix, x, y, color, val):
    if not is_valid_move(matrix, x, y):
        return
    if matrix[x][y] == val:
        matrix[x][y] = color
    else:
        return
    flood_fill_helper(matrix, x+1, y, color, val)
    flood_fill_helper(matrix, x-1, y, color, val)
    flood_fill_helper(matrix, x, y+1, color, val)
    flood_fill_helper(matrix, x, y-1, color, val)

def is_valid_move(matrix, x, y):
    x_valid = x < len(matrix) and x >= 0
    y_valid = x < len(matrix[0]) and y >= 0
    return x_valid and y_valid


screen = [  [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 1, 1],
            [1, 2, 2, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 0, 1, 0],
            [1, 1, 1, 2, 2, 2, 2, 0],
            [1, 1, 1, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 2, 2, 1]]

flood_fill(screen, 4, 4, 3)

for i in range(len(screen)):
    print(screen[i])