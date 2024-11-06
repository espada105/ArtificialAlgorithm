import networkx as nx
import matplotlib.pyplot as plt

# Example adjacency list
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# Create a Graph from the adjacency list
adjacency_list_graph = nx.Graph(graph)

# Set the figure size
plt.figure(figsize=(5, 5))

# Draw the graph with labels and a node color
nx.draw(adjacency_list_graph, with_labels=True, node_color='lightcoral')

# Add a title to the plot
plt.title("Graph from Adjacency List")

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
