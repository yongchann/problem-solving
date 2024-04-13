from collections import deque

def solution(n, wires):
    answer = float("INF")
    for i in range(n-1):
        answer = min(answer, search(n, wires[:i] + wires[i+1:]))
    return answer

def search(n, wires):
    ret = []
    
    # 초기화
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    for node in range(1, n+1):
        if visited[node]:
            continue
            
        # 방문하지 않은 첫 노드에 대해 bfs 탐색
        cnt = 1
        q = deque([node])
        visited[node] = True
        while q:
            _node = q.popleft()
            for connected_node in graph[_node]:
                if not visited[connected_node]:
                    cnt += 1
                    visited[connected_node] = True
                    q.append(connected_node)
            
        ret.append(cnt)
    return abs(ret[0]-ret[1])        
    