class graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
        
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])
        
    def dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs_recursive(neighbor, visited)


graph = graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print(graph.graph)
