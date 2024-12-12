import numpy as np

n = 4 #노드 수

adjacency_matrix = np.zeros((n, n)) #인접 행렬 초기화(무향 그래프 예시)
# adjacency_matrix = [[0] * n for _ in range(n)]
edges = [(0,1), (0,2), (1,2), (2,3 )] #엣지 추가
# 노드 0: 다른 노드 1, 2와 연결.
# 노드 1: 노드 0, 2와 연결.
# 노드 2: 노드 0, 1, 3과 연결.
# 노드 3: 노드 2와 연결.
for edge in edges:
    u, v = edge
    adjacency_matrix[u][v] = 1
    adjacency_matrix[v][u] = 1 

print('Adjacency Matrix:')
print(adjacency_matrix)



#     0 1 2 3   x축과 y으로 연결되면 1로 표시한거임
#
# 0   0 1 1 0
# 1   1 0 1 0
# 2   1 1 0 1
# 3   0 0 1 0

# 그래프의 종류
# 1. 무방향 그래프: 간선에 방향이 없음(친구관계)
# 2. 방향 그래프: 간선에 방향이 있음(웹페이지 링크)
# 3. 가중치 그래프: 간선에 가중치가 있음(도로거리)

# 그래프 표현 방법
# 1. 인접 행렬
# - 2차원 배열로 그래프를 표현
# - 간선의 유무를 0과 1로 표시
# 2. 인접 리스트
# - 각 정점에 연결된 정점을 리스트로 표현
# - 메모리 효율적