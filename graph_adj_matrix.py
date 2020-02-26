class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.adj_matrix[src][dest] = 1
        self.adj_matrix[dest][src] = 1

    def BFS(self, s):
        visited = [False] * self.V
        queue = []
        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in [index for index, val in enumerate(self.adj_matrix[s]) if val == 1]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
                    
    def DFS(self, s, visited=None):
        if not visited:
            visited = [False] * self.V
        for i in [index for index, val in enumerate(self.adj_matrix[s]) if val == 1]:
            if visited[i] == False:
                visited[i] = True
                print(i, end="  ")
                self.DFS(i, visited)


    def __str__(self):
        ret = ""
        for i, row in enumerate(self.adj_matrix):
            ret += '{} -> {}\n'.format(i, [index for index, val in enumerate(row) if val == 1])
        return ret

if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    print(str(graph))
    graph.BFS(2)
    print("\n")
    graph.DFS(2)