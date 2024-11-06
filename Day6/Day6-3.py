adjacency_list = {0: [], 1:[], 2:[], 3:[]}

edges = [[0,1],[0,2],[1,2],[2,3]]

for edge in edges:
    u, v = edge
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

print("adjacency_list")
for key, value in adjacency_list.items():
    print(f"{key}: {value}")

