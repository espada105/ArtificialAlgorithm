from collections import deque

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
#         for node in self.graph:
#             print(f"{node}: {self.graph[node]}")

# g = Graph()
# g.add_edge(1, 3)
# g.add_edge(0, 2)
# g.add_edge(0, 2)
# g.add_edge(1, 3, 4)
# g.add_edge(2, 5)
# g.add_edge(4)
# g.print_graph()

#     0
#     |
#     1
#    /|\
#   / | \
#  2  |  3
#   \ | /
#    \|/
#     4

graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3],
}


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print(f"\n시작 노드: {start}")
    print(f"큐 상태: {list(queue)}")
    
    while queue:
        node = queue.popleft()
        print(f"\n큐에서 꺼낸 노드: {node}")
        
        if node not in visited:
            print(f"노드 {node} 방문 및 출력", end=' -> ')
            print(node, end=' ')
            
            visited.add(node)
            print(f"\n방문 노드 집합: {visited}")
            
            new_nodes = [neighbo for neighbo in graph[node] if neighbo not in visited]
            print(f"추가할 인접 노드들: {new_nodes}")
            
            queue.extend(new_nodes)
            print(f"큐 상태: {list(queue)}")
        else:
            print(f"노드 {node}는 이미 방문함")
            
    return visited

bfs(graph, 0)