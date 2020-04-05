from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def is_cyclic(self):
        parent = [-1] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y) 
    
    def find_parent(self, parent, node):
        if parent[node] == -1:
            return node
        else: 
            return self.find_parent(parent, parent[node])

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

g = Graph(3) 
g.add_edge(0, 1) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
  
if g.is_cyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")