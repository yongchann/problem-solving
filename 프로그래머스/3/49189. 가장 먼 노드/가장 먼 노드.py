from collections import deque

def solution(n, edges):
    # 각 노드의 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS를 통해 1번 노드에서 각 노드까지의 최단 거리 계산
    def bfs(start):
        queue = deque([start])
        distances = [-1] * (n + 1)
        distances[start] = 0
        max_distance = 0
        while queue:
            current = queue.popleft()
            current_distance = distances[current]
            for neighbor in graph[current]:
                if distances[neighbor] == -1:  # 아직 방문하지 않은 노드라면
                    distances[neighbor] = current_distance + 1
                    queue.append(neighbor)
                    max_distance = max(max_distance, current_distance + 1)
        return distances, max_distance
    
    # 1번 노드에서 모든 노드까지의 최단 거리 계산
    distances_from_1, max_distance = bfs(1)
    
    # 최장 거리를 가지는 노드들의 개수 세기
    farthest_nodes_count = 0
    for distance in distances_from_1:
        if distance == max_distance:
            farthest_nodes_count += 1
            
    return farthest_nodes_count