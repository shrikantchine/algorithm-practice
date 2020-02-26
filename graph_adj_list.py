class Graph(object):
    def __init__(self, V=None):
        self.V = V
        self.adj_list = {}
        if V: 
            for i in range(V):
                self.adj_list[i] = []
        
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def BFS(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end="  ")
            for i in self.adj_list[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, s, visited=None):
        if not visited:
            visited = [False] * self.V
        for i in self.adj_list[s]:
            if visited[i] == False:
                visited[i] = True
                print(i, end="  ")
                self.DFS(i, visited)

    def __str__(self):
        ret = ""
        for key, val in self.adj_list.items():
            ret += '{} -> {}\n'.format(key, val)
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