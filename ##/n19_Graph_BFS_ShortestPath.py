from collections import deque

def bfs_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

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

start = 2
end = 3

graph = {  
    0: [1, 2],
    1: [0, 3],
    2: [0, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
shortest_path_length = bfs_shortest_path(graph, start, end)
print(f"최단 경로 길이: {shortest_path_length}")