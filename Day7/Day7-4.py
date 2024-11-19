# 0:[1,3]
# 1:[0,2]
# 2:[0,2]
# 3:[1,3,4]
# 4:[2,5]
# 5:[4]


from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
    def bfs(self, start):
        visited = set()        # 방문한 노드를 저장할 집합
        queue = deque([start]) # 큐 생성 및 시작 노드 추가
        visited.add(start)     # 시작 노드를 방문 처리
        
        while queue:           # 큐가 빌 때까지 반복
            vertex = queue.popleft()  # 큐에서 노드를 하나 꺼냄
            print(vertex, end=" ")    # 현재 노드 출력
            
            # 현재 노드의 이웃 노드들을 확인
            for neighbor in self.graph[vertex]:
                # 방문하지 않은 이웃 노드라면
                if neighbor not in visited:
                    visited.add(neighbor)  # 방문 처리
                    queue.append(neighbor) # 큐에 추가

# 그래프 생성 및 테스트
g = Graph()

# 주어진 그래프 구조 추가
edges = [
    (0,1), (0,3),
    (1,0), (1,2),
    (2,0), (2,2),
    (3,1), (3,3), (3,4),
    (4,2), (4,5),
    (5,4)
]

for u, v in edges:
    g.add_edge(u, v)

# BFS 실행 (0번 노드부터 시작)
print("BFS 탐색 결과:")
g.bfs(0)