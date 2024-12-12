# BFS (Breadth-First Search)
# • 가까운 정점부터 차례대로 탐색.
# • 큐(Queue)를 사용하여 구현함.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v): #간선 추가
        if u not in self.graph: 
            self.graph[u] = []
        self.graph[u].append(v) #키 u와 값 v를 연결 {u: v}


        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u) #키 v와 값 u를 연결 {v: u}
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ':', self.graph[vertex]) #최종적으로 연결된걸 보여줌

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)

print(graph.graph)

# 아래에 들어가는 입력그래프임(위의 graph를 생성했을때)
# {  
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 4, 5],
#     3: [1],
#     4: [2],
#     5: [2]
# }


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end = "")
            visited.add(vertex)
            queue.extend(
                [neighbor for neighbor in graph[vertex]
                if neighbor not in visited])
#               neighbors_to_add = []  # 방문하지 않은 노드를 저장할 리스트
#               for neighbor in graph[vertex]:  # 현재 노드의 인접 노드를 하나씩 순회
#                   if neighbor not in visited:  # 방문하지 않은 노드인지 확인
#                   neighbors_to_add.append(neighbor)  # 방문하지 않은 노드를 리스트에 추가

#               queue.extend(neighbors_to_add)  # 리스트를 큐에 추가

bfs(graph.graph,2 )