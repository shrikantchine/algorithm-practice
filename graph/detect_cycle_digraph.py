from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if self.is_cyclic_helper(node, visited, rec_stack) == True:
                return True
        return False

    def is_cyclic_helper(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.is_cyclic_helper(neighbour, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbour] == True:
                return True
        rec_stack[node] = False
        return False


g = Graph(4) 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
if g.is_cyclic() == 1: 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")