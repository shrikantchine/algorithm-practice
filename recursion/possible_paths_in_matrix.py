'''
The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.
'''

def possible_paths(M, N):
    return possible_paths_helper(M, N, 0, 0)

def possible_paths_helper(M, N, row, col):
    if row >= M or col >= N:
        return 0
    if row == M-1 and col == N-1:
        return 1
    return possible_paths_helper(M, N, row+1, col) + possible_paths_helper(M, N, row, col+1)

print(possible_paths(3, 3))
print(possible_paths(2, 8))