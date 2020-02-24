#Chess board size
n = 8

def knights_tour():
    '''
    The knight is placed on first block of an empty board,
    and moving according to the rules of chess, must visit each square exactly once
    '''
    board = [[-1 for i in range(n)] for j in range(n)]
    
    #move_x = [2, 1, 2, -1, -2, 1, -2, -1]
    #move_y = [1, 2, -1, 2, 1, -2, -1, -2]
    
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
    
    board[0][0] = 0
    
    if not (util(board, 0, 0, move_x, move_y, 1)):
        print('Solution does not exist')
    else:
        print_board(board)
    
    
def util(board, curr_x, curr_y, move_x, move_y, pos) :
    if pos == n*n:
        return True
    for i in range(n):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(board, new_x, new_y):
            board[new_x][new_y] = pos
            if util(board, new_x, new_y, move_x, move_y, pos+1) :
                return True
            board[new_x][new_y] = -1
    return False
    


def isSafe(board, x, y):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
        return True
    return False

def print_board(board):
    for i in range(n):
        print(board[i])
    

if __name__ == '__main__':
    knights_tour()