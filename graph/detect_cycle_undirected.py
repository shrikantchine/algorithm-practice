from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def is_cyclic(self):
        visisted = [False] * self.V
        for node in range(self.V):
            if visisted[node] == False:
                if self.is_cyclic_helper(node, visisted, -1) == True:
                    return True
        return False

    def is_cyclic_helper(self, node, visited, parent):
        visited[node] = True
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.is_cyclic_helper(neighbour, visited, node) == True:
                    return True
            elif parent != neighbour:
                return True
        return False

g = Graph(5) 
g.add_edge(1, 0) 
g.add_edge(0, 2) 
g.add_edge(2, 0) 
g.add_edge(0, 3) 
g.add_edge(3, 4) 
  
if g.is_cyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")
g1 = Graph(3) 
g1.add_edge(0,1) 
g1.add_edge(1,2) 
  
  
if g1.is_cyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")