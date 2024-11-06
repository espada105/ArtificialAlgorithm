class Graph:
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

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))

# Create an instance of Graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

# Print the adjacency list
g.print_graph()

# Perform DFS Iterative
print("\nDFS Iterative:")
dfs_iterative(g.graph, 0)
