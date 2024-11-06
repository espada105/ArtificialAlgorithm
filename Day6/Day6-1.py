import numpy as np

n = 4

adjacency_matrix = np.zeros((n,n))

edges = [[0,1],[0,2],[1,2],[2,3]]

for edge in edges:
    u, v = edge
    adjacency_matrix [u][v] = 1
    adjacency_matrix [v][u] = 1

print("adjacency_matrix")
print(adjacency_matrix)
