import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}


adjacency_list_graph = nx.Graph(graph)


plt.figure(figsize=(5, 5))


nx.draw(adjacency_list_graph, with_labels=True, node_color='lightcoral')

plt.title("Graph from Adjacency List")


plt.tight_layout()

plt.show()
