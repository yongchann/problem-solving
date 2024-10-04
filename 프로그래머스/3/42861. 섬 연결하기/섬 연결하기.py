from heapq import heappush, heappop

def solution(n, costs):
    graph = [set() for _ in range(n)]
    for a, b, cost in costs:
        graph[a].add((b, cost))
        graph[b].add((a, cost))
    
    start = 0
    visited = set()
    pq = [(0, start)]
    answer = 0
    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        
        answer += cost
        visited.add(node)
        
        for neighbor, cost in graph[node]:
            heappush(pq, (cost, neighbor))
    return answer