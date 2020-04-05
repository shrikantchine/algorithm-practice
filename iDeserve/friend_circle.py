def find_number_of_friend_circles(matrix, n):
    """
    Steps:
    1. Find a non-visited node
    2. Mark it as visited
    3. Add 1 to count of friend circles
    4. Run DFS at the node
    """
    friend_circle_count = 0
    visited=[False]*n
    for node in range(len(visited)):
        if visited[node]:
            continue
        friend_circle_count += 1
        dfs(matrix, node, visited)

    print(friend_circle_count)


def dfs(matrix, node, visited):
    visited[node] = True
    if node+1 < len(visited) and matrix[node][node+1] == 'Y':
        dfs(matrix, node+1, visited)

matrix = [['Y', 'Y', 'N', 'N'], 
          ['Y', 'Y', 'Y', 'N'], 
          ['N', 'Y', 'Y', 'N'], 
          ['N', 'N', 'N', 'Y']]

find_number_of_friend_circles(matrix, 4)