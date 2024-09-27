from collections import deque

def bfs(n, graph):
    areas = []
    visited = [False] * (n+1)
    for node in range(1, n+1):
        if not visited[node]: # 첫 방문 노드에 대해 bfs 탐색
            area_size = 1
            visited[node] = True
            q = deque([node])
            
            while q:
                now = q.popleft()
                for next_node in graph[now]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        area_size += 1
                        q.append(next_node)
                    
            areas.append(area_size)
            
    return areas

def solution(n, wires):
    min_diff = float('inf')
    graph = [set() for _ in range(n+1)]
    
    for wire in wires:
        graph[wire[0]].add(wire[1])
        graph[wire[1]].add(wire[0])
    
    for wire in wires:
        # 연결 제거
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        # 그래프 탐색
        areas = bfs(n, graph)
        min_diff = min(min_diff, abs(areas[0]-areas[1]))
        
        # 연결 복원
        graph[wire[0]].add(wire[1])
        graph[wire[1]].add(wire[0])
        
    return min_diff
        