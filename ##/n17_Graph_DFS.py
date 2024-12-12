# DFS, DepthFirstSearch
# - 작동 방식
# 1. 시작 노드에서 가능한 깊게 탐색을 진행
# 2. 더 이상 탐색할 노드가 없으면 이전 노드로 되돌아가서 다른 경로를 탐색
# 3. 모든 노드를 방문할 때까지 진행

# 용도
# 1. 그래프 경로탐색
# 2. 사이클 감지
# 3. 위상 정렬
# 4. 미로 찾기

def dfs_iteraive(graph, start):
    visited = set()
    stack = [start] 

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end='')
            visited.add(node)
            stack.extend(reversed(graph[node]))

print("\n DFS Iterative\n")

dfs_iteraive({0:[1,2,3],
            1:[0,2],
            2:[0,1,4],
            3:[0],
            4:[2]},0)

###########
# .pop ->node-> pop으로 node가 제거된 stack확인
# node를 visit에 넣고 현재 stack확인
# 위를 반복하기 전에 중복이면 stack에서 그냥 제거해라
###########


# 그래프 탐색 알고리즘

# - 깊이 우선 탐색 (DFS, Depth-First Search)
# 1. 재귀 또는 스택 사용
# 2. 한 방향을 끝까지 탐색후 돌아감

# - 너비 우선 탐색 (BFS, Breadth-First Search)
# 1. 큐를 사용
# 2. 인접한 정점을 먼저 탐색

def dfs_recursive(node, visited):
    if node not in visited:
        print(node, end='\n')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(neighbor, visited)
graph ={0:[1,2,3],
        1:[0,2],
        2:[0,1,4],
        3:[0],
        4:[2]}
visited_nodes = set()
print('\nDFS Recursive:')
dfs_recursive(0, visited_nodes)