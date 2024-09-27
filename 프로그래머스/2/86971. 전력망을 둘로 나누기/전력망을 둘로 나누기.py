from collections import deque

def bfs(n, graph):
    start, area_size = 1, 1
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])
    
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                area_size += 1
                q.append(next_node)
    return area_size

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
        count = bfs(n, graph)
        min_diff = min(min_diff, abs(count - (n-count)))
        
        # 연결 복원
        graph[wire[0]].add(wire[1])
        graph[wire[1]].add(wire[0])
        
    return min_diff
