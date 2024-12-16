from collections import deque

def bfs_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 #시작노드의 거리를 0으로

    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

                if neighbor == end:
                    return distances[neighbor]
                
    return float('inf')
# 초기 상태: distances = {0: inf, 1: inf, 2: 0, 3: inf, 4: inf, 5: inf}, queue = [2]
# 현재 노드: 2, queue 상태: [] 거리 0
# 추가된 노드: 0, 거리 업데이트: distances[0] = 1
# 추가된 노드: 4, 거리 업데이트: distances[4] = 1
# 추가된 노드: 5, 거리 업데이트: distances[5] = 1

# 현재 노드: 0, queue 상태: [4, 5]
# 추가된 노드: 1, 거리 업데이트: distances[1] = 2

# 현재 노드: 4, queue 상태: [5, 1]
# 현재 노드: 5, queue 상태: [1]
# 현재 노드: 1, queue 상태: []

# 추가된 노드: 3, 거리 업데이트: distances[3] = 3
# 목표 노드 3에 도달, 최단 거리: 3

# 최단 경로 길이: 3

start = 2
end = 3

graph = {  
    0: [1, 2], #2번째로 실행
    1: [0, 3], 
    2: [0, 4, 5], # 1번째로 실행 0-> 4-> 5 ,inf인것만 queue에 추가(0은 있으니 4와 5추가), 1차 for문 종료
    3: [1], 
    4: [2], 
    5: [2], 
}
shortest_path_length = bfs_shortest_path(graph, start, end)
print(f"최단 경로 길이: {shortest_path_length}")    