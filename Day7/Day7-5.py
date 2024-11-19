from collections import deque

def bfs_shortest_path(graph, start, end):
    # 모든 노드의 거리를 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드의 거리는 0
    
    # BFS를 위한 큐 초기화
    queue = deque([start])
    
    while queue:
        current_node = queue.popleft()
        
        # 현재 노드의 이웃 노드들을 탐색
        for neighbor in graph[current_node]:
            # 아직 방문하지 않은 노드라면
            if distances[neighbor] == float('inf'):
                # 현재까지의 거리 + 1
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
            
            # 목표 노드에 도달했다면 거리 반환
            if neighbor == end:
                return distances[neighbor]
    
    # 목표 노드에 도달할 수 없는 경우
    return float('inf')

# 그래프 정의
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [0, 2],
    3: [1, 3, 4],
    4: [2, 5],
    5: [4]
}

start = 0  # 시작 노드
end = 5    # 목표 노드

# 최단 경로 길이 계산
shortest_path_length = bfs_shortest_path(graph, start, end)
print(f"최단 경로의 길이: {shortest_path_length}")