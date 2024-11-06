# class Graph:
#     def __init__(self):
#         self.graph = {}
        
#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.graph[u] = []
#         self.graph[u].append(v)
        
#         if v not in self.graph:
#             self.graph[v] = []
#         self.graph[v].append(u)
        
#     def print_graph(self):
#         for vertex in self.graph:
#             print(vertex, ":", self.graph[vertex])

# def dfs_iterative(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(f"Visit {node}")
#             visited.add(node)
#             stack.extend(reversed(graph[node]))


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)


# print("Adjacency List:")
# g.print_graph()


# print("\nDFS Iterative:")
# dfs_iterative(g.graph, 0)




0: [1, 2]
1: [0, 2]
2: [0, 1, 3]
3: [2]

