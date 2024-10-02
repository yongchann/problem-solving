from collections import deque

n = int(input())
graph = []
for i in range(n):
    conns = list(map(int, input().split()))
    graph.append([i for i, conn in enumerate(conns) if conn == 1])

for i in range(n):
    dist = [0] * n
    q = deque([i])
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not dist[neighbor]:
                dist[neighbor] = 1
                q.append(neighbor)
                
    print(*dist)