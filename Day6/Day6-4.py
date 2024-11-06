class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v].append(u)
        self.graph[v].append(i)
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])
