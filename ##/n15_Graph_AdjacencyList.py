adjacencyList = {0: [], 1: [], 2: [], 3: []} #dictionary로 초기화

edges = [(0, 1), (0,2), (1,2), (2,3)] # 

for edge in edges:
    u, v = edge
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)

for key, value in adjacencyList.items():
    print(f"{key}: {value}")

# 0: [1, 2]
# 1: [0, 2]
# 2: [0, 1, 3]
# 3: [2]
# 노드0은 1,2랑 연결
# 노드1은 0,2랑 연결 ... 나머지도 같음