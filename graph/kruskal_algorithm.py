from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.weight = defaultdict(int)

    def add_edge(self, src, dest, weigth):
        self.graph[src].append(dest)
        self.weight[(src, dest)] = weigth

    