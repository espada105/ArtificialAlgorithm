import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [] 
        self.graph[u].append(v) #[u]가 키 v가 값
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u) #[v]가 키 u가 값
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])

graph = Graph()

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,3)

# 시각표현
adjacency_list_graph = nx.Graph(graph.graph) 
plt.figure(figsize=(5,5))
nx.draw(adjacency_list_graph, with_labels = True, node_color = 'lightcoral')
plt.title("Graph")
plt.tight_layout()
plt.show()